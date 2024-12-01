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
    text_size=None,
    color="black",
    width="5cm",
):
    doc.append(NoEscape(r"\begin{textblock*}{" + w + r"}" + rf"({x}mm, {y}mm)"))
    if text_size:
        doc.append(NoEscape(f"\\{text_size}"))
    doc.append(content)
    doc.append(NoEscape(r"\end{textblock*}"))


def place_text_block(doc, content, xy, hw):
    # seems not to be placed in absolute as table messes this up
    text_content = NoEscape(
        r"\framebox["
        + hw[1]
        + r"]{"
        + r"\parbox[t]["
        + hw[0]
        + r"][t]{"
        + str(hw[1])
        + r"}{"
        + content
        + r"}}"
    )
    text_block(doc, text_content, xy[0], xy[1])


def include_matrix(doc) -> None:
    for i in range(-5, 20):
        i_1 = i * 10
        for j in range(-5, 40):
            j_1 = j * 10
            text_block(doc, f"{(i_1, j_1)}", i_1, j_1, text_size="tiny")


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
