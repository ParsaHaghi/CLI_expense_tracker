def main():
    print("Welcome to the Expense Tracker!")
    expenses = {'Food': 0, 'Transportation': 0, 'Entertainment': 0, 'Other': 0}
    
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category_choice = input("select a category (1. Food, 2. Transportation, 3. Entertainment, 4. Other):")
            if category_choice == '1':
                category = "Food"
            elif category_choice == '2':
                category = "Transportation"
            elif category_choice == '3':
                category = "Entertainment"
            elif category_choice == '4':
                category = "Other"
            else:
                print("Invalid category choice. Defaulting to 'Other'.")
                category = "Other"
            expenses[category] += amount
            print(f"Added ${amount:.2f} to {category} expenses.")
        
        elif choice == '2':
            print(expenses.items() )
        
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()


mydict = {'apple' : 3, 'banana' : 5, 'orange' : 2}
new_apple_price = 4
mydict['apple'] = new_apple_price
print(mydict)