from PIL import Image, ImageDraw, ImageFont
from random import randint


QR_X_OFFSET = 94
QR_Y_OFFSET = 603
RESIZE_RATIO = 2.89
TIME_FONT_SIZE = 45
TIME_FONT_COLOR = (216, 208, 206)
TIME_FONT_OFFSET = (916, 11)
CODE_FONT_SIZE = 130
CODE_FONT_COLOR = (60, 60, 60)


def add_qr(qr):
    base = Image.open('base.png')
    qr = Image.open(qr)

    qr_w, qr_h = qr.size
    qr_resized = qr.resize((int(qr_w * RESIZE_RATIO), int(qr_h * RESIZE_RATIO),))
    qr_w, qr_h = qr_resized.size
    area = (QR_X_OFFSET, QR_Y_OFFSET, QR_X_OFFSET + qr_w, QR_Y_OFFSET + qr_h)
    base.paste(qr_resized, area)

    return base


def set_time(img):
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('fonts/SamsungSans-Medium.ttf', TIME_FONT_SIZE)

    hour = randint(10, 23)
    minutes = randint(0, 59)
    minutes = '{0:02d}'.format(minutes)

    draw.text(TIME_FONT_OFFSET, "{}:{}".format(hour, minutes), font=font, fill=TIME_FONT_COLOR)
    return img


def set_code(base, code):
    code_w, code_h = code.size
    base_w, base_h = base.size

    x_offset = int((base_w - code_w) / 2)
    offset = (x_offset, 1486)
    base.paste(code, offset)
    return base


def create_code(code):
    font = ImageFont.truetype('fonts/Berthold-regular.ttf', CODE_FONT_SIZE)
    width, height = font.getsize(code)
    img = Image.new('RGBA', (width, height), (255, 255, 255,))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), code, font=font, fill=CODE_FONT_COLOR)
    return img


def generate_screenshot(code, bytes_image):
    code = code.upper()
    code_image = create_code(code)
    image = add_qr(bytes_image)
    image = set_time(image)
    image = set_code(image, code_image)

    image.save("{}.png".format(code), "PNG")


