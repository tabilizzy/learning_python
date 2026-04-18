class User:
    def __init__(self, username: str):
        self.username = username

    def login(self):
        return f"Welcome to you {self.username}, thank you for loging in "
    
    def logout(self):
        return f"Goodbye {self.username}, you have logout "

user1 = User("lizzy")
print(user1.login())
print(user1.logout())