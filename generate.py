from burger import get_coupon_image, get_coupon_qr
from screenshot import generate_screenshot
from pathlib import Path

CODES = [
    "5bd1c98203df2a0261635822"
]

for c in CODES:
    code = get_coupon_qr(c)

    file = Path("{}.png".format(code))
    if not file.is_file():
        qr = get_coupon_image(c)

        print("[+] Generating screenshot for {}".format(code))
        generate_screenshot(code, qr)
    else:
        print("[] Screenshot already generated for {}".format(code))
