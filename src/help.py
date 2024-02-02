from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

def help():
    line1 = "Commands: \n"
    line2 = "\n"
    line3 = "clear\n"
    line4 = "pwd\n"
    line5 = "cd\n"
    line6 = "makeqr\n"
    line7 = "rick\n"

    main_panel = Panel(line1 + line2 + line3 + line4 + line5 + line6 + line7)
    console.print(main_panel)
