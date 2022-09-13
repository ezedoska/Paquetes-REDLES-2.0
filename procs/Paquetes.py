from procs.procs_db import exec_proc, make_paq, upl_paq
from rich.console import Console
from rich.prompt import Confirm, Prompt
import glob

console = Console()


def send(engine, form) -> int:
    console.rule(f"[bold red]{form['titulo']}")
    if Confirm.ask(f"Correr {form['form']}?"):
        try:
            exec_proc(engine, form["exec"])
            console.rule()
        except Exception:
            console.print_exception(show_locals=True)
            Prompt.ask("Presione [bold red]ENTER[/bold red] para continuar")
            return 0
    if Confirm.ask(f"Crear archivos {form['form']}?"):
        try:
            console.log("Creando carpetas y archivos")
            make_paq(engine, form)
            console.rule()
        except Exception:
            console.print_exception(show_locals=True)
            Prompt.ask("Presione [bold red]ENTER[/bold red] para continuar")
            return 0
    Prompt.ask("Presione [bold red]ENTER[/bold red] para continuar")
    return 0


def recv(engine, form) -> int:
    console.rule(f"[bold red]{form['titulo']}")
    console.log("Buscando paquetes...")
    pqt = glob.glob(f"*{form['pqt']}*")
    if len(pqt) == 0:
        console.log("No se encontro el archivo a subir.")
        Prompt.ask("Presione [bold red]ENTER[/bold red] para continuar")
        return 0
    if Confirm.ask(f"Subir archivo/s\n{pqt}?\n"):
        try:
            upl_paq(engine, form, pqt)
        except Exception:
            console.print_exception(show_locals=True)
            Prompt.ask("Presione [bold red]ENTER[/bold red] para continuar")
            return 0
    console.rule()
    if Confirm.ask(f"Correr proceso INSERT {form['form']}?"):
        try:
            for proc in form["exec"]:
                exec_proc(engine, proc)
                console.rule()
        except Exception:
            console.print_exception(show_locals=True)
            Prompt.ask("Presione [bold red]ENTER[/bold red] para continuar")
            return 0
    Prompt.ask("Presione [bold red]ENTER[/bold red] para continuar")
    return 0
