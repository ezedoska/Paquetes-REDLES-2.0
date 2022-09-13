from procs import Paquetes, Login, Estado
from procs.PaquetesDICT import paquetesOUT, paquetesIN

from consolemenu import *
from consolemenu.items import *
from pyfiglet import Figlet

"""
[Selector de paquetes a procesar por medio del consolemenu.]
"""


def main():
    # Llamamos la funcion que loguea y guarda la coneccion para uso posterior.
    db = Login.go()

    # Seleccionamos el font para fig.
    f = Figlet(font="slant")
    # Creamos el menu de seleccion con las funciones.
    menu = ConsoleMenu(
        "\n" + f.renderText("Paquetes"), "Seleccione el paquete que desea procesar."
    )

    # Creamos cada item y las funciones que contienen.
    estado = FunctionItem(
        "Ver estado de los paquetes.",
        Estado.go,
        # args=(db["engine"]),
        kwargs={"engine": db["engine"]},
        menu=menu,
        should_exit=False,
    )
    paquete0 = FunctionItem(
        "Ejecutar Paquete 0.(F1252)",
        Paquetes.send,
        args=(db["engine"], paquetesOUT["F1252"]),
        kwargs=None,
        menu=menu,
        should_exit=False,
    )
    paquete1 = FunctionItem(
        "Ejecutar Paquete 1.(F1252v)",
        Paquetes.recv,
        args=(db["engine"], paquetesIN["F1252v"]),
        kwargs=None,
        menu=menu,
        should_exit=False,
    )
    paquete2 = FunctionItem(
        "Ejecutar Paquete 2.(FSINTYS)",
        Paquetes.send,
        args=(db["engine"], paquetesOUT["FSINTYS"]),
        kwargs=None,
        menu=menu,
        should_exit=False,
    )
    paquete4 = FunctionItem(
        "Ejecutar Paquete 4.(F1253)",
        Paquetes.send,
        args=(db["engine"], paquetesOUT["F1253"]),
        kwargs=None,
        menu=menu,
        should_exit=False,
    )
    paquete7 = FunctionItem(
        "Ejecutar Paquete 7.(F1257)",
        Paquetes.send,
        args=(db["engine"], paquetesOUT["F1257"]),
        kwargs=None,
        menu=menu,
        should_exit=False,
    )
    paquete8 = FunctionItem(
        "Ejecutar Paquete 8.(F1258)",
        Paquetes.send,
        args=(db["engine"], paquetesOUT["F1258"]),
        kwargs=None,
        menu=menu,
        should_exit=False,
    )
    paquete14 = FunctionItem(
        "Ejecutar Paquete 14.(F1253ADH)",
        Paquetes.send,
        args=(db["engine"], paquetesOUT["F1253ADH"]),
        kwargs=None,
        menu=menu,
        should_exit=False,
    )
    paquete15 = FunctionItem(
        "Ejecutar Paquete 15.(F1253ADHv)",
        Paquetes.recv,
        args=(db["engine"], paquetesIN["F1253ADHv"]),
        kwargs=None,
        menu=menu,
        should_exit=False,
    )

    # Añadimos las funciones al menu.
    menu.append_item(estado)
    menu.append_item(paquete0)
    menu.append_item(paquete1)
    menu.append_item(paquete2)
    menu.append_item(paquete4)
    menu.append_item(paquete7)
    menu.append_item(paquete8)
    menu.append_item(paquete14)
    menu.append_item(paquete15)
    # Mostramos el menu.
    menu.show()


if __name__ == "__main__":
    main()
