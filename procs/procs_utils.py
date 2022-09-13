import sqlalchemy
import pandas as pd
from tqdm import tqdm
import sys
import gnupg
from rich.console import Console
from rich.progress import Progress

console = Console()


def encrypt_file(file, output_file):
    gpg = gnupg.GPG()
    with open(file, "rb") as f:
        status = gpg.encrypt_file(
            f,
            recipients=["bases@sintys.gov.ar", "emore@desarrollosocial.gob.ar"],
            output=output_file,
        )
    if status.ok:
        console.log(f"Se encripto '{file}' con exito.")
    else:
        console.log(status.stderr)


def decrypt_file(file, passphrase, output_file):
    gpg = gnupg.GPG()
    with open(file, "rb") as f:
        status = gpg.decrypt_file(f, passphrase=passphrase, output=output_file)
    if status.ok:
        console.log(f"Se desencripto '{file}' con exito.")
    else:
        console.log(status.stderr)


def chunker(seq, size):
    # from http://stackoverflow.com/a/434328
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def subir_con_progreso(df, engine, table, dtypes=None, divchunk=25, repl=True):
    con = engine.connect()
    if len(df) < 25:
        divchunk = 1
    chunksize = int(len(df) / divchunk)  # 10%
    with tqdm(total=len(df), colour="green") as pbar:
        for i, cdf in enumerate(chunker(df, chunksize)):
            if repl:
                replace = "replace" if i == 0 else "append"
            else:
                replace = "append"
            cdf.to_sql(
                con=con,
                name=f"{table}",
                if_exists=replace,
                index=False,
                schema="dbo",
                dtype=dtypes,
            )
            pbar.update(chunksize)
    con.close()
    # with Progress() as progress:
    #     task1 = progress.add_task("[green]Subiendo...", total=len(df))
    #     for i, cdf in enumerate(chunker(df, chunksize)):
    #         if repl:
    #             replace = "replace" if i == 0 else "append"
    #         else:
    #             replace = "append"
    #         cdf.to_sql(
    #             con=con,
    #             name=f"{table}",
    #             if_exists=replace,
    #             index=False,
    #             schema="dbo",
    #             dtype=dtypes,
    #         )
    #         progress.update(task1, advance=chunksize)
