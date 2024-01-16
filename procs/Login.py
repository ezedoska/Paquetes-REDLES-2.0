import getpass
import urllib
from sqlalchemy import create_engine
from rich import print
from rich.panel import Panel
from rich.text import Text
import time
import os
import pandas as pd

# from procesos import discordbot as dbot
from rich.prompt import Prompt


def go():
    """
    [Logueo a la DB devuelve las conecciones para usar]
    Returns:
        [ret] -- [diccionario con engine y conneccion a SQL alchemy]
    """
    print(
        Panel(
            Text("BASE ADM_EFECTORES", justify="center"),
            title="[red]LOGIN",
        )
    )
    while True:
        # creamos la variable con los datos del server
        computer = os.environ["COMPUTERNAME"]
        if "vdm-" in computer.lower():
            Ip = "192.168.1.40,21433"
        else:
            # Ip = "localhost,21433"
            Ip = "127.0.0.1,21433"
        server = (
            r"Driver={SQL Server};"
            + f"Server={Ip};"
            + f"Database=adm_efectores;UID=IDFALSA;PWD=PasswordFalso;"
        )
        # Ip = ".\OUTER_HEAVEN"
        # server = (
        #     r"Driver={SQL Server};"
        #     + f"Server={Ip};"
        #     + f"Database=test;Trusted_Connection=yes;')"
        # )
        # parseamos para que lo pueda leer bien sqlalchemy
        urlserver = urllib.parse.quote_plus(server)
        # creamos el motor de sqlengine dandole el parametro de urlserver
        engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(urlserver))
        # creamos la coneccion en una variable
        try:
            print(Panel.fit("Conectando con la base..."))
            conn = engine.connect()
            print(Panel.fit("[green]Login OK!"))
            conn.close()
            ret = {"engine": engine}
            time.sleep(1)
            return ret
        except Exception as e:
            print(
                Panel.fit(
                    f"[red]Hubo un error en sus credenciales/la base, intente de nuevo.\n{str(e)}"
                )
            )
