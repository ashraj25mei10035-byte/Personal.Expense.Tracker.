"""
Menu System for Expense Tracker
"""
from expense_manager import ExpenseManager
from file_manager import FileManager

class MainMenu:
    def __init__(self):
        self.expense_manager = ExpenseManager()
        self.file_manager = FileManager()
    
    def display_main_menu(self):
        while True:
            print("\n📋 MAIN MENU")
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. View by Category")
            print("4. Set Monthly Budget")
            print("5. View Budget Report")
            print("6. Save Data")
            print("7. Load Data")
            print("8. Exit")
            
            choice = input("Enter your choice (1-8): ")
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_all_expenses()
            elif choice == '3':
                self.view_by_category()
            elif choice == '4':
                self.set_budget()
            elif choice == '5':
                self.view_budget_report()
            elif choice == '6':
                self.save_data()
            elif choice == '7':
                self.load_data()
            elif choice == '8':
                print("👋 Thank you for using Expense Tracker!")
                break
            else:
                print("❌ Invalid choice! Please try again.")
    
    def add_expense(self):
        print("\n💰 ADD NEW EXPENSE")
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (DD/MM/YYYY): ")
        
        self.expense_manager.add_expense(amount, category, description, date)
        print("✅ Expense added successfully!")
    
    def view_all_expenses(self):
        self.expense_manager.view_all_expenses()
    
    def view_by_category(self):
        category = input("Enter category to view: ")
        self.expense_manager.view_by_category(category)
    
    def set_budget(self):
        budget = float(input("Enter monthly budget: ₹"))
        self.expense_manager.set_budget(budget)
        print(f"✅ Monthly budget set to ₹{budget}")
    
    def view_budget_report(self):
        self.expense_manager.view_budget_report()
    
    def save_data(self):
        if self.file_manager.save_data(self.expense_manager):
            print("✅ Data saved successfully!")
        else:
            print("❌ Error saving data!")
    
    def load_data(self):
        if self.file_manager.load_data(self.expense_manager):
            print("✅ Data loaded successfully!")
            self.view_all_expenses()
        else:
            print("❌ No saved data found!")