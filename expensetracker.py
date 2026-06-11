expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category (Food/Travel/Shopping/etc): ")
        amount = float(input("Enter amount: "))
        expenses.append({"category": category, "amount": amount})
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for expense in expenses:
                print(f"{expense['category']} - ₹{expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal Expense: ₹{total}")

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice! Please try again.")