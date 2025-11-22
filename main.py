"""
Personal Expense Tracker - Main File
"""
from menu import MainMenu

def main():
    print("💰 Personal Expense Tracker")
    print("============================")
    
    menu = MainMenu()
    menu.display_main_menu()

if __name__ == "__main__":
    main()