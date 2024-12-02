from datetime import date
from typing import TypedDict, Optional

class PersonalStuff(TypedDict):
    first_name: str
    middle_name: Optional[str]
    last_name: str
    address: str
    email: str

class WorkEntry(TypedDict):
    name: str
    position: str
    start_date: date
    end_date: date
    bullets: list[str]
    tools: list[str]
    location: str
