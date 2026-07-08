from rich.console import Console

from src.core.config import APP_NAME
from src.services.cv_analyzer import CVAnalyzer
from src.services.cv_service import CVService

console = Console()

console.rule(f"[bold blue]{APP_NAME}[/bold blue]")

texto = CVService.read_cv("assets/cv/cv.pdf")

console.print("[yellow]Analizando hoja de vida...[/yellow]\n")

resultado = CVAnalyzer.analyze(texto)

console.print(resultado)