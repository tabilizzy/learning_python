class User:
    role = "Trainee"
    def __init__(self, user_id: int, username: str, email: str, password: str, is_active: bool = True):
        #Instance attributes (unique to each object)
        self._user_id = user_id  #protected
        self.username = username  #public
        self.__email = email     #private
        self.is_active = is_active    #public
        self.__password = password
        #self.created_at = datetime.utcnow() # can run code too

    def to_dict(self):
        return self.__dict__

# this is an instance method
    def greet(self):
        return f"hello, {self.username}"

    def get_password_hash(self):
        return self.__password
    
    #@property
    def get_email(self):
        return self.__email

    def set_password(self, value: str):
        if len(value) > 8:
            raise ValueError("password is too long")
        self.__password  = value

    def set_email(self, value: str):
        if "@" in value:
            self.__email = value
        print("wrong email")

    def __str__(self):
        return self.username
    


#Creating objects
user1 = User(1, "alice",  "alice@example.com" , "1234")
user2 = User(2, "bob", "bob@example.com", "4567", is_active = False)

print(user1)

print(user1.to_dict())


print(user1.greet())
print(user1.get_email())
print(user1.get_password_hash())

print(user1.set_email("tabilizzygmail.com"))
print(user1.set_password("thjqwdwqdhqwdiswqsnxashuduwqdqjasakjnqidwbwaqd"))
