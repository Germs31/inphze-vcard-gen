from pathlib import Path

import qrcode

from contact_data import CONTACT
from vcard import build_vcard


OUTPUT_DIR = Path("output")
PNG_PATH = OUTPUT_DIR / "contact-qr.png"


def generate_png_qr(data: str, file_path: Path) -> None:
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(file_path)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    vcard = build_vcard(CONTACT)
    generate_png_qr(vcard, PNG_PATH)

    print("QR code generated successfully.")
    print(f"PNG: {PNG_PATH}")


if __name__ == "__main__":
    main()