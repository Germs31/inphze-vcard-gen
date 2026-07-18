from pathlib import Path

import qrcode
from PIL import Image

from contact_data import CONTACT
from vcard import build_vcard


OUTPUT_DIR = Path("output")
PNG_PATH = OUTPUT_DIR / "contact-qr.png"
LOGO_PATH = Path("assets/logo.png")
LOGO_SIZE_RATIO = .30


def generate_png_qr(data: str, file_path: Path) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    if LOGO_PATH.exists():
        logo = Image.open(LOGO_PATH).convert("RGBA")

        logo_size = int(image.size[0] * LOGO_SIZE_RATIO)
        logo.thumbnail((logo_size, logo_size))

        logo_position = (
            (image.size[0] - logo.size[0]) // 2,
            (image.size[1] - logo.size[1]) // 2,
        )

        image.alpha_composite(logo, logo_position)

    image.save(file_path)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    vcard = build_vcard(CONTACT)
    generate_png_qr(vcard, PNG_PATH)

    print("QR code generated successfully.")
    print(f"PNG: {PNG_PATH}")


if __name__ == "__main__":
    main()