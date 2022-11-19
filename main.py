import pytesseract as pytesseract
from PIL import Image
from fastapi import FastAPI

# Samarth

app = FastAPI()


@app.route("/")
def hello():
    return {"value": get_text()}


def get_text():
    pytesseract.pytesseract.tesseract_cmd = './.apt/usr/share/tesseract-ocr/4.00/tessdata'
    image = Image.open('./sam.png', mode='r')
    raw = str(pytesseract.image_to_string(image))
    raw.strip()
    equals_pos = raw.rfind('=')
    raw = raw[0:equals_pos].strip()
    final = -1
    if raw.__contains__('-'):
        pos = raw.rfind('-')
        first = int(raw[0:pos])
        if raw[pos + 1: raw.__sizeof__()].__eq__("O0"):
            second = 0
        else:
            second = int(raw[pos + 1: raw.__sizeof__()])
        final = first - second

    elif raw.__contains__('+'):
        pos = raw.rfind('+')
        first = int(raw[0:pos])
        if raw[pos + 1: raw.__sizeof__()].__eq__("O0"):
            second = 0
        else:
            second = int(raw[pos + 1: raw.__sizeof__()])
        final = first + second

    elif raw.__contains__('*'):
        pos = raw.rfind('*')
        first = int(raw[0:pos])
        second = int(raw[pos + 1: raw.__sizeof__()])
        final = first * second

    return final
