import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def create_file():
    """Create CSV file with header if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    """Add a new expense."""
    category = input("Enter Category: ").strip()
    description = input("Enter Description: ").strip()

    while True:
        try:
            amount = float(input("Enter Amount (₹): "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")

    date = datetime.now().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("\n✅ Expense Added Successfully!\n")


def view_expenses():
    """Display all expenses."""
    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("\nNo Expenses Found.\n")
        return

    print("\n================ EXPENSE LIST ================")
    print(f"{'No':<5}{'Date':<15}{'Category':<15}{'Description':<20}{'Amount'}")
    print("-" * 70)

    for i, row in enumerate(reader[1:], start=1):
        print(f"{i:<5}{row[0]:<15}{row[1]:<15}{row[2]:<20}₹{row[3]}")

    print()


def total_expense():
    """Calculate total expense."""
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\n💰 Total Expense: ₹{total:.2f}\n")


def delete_expense():
    """Delete an expense."""
    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("\nNo Expenses Found.\n")
        return

    view_expenses()

    try:
        choice = int(input("Enter Expense Number to Delete: "))

        if 1 <= choice <= len(reader) - 1:
            deleted = reader.pop(choice)

            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(reader)

            print(f"\n✅ Deleted: {deleted[2]}\n")
        else:
            print("Invalid Expense Number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    create_file()

    while True:
        print("========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            print("\n👋 Thank You for Using Expense Tracker!")
            break

        else:
            print("\n❌ Invalid Choice. Try Again.\n")


if __name__ == "__main__":
    main()