"""
Definitions of rich formatting styles to be used across nrobo framework
for rich formatted console outputs.

@author: Panchdev Chauhan
@email: erpanchdev@gmail.com
"""
from rich.theme import Theme


class STYLE:
    """Types of styles"""

    TASK = "task"
    STEP = "step"
    HLOrange = "highlight_text_style_orange"
    HLRed = "highlight_text_style_red"
    HLGreen = "highlight_text_style_green"
    WARNING = "warning",
    INFO = "info",
    DANGER = "danger"
    PURPLE4 = "purple4"


themes = Theme({  # Defined rich themes
    STYLE.TASK: "bold blue",
    STYLE.STEP: "italic green",
    STYLE.HLOrange: "italic dark_orange3",
    STYLE.HLRed: "italic red",
    STYLE.HLGreen: "italic green",
    STYLE.INFO: "dim cyan",
    STYLE.WARNING: "magenta",
    STYLE.DANGER: "bold red",
})
