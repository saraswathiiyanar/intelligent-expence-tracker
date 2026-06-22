class RecommendationEngine:

    @staticmethod
    def generate_advice(total_expense):

        if total_expense == 0:
            return "Start tracking your expenses regularly."

        elif total_expense > 10000:
            return "Your spending is high. Consider reducing unnecessary expenses and increase your savings."

        elif total_expense > 5000:
            return "You are spending moderately. Maintain a proper monthly budget."

        else:
            return "Excellent! Your expenses are under control. Keep saving regularly."

    @staticmethod
    def savings_tip():
        return "Try to save at least 20% of your monthly income."

    @staticmethod
    def budget_tip():
        return "Set a monthly budget and monitor your spending weekly."

    @staticmethod
    def emergency_fund_tip():
        return "Maintain an emergency fund covering at least 3 to 6 months of expenses."