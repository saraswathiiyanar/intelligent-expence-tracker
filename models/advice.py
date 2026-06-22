class Advice:
    def __init__(self, advice_id, recommendation, generated_date):
        self.advice_id = advice_id
        self.recommendation = recommendation
        self.generated_date = generated_date

    def get_advice_details(self):
        return {
            "advice_id": self.advice_id,
            "recommendation": self.recommendation,
            "generated_date": self.generated_date
        }