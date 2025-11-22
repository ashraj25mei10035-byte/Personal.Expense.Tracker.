"""
Expense Management Core Logic
"""

class ExpenseManager:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0
        self.categories = ["Food", "Transport", "Entertainment", "Shopping", "Bills", "Other"]
    
    def add_expense(self, amount, category, description, date):
        """Add a new expense to the tracker"""
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': date
        }
        self.expenses.append(expense)
    
    def view_all_expenses(self):
        """Display all expenses"""
        if not self.expenses:
            print("📭 No expenses recorded yet!")
            return
        
        print(f"\n📊 ALL EXPENSES (Total: {len(self.expenses)})")
        print("=" * 60)
        print(f"{'Date':<12} {'Category':<15} {'Description':<20} {'Amount':<10}")
        print("-" * 60)
        
        total = 0
        for expense in self.expenses:
            print(f"{expense['date']:<12} {expense['category']:<15} {expense['description']:<20} ₹{expense['amount']:<8.2f}")
            total += expense['amount']
        
        print("-" * 60)
        print(f"{'TOTAL':<47} ₹{total:.2f}")
    
    def view_by_category(self, category):
        """Display expenses for a specific category"""
        category_expenses = [e for e in self.expenses if e['category'].lower() == category.lower()]
        
        if not category_expenses:
            print(f"📭 No expenses found for category: {category}")
            return
        
        print(f"\n📊 EXPENSES FOR: {category.upper()}")
        print("=" * 50)
        total = 0
        for expense in category_expenses:
            print(f"{expense['date']} - {expense['description']}: ₹{expense['amount']:.2f}")
            total += expense['amount']
        
        print("-" * 50)
        print(f"Category Total: ₹{total:.2f}")
    
    def set_budget(self, budget):
        """Set monthly budget"""
        self.monthly_budget = budget
    
    def view_budget_report(self):
        """Display budget vs actual spending"""
        if self.monthly_budget == 0:
            print("❌ Please set a monthly budget first!")
            return
        
        total_spent = sum(expense['amount'] for expense in self.expenses)
        remaining = self.monthly_budget - total_spent
        
        print(f"\n💰 BUDGET REPORT")
        print("=" * 30)
        print(f"Monthly Budget:    ₹{self.monthly_budget:.2f}")
        print(f"Total Spent:       ₹{total_spent:.2f}")
        print(f"Remaining:         ₹{remaining:.2f}")
        
        # Budget status
        if remaining < 0:
            print("🚨 OVER BUDGET! Reduce spending.")
        elif remaining < self.monthly_budget * 0.2:
            print("⚠️  Low budget remaining. Be careful!")
        else:
            print("✅ Within budget. Good job!")
    
    def get_category_summary(self):
        """Get spending summary by category"""
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            if category in summary:
                summary[category] += expense['amount']
            else:
                summary[category] = expense['amount']
        return summary
    