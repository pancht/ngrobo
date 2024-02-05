from rich.theme import Theme


class STYLE:
    TASK = "task"
    STEP = "step"
    HLOrange = "highlight_text_style_orange"
    HLRed = "highlight_text_style_red"
    HLGreen = "highlight_text_style_green"
    WARNING = "warning",
    INFO = "info",
    DANGER = "danger"


themes = Theme({
    # doc: https://rich.readthedocs.io/en/latest/style.html#style-themes
    STYLE.TASK: "bold blue",
    STYLE.STEP: "italic green",
    STYLE.HLOrange: "italic dark_orange3",
    STYLE.HLRed: "italic red",
    STYLE.HLGreen: "italic green",
    STYLE.INFO: "dim cyan",
    STYLE.WARNING: "magenta",
    STYLE.DANGER: "bold red"
})
