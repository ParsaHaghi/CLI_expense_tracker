import datetime
import requests


def get_auto_date():
    try:
        # 1. Try Internet (Modern/Simple API)
        # We set a short timeout (e.g., 2 seconds) so the app doesn't hang if offline.
        response = requests.get("http://worldtimeapi.org/api/ip", timeout=2)
        response.raise_for_status()
        
        # Parse the data
        data = response.json()
        # The API returns ISO format (2023-10-27T...), slice it to get just YYYY-MM-DD
        date_str = data['datetime'][:10]
        
        # Convert - to / to match your preferred format
        return date_str.replace('-', '/')
        
    except (requests.RequestException, ValueError):
        # 2. Fallback to Windows OS Date
        # datetime.now() automatically pulls from the local Windows system clock
        now = datetime.datetime.now()
        return now.strftime("%Y/%m/%d")

def manual_date_entry(date=''):
    while True:
        if date == '1':
            return get_auto_date()
        elif date == '2':
            return None

        try:
            datetime1 = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y/%m/%d")
            return datetime1
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.\n"
                  "For auto date press 1 and for canceling, press 2")
            date = input("Enter the date (YYYY-MM-DD): ")


def main():
    print("Welcome to the Expense Tracker!")
    expenses = []
    
    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category_choice = input("write the category: ")
            category = category_choice.capitalize()
            date = input("press 1 for today or Enter the date (YYYY-MM-DD): ")
            if date == '1':
                date = get_auto_date()
                print(date)
            else:
                date = manual_date_entry(date)
                if date is None:
                    print("Expense entry cancelled.")
                    break
            expenses.append({'amount': amount, 'category': category, 'date': date})
            print(f"Expense added: ${amount:.2f} for {category} on {date}")
            print(expenses)
        
        elif choice == '2':
            if not expenses:
                print("No expenses recorded.")
            else:
                print("\nExpenses:")
                for idx, expense in enumerate(expenses, start=1):
                    print(f"{idx}. ${expense['amount']:.2f} for {expense['category']} on {expense['date']}")
        
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()
