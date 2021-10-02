import os.path

import markdown


def open_file(filename: str):
    filepath = os.path.join("app/pages/", filename)
    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    html = markdown.markdown(text)
    data = {"text": html}
    return data
