from contact_data import CONTACT

def escape_vcard_value(value: str)-> str:
    return (
        value.replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace(";", "\\;")
        .replace(",", "\\,")
    )

def build_vcard(contact: dict[str, str]) -> str:
    lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{escape_vcard_value(contact['last_name'])};{escape_vcard_value(contact['first_name'])};;;",
        f"FN:{escape_vcard_value(contact['full_name'])}",
        f"ORG:{escape_vcard_value(contact['company'])}",
        f"TITLE:{escape_vcard_value(contact['title'])}",
        f"TEL;TYPE=CELL:{escape_vcard_value(contact['phone'])}",
        f"EMAIL;TYPE=INTERNET,WORK:{escape_vcard_value(contact['email'])}",
        f"URL:{escape_vcard_value(contact['website'])}",
        f"ADR;TYPE=WORK:;;;{escape_vcard_value(contact['city'])};{escape_vcard_value(contact['state'])};;;",
        f"NOTE:{escape_vcard_value(contact['note'])}",
        "END:VCARD",
    ]
    return "\n".join(lines)

if __name__ == "__main__":
    vcard = build_vcard(CONTACT)
    print(vcard)
    print()
    print("Starts correctly:", vcard.startswith("BEGIN:VCARD"))
    print("Ends correctly:", vcard.endswith("END:VCARD"))