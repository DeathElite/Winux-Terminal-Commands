from rich.console import Console
from rich.text import Text

console = Console()

class errors:
    def command_not_recognised(command):
        text = Text("error: " + command + " is not recognised as a command")
        text.stylize("bold red")
        console.print(text)
