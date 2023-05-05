"""
hw_21.md
"""
import json
import pathlib
from typing import TypedDict


class ContactAsDict(TypedDict):
    name: str
    age: int | None
    phones: list[str]


def parse_file_for_contacts(path_to_file: pathlib.Path) -> list[ContactAsDict]:
    contacts = []
    with open(path_to_file) as file:
        for line in file:
            normalized_line = line.strip()

            # handle empty lines
            if not normalized_line:
                continue

            # [parse]-[BEGIN]
            name_raw, age_raw, phones_raw = normalized_line.split(";")
            name = name_raw.strip()
            try:
                age = int(age_raw.strip())
            except ValueError:
                age = None

            phones = []
            for phone in phones_raw.split(","):
                if phone := phone.strip():
                    phones.append(phone)

            contact = ContactAsDict(name=name, age=age, phones=phones)
            # [parse]-[END]

            contacts.append(contact)

    return contacts


def write_contacts_as_json(
    contacts: list[ContactAsDict], path_to_file: pathlib.Path
) -> None:
    with open(path_to_file, "w") as file:
        json.dump(contacts, file, indent=2)
    print(f"Contacts were written to {path_to_file.as_uri()}")


def write_contacts_as_txt(
    contacts: list[ContactAsDict], path_to_file: pathlib.Path
) -> None:
    with open(path_to_file, "w") as file:
        for contact in contacts:
            name = contact["name"]
            age = contact["age"] if contact["age"] is not None else ""
            phones = ",".join(contact["phones"]) if contact["phones"] else ""

            file.write(f"{name};{age};{phones}\n")

    print(f"Contacts were written to {path_to_file.as_uri()}")


def main() -> None:
    path_to_folder = pathlib.Path(__file__).parent
    path_to_input_files = path_to_folder / "hw_21_examples"
    path_to_input_file = path_to_input_files / "users.txt"
    path_to_output_files = path_to_folder / "hw_21_results"
    path_to_output_txt = path_to_output_files / "users_out.txt"
    path_to_output_json = path_to_output_files / "users_out.json"

    contacts = parse_file_for_contacts(path_to_file=path_to_input_file)
    write_contacts_as_json(contacts=contacts, path_to_file=path_to_output_json)
    write_contacts_as_txt(contacts=contacts, path_to_file=path_to_output_txt)


if __name__ == "__main__":
    main()
