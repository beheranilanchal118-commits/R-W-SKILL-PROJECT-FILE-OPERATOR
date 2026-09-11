import datetime


class JournalManager:

    def __init__(self):

        self.pin = 1234

        try:
            with open("journal.txt", "x") as file:
                pass

        except FileExistsError:
            pass

        except PermissionError:
            print("Error: Permission denied while creating file.")

    def add_entry(self, entry):

        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        try:

            user_pin = int(input("Enter Your PIN: "))

            if user_pin != self.pin:
                raise PermissionError("Invalid PIN.")

            with open("journal.txt", "a") as file:

                file.write(f"{timestamp}\n")
                file.write(f"{entry}\n")
                file.write("-" * 40 + "\n")

            print("Entry added successfully.")

        except ValueError:
            print("Error: PIN must be numeric.")

        except PermissionError as e:
            print(f"Error: {e}")

        except FileNotFoundError:
            print("Error: Journal file not found.")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    def view_all_entries(self):

        try:

            with open("journal.txt", "r") as file:
                entries = file.read()

            if entries:
                print("\n========== ALL JOURNAL ENTRIES ==========")
                print(entries)

            else:
                print("No journal entries found.")

        except FileNotFoundError:
            print("Error: Journal file does not exist.")

        except PermissionError:
            print("Error: Permission denied while reading file.")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    def search_entry(self):

        word = input("Enter keyword or date to search: ").lower()

        try:

            with open("journal.txt", "r") as file:

                found = False

                for line in file:

                    if word in line.lower():
                        print(line.strip())
                        found = True

                if not found:
                    print("No matching entry found.")

        except FileNotFoundError:
            print("Error: Journal file does not exist.")

        except PermissionError:
            print("Error: Permission denied while reading file.")

        except Exception as e:
            print(f"Unexpected Error: {e}")

    def delete_all_entries(self):

        try:

            user_pin = int(input("Enter Your PIN: "))

            if user_pin != self.pin:
                raise PermissionError("Invalid PIN.")

            confirm = input(
                "Are you sure you want to delete ALL entries? (yes/no): "
            )

            if confirm.lower() != "yes":
                print("Deletion cancelled.")
                return

            import os

            if os.path.exists("journal.txt"):

                os.remove("journal.txt")

                print("All journal entries deleted successfully.")

            else:
                print("Error: Journal file does not exist.")

        except ValueError:
            print("Error: PIN must be numeric.")

        except PermissionError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected Error: {e}")


journal = JournalManager()


while True:

    print("\n======================================================")
    print("         WELCOME TO JOURNAL MANAGEMENT SYSTEM")
    print("======================================================")

    print("1. Add Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    print("======================================================")

    choice = input("Enter Your Choice: ")

    try:

        if choice == "1":

            entry = input("Enter Your Journal Entry: ")

            if not entry.strip():
                print("Error: Entry cannot be empty.")

            else:
                journal.add_entry(entry)
                input("\nPress Enter To Continue...")

        elif choice == "2":

            print("======================================================")

            journal.view_all_entries()

            print("======================================================")

            input("\nPress Enter To Continue...")

        elif choice == "3":

            print("======================================================")

            journal.search_entry()

            print("======================================================")

            input("\nPress Enter To Continue...")

        elif choice == "4":

            print("======================================================")

            journal.delete_all_entries()

            print("======================================================")

            input("\nPress Enter To Continue...")

        elif choice == "5":

            print("\n")
            print("======================================================")
            print("Thank You For Using Journal App.")
            print("======================================================")

            break

        else:

            print("Invalid choice. Please select 1 to 5.")

    except Exception as e:

        print(f"Unexpected Error: {e}")