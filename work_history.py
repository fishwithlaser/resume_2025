
from datetime import date
from typing import List
from data import personal_stuff, work_entries

from pylatex import Document, NoEscape

from data_types import SkillCategory, WorkEntry
from latex_tools import place_colored_block, place_text_block, place_colored_block

from fonts_and_colors import (
    BLACK, 
    WHITE, 
    PRIMARY_RED, 
    PRIMARY_BLUE, 
    PRIMARY_YELLOW, 
    PRIMARY_GREY, 
    PRIMARY_GREEN, 
    PRIMARY_CYAN, 
    BEIGE, 
    BROWN,
    ALBA,
    DECOMART,
    BAUHAUS93,
    FUTURA,
    FONT_FAMILIES
)

def place_work_history(doc: Document, work_entries: List[WorkEntry], x:int):
    last_employer = None

    place_text_block(doc, "Work Experience", (0, x), ('0.5cm', '5cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='16')
    x += 5
    for entry in work_entries:
        if entry['name'] != last_employer:
            x += 5
            place_colored_block(doc, (0,x), ('0.25cm', '12cm'), PRIMARY_YELLOW)
            place_text_block(doc, entry['name'], (2.5, x), ('0.5cm', '12cm'), font_family=DECOMART, color=PRIMARY_BLUE, font_size='16')
            x += 6
            place_text_block(doc, entry['location'], (2.5, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_GREY, font_size='10')
            last_employer = entry['name']
            x += 4

        place_text_block(doc, entry['position'], (2.5, x), ('0.5cm', '11cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')
        place_text_block(doc, f"{entry['start_date'].strftime('%b, %Y')} -", (85, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')
        if entry['end_date'] == date.max:
            place_text_block(doc, 'Present', (105, x), ('0.5cm', '11cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')
        else:
            place_text_block(doc, entry['end_date'].strftime('%b, %Y'), (105, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')

        x += 5

        for entry, line_guess in entry['bullets']:
            place_text_block(doc, entry, (5, x), ('0.5cm', '11.5cm'), font_family=FUTURA, color=PRIMARY_GREY, font_size='10')
            x += 5 * line_guess

def place_skills(doc: Document, skill_categories: List[SkillCategory], x:int, y:int):
    place_text_block(doc, "Skills", (y, x), ('0.5cm', '5cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='16')
    x += 5

    for category in skill_categories:
        place_colored_block(doc, (y, x), ('0.25cm', '12cm'), PRIMARY_YELLOW)
        place_text_block(doc, category['category'], (y+2.5, x), ('0.5cm', '12cm'), font_family=DECOMART, color=PRIMARY_BLUE, font_size='16')
        x += 6

        for subcategory in category['skills']:
            place_text_block(doc, subcategory['subcategory'], (y+2.5, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_GREY, font_size='12')
            x += 4

            for item in subcategory['items']:
                place_text_block(doc, f"- {item}", (y+5, x), ('0.5cm', '11.5cm'), font_family=FUTURA, color=PRIMARY_GREY, font_size='10')
                x += 5