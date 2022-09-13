import pandas as pd
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from procs.console import console
import procs.discordbot as dbot


def go(engine):
    """
    [Muestra el ultimo numero procesado para cada paquete]

    Arguments:
        engine {[sqlalchemy]} -- [engine creado por sqlalchemy]
    """
    console.rule(f"[bold red]ESTADO PAQUETES")

    paquetes = pd.read_sql_query(
        "SELECT *  FROM [adm_efectores].[dbo].[PaquetesEnviados] order by envio",
        con=engine,
    )
    dbot.log(paquetes, "")
    # print(paquetes.to_string(index=False, justify="center", col_space=10))
    print(paquetes.to_markdown(index=False))

    Prompt.ask("\nPresione [red][ENTER][/red] para volver al menu.")
    return 0
