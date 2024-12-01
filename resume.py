from pylatex import Document, TikZ, TikZDraw, NoEscape

from latex_tools import include_matrix

def generate_grid_with_coordinates(filename="grid_with_coordinates.pdf", grid_size=(10, 10), cell_size=(1, 1)):
    """
    Generates a PDF with a grid and coordinate labels using pylatex.

    :param filename: Output PDF file name
    :param grid_size: Tuple (rows, cols) for the grid dimensions
    :param cell_size: Tuple (width, height) for the size of each grid cell
    """
    rows, cols = grid_size
    cell_width, cell_height = cell_size

    # Create a LaTeX document with 0.5-inch margins
    doc = Document()
    doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
    # doc.preamble.append(NoEscape(r'\usepackage{svg}'))
    doc.preamble.append(NoEscape(r'\usepackage[margin=0.5in]{geometry}'))
    doc.preamble.append(NoEscape(r'\usepackage{textpos}'))
    doc.preamble.append(NoEscape(r'\usepackage{xcolor}'))
    doc.preamble.append(NoEscape(r'\usepackage{tikz}'))
    doc.preamble.append(NoEscape(r'\usepackage{sectsty}'))

    include_matrix(doc)

    # Generate PDF
    doc.generate_pdf(filename.replace('.pdf', ''), clean_tex=False)
    print(f"PDF generated: {filename}")

# Generate the grid PDF
generate_grid_with_coordinates(grid_size=(10, 10), cell_size=(1, 1))
