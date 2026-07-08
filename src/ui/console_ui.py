from rich.console import Console

console = Console()


def user_input():
    return console.input("\n[bold cyan]Tú:[/bold cyan] ")


def bot_output(message):
    console.print(f"\n[bold green]CareerPilotAI:[/bold green]\n{message}")