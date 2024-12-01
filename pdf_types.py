from typing import TypedDict, NotRequired

class FontOptions(TypedDict):
    bold: NotRequired[bool]
    size: NotRequired[int]  # Font size in points
