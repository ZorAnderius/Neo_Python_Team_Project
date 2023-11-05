from colorama import Fore
from pathlib import Path
import os.path
from rich.console import Console

from address_book_classes.AddressBook import AddressBook
from notes_classes.NoteBook import NoteBook
from user_interface.command_functions import *
from user_interface.parse_input import parse_input

book_path = Path("address_book.json")
notebook_path = Path("note_book.json")


def main():
    book = AddressBook()
    notebook = NoteBook()
    console = Console()
    if os.path.exists(book_path):
        new_book = book.read_from_file(book_path)
        if new_book and type(new_book) is dict:
            book = book.add_book(new_book)
    if os.path.exists(notebook_path ):
        new_notebook = notebook.read_from_file(notebook_path )
        if new_notebook and type(new_notebook) is dict:
            notebook = notebook.add_book(new_notebook)
    while True:
        user_input = input(Fore.CYAN + "Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print(Fore.BLUE + "Good bye!")
                break
            elif command == "hello":
                print(Fore.BLUE + "How can I help you?")
            elif command == "add-contact":
                print(added_contact(args, book))
            elif command == "change-contact":
                print(change_contact(args, book))
            elif command == "add-email":
                print(add_email(args, book))
            elif command == "change-email":
                print(change_email(args, book))
            elif command == "add-address":
                print(add_address(args, book))
            elif command == "change-address":
                print(change_address(args, book))
            elif command == "phone":
                print(find_phone(args, book)[:-1:])
            elif command == "all-contacts":
                console.print(show_all(book))
            elif command == 'delete-record':
                print (delete_record(args, book))
            elif command == "search-by-name":
                result = search_by_name(args, book)
                if result is not None:
                    console.print(result)
            elif command == "search-by-phone":
                result = search_by_phone(args, book)
                if result is not None:
                    console.print(result)
            elif command == "search-by-email":
                result = search_by_email(args, book)
                if result is not None:
                    console.print(result)
            elif command == "remove-phone":
                remove_phone(args, book)
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(show_all_birthdays(args, book))
            elif command == "add-note":
                print(add_note(args, notebook))
            elif command == "add-tag":
                print(add_tag(args, notebook))
            elif command == "change-title":
                print(change_note_title(args, notebook))
            elif command == "change-body":
                print(change_note_body(args, notebook))
            elif command == "change-tag":
                print(change_note_tag(args, notebook))
            elif command == "remove-note":
                print(remove_note(args, notebook))
            elif command == "remove-body":
                print(remove_note_body(args, notebook))
            elif command == "remove-tag":
                print(remove_note_tag(args, notebook))
            elif command == "all-notes":
                print(show_all(notebook))
            else:
                print(Fore.YELLOW + "Invalid command")

    book.save_to_file(book_path)
    notebook.save_to_file(notebook_path)


if __name__ == "__main__":
    main()
