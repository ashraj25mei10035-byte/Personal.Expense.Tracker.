"""
File Management for Expense Data
"""
import json
import os

class FileManager:
    def __init__(self, filename="expense_data.json"):
        self.filename = filename
    
    def save_data(self, expense_manager):
        """Save expense data to JSON file"""
        try:
            data = {
                'expenses': expense_manager.expenses,
                'monthly_budget': expense_manager.monthly_budget
            }
            
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return False
    
    def load_data(self, expense_manager):
        """Load expense data from JSON file"""
        try:
            if not os.path.exists(self.filename):
                return False
            
            with open(self.filename, 'r') as file:
                data = json.load(file)
            
            expense_manager.expenses = data['expenses']
            expense_manager.monthly_budget = data['monthly_budget']
            return True
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False