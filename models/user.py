class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def get_user_details(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }