from procs.console import console
from procs.procs_utils import encrypt_file, decrypt_file, subir_con_progreso
import time
import pandas as pd
from datetime import datetime
import csv
import os
from zipfile import ZipFile
import shutil
import glob
import tarfile
from procs.DictsAndLists import lista, listaTCA


def exec_proc(engine, proc: str):
    with console.status("Ejecutando proceso...", spinner="aesthetic"):
        console.log(f"Ejecutando store [bold red]{proc.upper()}.")
        time.sleep(2)
        # console.log(f"EXEC {proc}")
        with engine.connect() as conn, conn.begin():
            conn.execute(f"EXEC {proc}")
    return console.log("El proceso termino exitosamente")


def make_paq(engine, form: dict):
    with console.status("Creando carpetas/archivos...", spinner="aesthetic"):
        # Buscamos el numero de lote y lo guardamos en loteN.
        lote = pd.read_sql_query(
            f"""SELECT numero
                FROM [dbo].[numeracion_paquetes]
                WHERE Paquete='{form["lotenombre"]}' 
            """,
            con=engine,
        )
        loteN = str(lote.iloc[0]["numero"])
        # Guardamos el formato para la fecha que se va usar para todo.
        loteF = datetime.today().strftime("%Y%m%d")
        # Creamos la carpeta, si ya existian avisa y sigue.
        loteC = form["direccion"] + loteN + "_" + loteF
        try:
            os.makedirs(f"{loteC}")
            console.log(f"Se creo la carpeta '{loteC}'.")
        except:
            console.log("La carpeta del paquete de este lote ya existia.")
        # Loopeamos los archivos del dict para salir.
        for key, value in form["files"].items():
            console.rule(f"Preparando '{key}'", align="left")
            time.sleep(2)
            # Leemos la tabla de salida del paquete.
            console.log(f"Leyendo tabla [blue]{value['tabla']}[/blue]")
            time.sleep(2)
            # paq = pd.read_sql_table(value["tabla"], con=engine, schema="dbo")
            paq = pd.read_sql_query(
                f"SELECT * FROM {value['tabla']} {value['whereorder']}", con=engine
            )
            paq.dropna(inplace=True)
            console.log("Hecho.")
            # Preparamos el nombre del archivo.
            if value["replace"] == "AAAAMMDD":
                archivo = value["archivo"].replace(value["replace"], loteF)
            else:
                archivo = value["archivo"].replace(value["replace"], loteN)
            # Creamos cabecera para 1252 y 1253.
            if key in ("Paquete 0", "Paquete 4"):
                # Contamos los rows del DF.
                rows = paq.shape[0]
                zerosC = "0" * (5 - len(str(rows)))
                paq.columns = [f"{value['cabecera']}{loteN}{loteF}{zerosC}{rows+1}"]
            # Lo guardamos en CSV/TXT dependiendo.
            paq.to_csv(
                f"{loteC}\\{archivo}",
                header=value["header"],
                index=None,
                sep=value["sep"],
                encoding="ansi",
                mode=value["mode"],
                line_terminator=value["line_terminator"],
                quoting=csv.QUOTE_NONE,
                escapechar=value["escapechar"],
            )
            # Creamos el archivo replica para el 1253.
            if key in ("Paquete 4"):
                file1 = open(f"{loteC}\\{archivo}", "r")
                file2 = open(f"{loteC}\\Padron_Efectores_Lote.txt", "w")
                for line in file1.readlines():
                    if line.startswith("02"):
                        file2.write(line)
                file2.close()
                file1.close()
                console.log("El archivo 'Padron Efectores Lote' fue creado con exito")
            # Borramos la ultima linea en blanco.
            with open(f"{loteC}\\{archivo}") as f:
                lines = f.readlines()
                last = len(lines) - 1
                lines[last] = lines[last].replace("\r", "").replace("\n", "")
            with open(f"{loteC}\\{archivo}", "w") as wr:
                wr.writelines(lines)
            # Encriptamos si son paquetes 2.
            if key in ("p2"):
                encrypt_file(
                    f"{loteC}\\{archivo}",
                    f"{loteC}\\{archivo}.gpg",
                )
            # Terminamos.
            console.log(f"El archivo '{key}' fue creado con exito")
        # Al terminar mostramos la carpeta y los archivos creados.
        os.startfile(loteC)
    return 0


