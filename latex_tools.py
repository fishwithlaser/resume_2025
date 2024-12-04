from pylatex import Document, NoEscape

from pdf_types import FontOptions


def apply_font(str_: any, **kwargs: FontOptions) -> str:
    str_ = str_.__str__()
    if "size" in kwargs:
        size_cmd = f"\\fontsize{{{kwargs['size']}}}{{{kwargs['size']}}}\\selectfont "
    else:
        size_cmd = "\\tiny "
    bold_cmd = r"\textbf{" + str_ + r"}" if kwargs.get("bold") else str_

    return NoEscape(size_cmd + bold_cmd)


def text_block(
    doc,
    content,
    x,
    y,
    w=r"\textwidth",
    h=None,
    font_size=None,
    color=None,
    font_family=None,
):
    """
    Places a styled text block in the document.

    Args:
        doc: The document object (e.g., from pylatex).
        content: The text content inside the block.
        x: The x-coordinate (in mm) for positioning the block.
        y: The y-coordinate (in mm) for positioning the block.
        w: The width of the block (default is \textwidth).
        h: The height of the block (optional, not used here).
        font_size: The size of the text (e.g., "12", "14").
        color: The text color (default is "black").
        font_family: The font family command (e.g., "alba", "decomart").
    """
    doc.append(NoEscape(r"\begin{textblock*}{" + w + r"}" + rf"({x}mm, {y}mm)"))

    if color:
        # Expecting color as a tuple (r, g, b), where 0 <= r, g, b <= 1
        color_rgb = f"{{{color[0]},{color[1]},{color[2]}}}"
        doc.append(NoEscape(r"\textcolor[rgb]" + color_rgb + r"{"))
    else:
        doc.append(NoEscape(r"\textcolor{black}{"))
    
    # Add text size if specified (using \fontsize for pt sizes)
    if font_size:
        # Example of using \fontsize{size}{baselineskip} for point sizes
        doc.append(NoEscape(f"\\fontsize{{{font_size}pt}}{{12pt}}\\selectfont "))

    # Apply font family if specified
    if font_family:
        doc.append(NoEscape(rf"\{font_family}" + " " + content))
    else:
        doc.append(content)

    doc.append(NoEscape(r"}"))
    doc.append(NoEscape(r"\end{textblock*}"))



def place_colored_block(doc, xy, hw, color):
    """
    Places a colored frame box at specified coordinates in the document.

    Args:
        doc: The document object (e.g., from pylatex).
        xy: Tuple (x, y) for absolute positioning on the page (in cm).
        hw: Tuple (height, width) for the box size (e.g., "2cm", "5cm").
        color: The background color (e.g., "red", "blue", "yellow").
    """
    # Ensure the `textpos` package is included
    doc.preamble.append(NoEscape(r"\usepackage[absolute,overlay]{textpos}"))
    # doc.preamble.append(NoEscape(r"\setlength{\TPHorizModule}{1cm}"))
    # doc.preamble.append(NoEscape(r"\setlength{\TPVertModule}{1cm}"))

    color_code = f"{{{color[0]},{color[1]},{color[2]}}}"

    framebox_code = NoEscape(
    r"\begin{textblock*}{"  # Start textblock definition
    + hw[1]  # Width of the box
    + r"}("
    + str(xy[0]/10)  # X-coordinate remains unchanged
    + r"cm,"
    + str(xy[1]/10)  # Y-coordinate now corresponds to the top-left corner
    + r"cm)"
    + r"\colorbox[rgb]"
    + color_code  # Color of the framebox
    + r"{\framebox["  # Start framebox
    + hw[1]  # Specify width
    + r"][t]{"
    + r"\rule{0pt}{"  # Rule to define height
    + hw[0]  # Specify height
    + r"}}}"
    + r"\end{textblock*}")  # End textblock definition
    doc.append(framebox_code)



def place_text_block(doc, content, xy, hw, font_family=None, color=None, font_size=12):
    text_content = NoEscape(r"\framebox[" +
                            hw[1] +
                            r"]{" +
                            r"\parbox[t][" +
                            hw[0] +
                            r"][t]{" +
                            str(hw[1]) +
                            r"}{" +
                            content +
                            r"}}")
    text_block(doc, text_content, xy[0], xy[1], font_family=font_family, color=color, font_size=font_size)


def include_matrix(doc) -> None:
    for i in range(-5, 20):
        i_1 = i * 10
        for j in range(-5, 40):
            j_1 = j * 10
            text_block(doc, f"{(i_1, j_1)}", i_1, j_1, font_size=6, color=(0.9, 0.9, 0.9))


def include_image(
    path: str,
    title: str,
    x="5cm",
) -> str:
    doc = Document()
    if title:
        doc.append(NoEscape(title))
    doc.append(NoEscape(r"\begin{figure}[h!]"))
    doc.append(NoEscape(r"\centering"))
    doc.append(
        NoEscape(rf"\includegraphics[width={x}]{{{path}}}")
    )  # Ensure braces around the path
    doc.append(NoEscape(r"\end{figure}"))
    return doc.dumps_content()
