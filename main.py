def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return f"Error: {str(e)}"
    return wrapper

contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}"

@input_error
def change_phone(name, new_phone):
    contacts[name] = new_phone
    return f"Phone number for {name} updated to {new_phone}"

@input_error
def get_phone(name):
    return f"Phone number for {name}: {contacts[name]}"

@input_error
def show_all():
    if not contacts:
        return "No contacts available."
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    while True:
        command = input("Enter command: ").lower()

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split()
            print(add_contact(name, phone))
        elif command.startswith("change"):
            _, name, new_phone = command.split()
            print(change_phone(name, new_phone))
        elif command.startswith("phone"):
            _, name = command.split()
            print(get_phone(name))
        elif command == "show all":
            print(show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()