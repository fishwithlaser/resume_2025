from datetime import date
from data import personal_stuff, work_entries, skill_categories

from pylatex import Document, NoEscape

from latex_tools import include_matrix, place_colored_block, place_text_block, place_colored_block
from work_history import place_skills, place_work_history

BOXES_FRAMES = False #good for debugging
ADD_FUN = False #good for fun, bad for jobs

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



def generate_grid_with_coordinates(filename="grid_with_coordinates.pdf", grid_size=(10, 10), cell_size=(1, 1)):
    """
    Generates a PDF with a grid and coordinate labels using pylatex.

    :param filename: Output PDF file name
    :param grid_size: Tuple (rows, cols) for the grid dimensions
    :param cell_size: Tuple (width, height) for the size of each grid cell
    """

    # Create a LaTeX document with 0.5-inch margins
    doc = Document()
    doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
    # doc.preamble.append(NoEscape(r'\usepackage{svg}'))
    doc.preamble.append(NoEscape(r'\usepackage[margin=0.5in]{geometry}'))
    doc.preamble.append(NoEscape(r'\usepackage{xcolor}'))
    doc.preamble.append(NoEscape(r'\usepackage{tikz}'))
    doc.preamble.append(NoEscape(r'\usepackage{sectsty}'))
    doc.preamble.append(NoEscape(r"\usepackage[absolute,overlay]{textpos}"))

    doc.preamble.append(NoEscape(r"\usepackage{fontspec}"))
    for font_name, font_file in FONT_FAMILIES.items():
        font_str = '\\newfontfamily\\' + font_name + "[Path=fonts/" + font_name +"/]{" + font_file+'}'
        doc.preamble.append(NoEscape(font_str))
    if not BOXES_FRAMES:
        doc.append(NoEscape(r'\setlength{\fboxrule}{0pt}'))

    x_min = 0
    y_min = 0

    # include_matrix(doc)

    #refactor for header
    name_string = personal_stuff['first_name'].title() + ' ' +\
        personal_stuff['middle_name'].title() + ' ' +\
        personal_stuff['last_name'].title()
    
    address = f"A: {personal_stuff['address']}"
    phone = f"E: {personal_stuff['email']}"

    if ADD_FUN:
        place_colored_block(doc, (20,2.5), ('2cm', '2cm'), PRIMARY_BLUE)
        place_colored_block(doc, (17,2.5), ('2cm', '2cm'), PRIMARY_YELLOW)
        place_colored_block(doc, (13,2.5), ('2cm', '2cm'), PRIMARY_GREEN)
        place_colored_block(doc, (8,2.5), ('2cm', '2cm'), PRIMARY_CYAN)
        place_colored_block(doc, (2,2.5), ('2cm', '2cm'), BEIGE)

    #NAME BLOCK
    place_colored_block(doc, (-2,3), ('0.5cm', '12cm'), PRIMARY_GREY)
    place_colored_block(doc, (0,5), ('0.5cm', '12cm'), BLACK)
    place_text_block(doc, name_string, (7,4), ('0.5cm', '13cm'), font_family=DECOMART, color=WHITE, font_size='24')

    place_colored_block(doc, (129,3), ('0.5cm', '8cm'), PRIMARY_YELLOW)
    place_colored_block(doc, (127,5), ('0.5cm', '8cm'), PRIMARY_BLUE)
    place_text_block(doc, address, (133,5.5), ('0.5cm', '6cm'), font_family=FUTURA, color=WHITE, font_size='10')
    place_text_block(doc, phone, (133,8.5), ('0.5cm', '6cm'), font_family=FUTURA, color=WHITE, font_size='10')
    
    
    x = 18
    y = 125
    place_work_history(doc, work_entries, x)
    place_skills(doc, skill_categories, x, y)

    # Generate PDF
    doc.generate_pdf(filename.replace('.pdf', ''), clean_tex=False, compiler='lualatex')
    print(f"PDF generated: {filename}")

# Generate the grid PDF
generate_grid_with_coordinates(grid_size=(10, 10), cell_size=(1, 1))
