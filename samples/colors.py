class Colors:
    BLUE = "#2980b9"
    RED = "#ce4250"
    ORANGE = "#f59e16"
    GREEN = "#268C52"
    MAGENTA = "#bd93f9"
    PURPLE = "#f676c0"

    DARK_BLUE = "#07086f"
    REGULAR_BLUE = "#0005e3"
    TURQ_BLUE = "#28dfff"
    LIGHT_BLUE = "#2494ea"

    GRAY = "#31363b"
    # BLACK = "#23262a"
    WHITE = "#eff0f1"

    def __iter__(self):
        for attr in [attr for attr in dir(self) if not attr.startswith("__")]:
            yield getattr(self, attr)

    def __reversed__(self):
        for attr in list(self)[-1::]:
            yield attr