def upl_paq(engine, form: dict, pqt: list) -> int:
    # with console.status("Subiendo paquete...", spinner="aesthetic"):
    # Buscamos el numero de lote y lo guardamos en loteN.
    lote = pd.read_sql_query(
        f"""SELECT numero
            FROM [dbo].[numeracion_paquetes]
            WHERE Paquete='{form["lotenombre"]}' 
        """,
        con=engine,
    )
    loteN = str(lote.iloc[0]["numero"])
    # Guardamos el formato para la fecha que se va usar para todo.
    loteF = datetime.today().strftime("%Y%m%d")
    # Creamos la carpeta, si ya existian avisa y sigue.
    loteC = form["direccion"] + loteN + "_" + loteF
    try:
        os.makedirs(f"{loteC}")
        console.log(f"Se creo la carpeta '{loteC}'.")
    except:
        console.log("La carpeta del paquete de este lote ya existia.")
    engine.execute(f"TRUNCATE TABLE {form['SCP']['tabla']} ")
    for file in pqt:
        if not form["lotenombre"] == "F.1253v":
            df = pd.read_csv(
                file,
                encoding=form["read_csv"]["encoding"],
                compression=form["read_csv"]["compression"],
                sep=form["read_csv"]["sep"],
                names=form["read_csv"]["names"],
                delimiter=form["read_csv"]["delimiter"],
                engine=form["read_csv"]["engine"],
                dtype=form["read_csv"]["dtype"],
                index_col=None,
            )
            console.log(f"Subiendo '{file}'.")
            subir_con_progreso(
                df,
                engine,
                form["SCP"]["tabla"],
                repl=form["SCP"]["repl"],
                dtypes=form["SCP"]["dtype"],
            )
        else:
            sintysUP(engine, file)
        # Muevo el paquete a la locacion.
        console.log(f"Moviendo '{file}' a la carpeta del lote.")
        try:
            shutil.move(file, f"{loteC}\\{file}")
            console.log(f"Listo!.")
        except:
            print("Hubo un problema moviendo los archivos.")
    return 0


def sintysUP(engine, pqt):
    # Armamos la salida del decrypt sacandole los ultimos 4 lugares a la direccion.
    paquete = pqt[0][: len(pqt[0]) - 4]

    # Desencriptamos.
    decrypt_file(pqt[0], "Eze2kftw!", paquete)

    # Abrimos el GZ en python para manosearlo por dentro.
    TarP3 = tarfile.open(paquete, "r:gz")
    print(f"Encontrado: {paquete}")

    # Buscamos los archivos dentro del GZ y los subimos a la DB.
    print("Subiendo vuelta SyNTIS.")
    for file in lista:
        engine.execute(f"DELETE FROM DTS_EntradaSintys_{file['Nombre']}_2019")
        try:
            filename = [name for name in TarP3.getnames() if file["Nombre"] in name]

            # En el caso de B00 hay chances de que venga un archivo VARIOS.B00, asi q lo filtramos.
            if file["Nombre"] == "B00":
                filename = [k for k in filename if not "VARIOS" in k]

            txt = TarP3.extractfile(filename[0])
            df = pd.read_csv(
                txt,
                sep="\t",
                encoding="ansi",
                dtype=file["dtype"],
                names=file["dtype"].keys(),
                header=0,
            )
            print(f"Subiendo {file['Nombre']}")
            subir_con_progreso(
                df, engine, f"DTS_EntradaSintys_{file['Nombre']}_2019", repl=False
            )
        except IndexError:
            console.log(f"'\n{file['Nombre']} no esta en la vuelta.")
            continue

    engine.execute(f"DELETE FROM DTS_EntradaSintys_TCA_2019")

    for file in listaTCA:
        try:
            filename = [name for name in TarP3.getnames() if file["Nombre"] in name]
            txt = TarP3.extractfile(filename[0])
            df = pd.read_csv(txt, sep="\t", encoding="ansi", dtype=file["dtype"])
            print(f"Subiendo {file['Nombre']}")
            df.insert(loc=0, column="tabla", value=file["Nombre"])
            subir_con_progreso(df, engine, "DTS_EntradaSintys_TCA_2019", repl=False)
        except IndexError:
            console.log(f"\n{file['Nombre']} no esta en la vuelta.\n")
            continue

    # Cerramos el GZ para que no haya error al moverlo.
    TarP3.close()
