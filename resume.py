from datetime import date
from data import personal_stuff, work_entries

from pylatex import Document, NoEscape

from latex_tools import include_matrix, place_colored_block, place_text_block, place_colored_block

BOXES_FRAMES = False #good for debugging
ADD_FUN = False #good for fun, bad for jobs

ALBA='alba'
DECOMART='decomart'
BAUHAUS93='bauhaus'
FUTURA='futura'

FONT_FAMILIES = {
    ALBA: 'ALBA____.TTF',
    DECOMART: 'Decomart4F.ttf',
    BAUHAUS93: 'bauhaus.ttf',
    FUTURA: 'FuturaStdBook.ttf',
}

BLACK = (0, 0, 0)
WHITE = (1, 1, 1)
PRIMARY_RED = (0.8, 0.0, 0.0)
PRIMARY_BLUE = (0.0, 0.2, 0.8)
PRIMARY_YELLOW = (1.0, 0.87, 0.2)
PRIMARY_GREY = (0.66, 0.66, 0.66)
PRIMARY_GREEN = (0.0, 0.8, 0.0)
PRIMARY_CYAN = (0.0, 0.8, 0.8)
BEIGE = (0.96, 0.96, 0.86)
BROWN = (0.6, 0.4, 0.08)

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


    place_text_block(doc, address, (133,10), ('0.5cm', '6cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')
    place_text_block(doc, phone, (133,13), ('0.5cm', '6cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')
    

    last_employer = None
    x = 18
    place_text_block(doc, "Work Experience", (0, x), ('0.5cm', '5cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='16')
    x += 5
    for entry in work_entries:
        if entry['name'] != last_employer:
            x += 5
            place_colored_block(doc, (0,x), ('0.25cm', '12cm'), PRIMARY_BLUE)
            place_text_block(doc, entry['name'], (5, x), ('0.5cm', '12cm'), font_family=DECOMART, color=PRIMARY_GREY, font_size='16')
            x += 6
            place_text_block(doc, entry['location'], (10, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_GREY, font_size='10')
            last_employer = entry['name']
            x += 4

        place_text_block(doc, entry['position'], (10, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')
        place_text_block(doc, f"{entry['start_date'].strftime('%b, %Y')} -", (80, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')
        if entry['end_date'] == date.max:
            place_text_block(doc, 'Present', (105, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')
        else:
            place_text_block(doc, entry['end_date'].strftime('%b, %Y'), (100, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_RED, font_size='10')

        x += 5

        for entry, line_guess in entry['bullets']:
            place_text_block(doc, entry, (15, x), ('0.5cm', '10cm'), font_family=FUTURA, color=PRIMARY_GREY, font_size='10')
            x += 5 * line_guess

    # Generate PDF
    doc.generate_pdf(filename.replace('.pdf', ''), clean_tex=False, compiler='lualatex')
    print(f"PDF generated: {filename}")

# Generate the grid PDF
generate_grid_with_coordinates(grid_size=(10, 10), cell_size=(1, 1))
