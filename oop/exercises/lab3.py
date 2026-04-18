class UserService:
    def __init__(self, username:str):
        self.__username = username

    def create_user(self, name:str):
        if len(name) < 3:
            print("please put in a longer name")
        self.__username = name

    def get_users(self):
        return self.__username

    def delete_user(self):
        del self.__username
        print("was successfully deleted")

user1 = UserService("Lizzy")

print(user1.create_user("Ta"))
print(user1.get_users())
user1.delete_user()