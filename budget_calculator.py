"""
Budget Calculation Utilities
"""

class BudgetCalculator:
    def __init__(self):
        self.categories = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]
    
    def calculate_category_totals(self, expenses):
        """Calculate total spending per category"""
        category_totals = {category: 0 for category in self.categories}
        
        for expense in expenses:
            category = expense['category']
            if category in category_totals:
                category_totals[category] += expense['amount']
            else:
                category_totals['Other'] += expense['amount']
        
        return category_totals
    
    def get_budget_status(self, total_spent, monthly_budget):
        """Get budget status message"""
        if monthly_budget == 0:
            return "No budget set"
        
        percentage = (total_spent / monthly_budget) * 100
        
        if percentage >= 100:
            return "Over budget"
        elif percentage >= 80:
            return "Approaching budget limit"
        elif percentage >= 50:
            return "Moderate spending"
        else:
            return "Within budget"