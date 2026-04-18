#in composition we have the has a relationship
#that is a user has a profile
# if the user is delected then the profile will no longer exist 
# composition is most perfered to inheritance
class Profile:
    def __init__(self, bio):
        self.bio = bio

class User:
    def __init__(self, profile):
        self.profile = profile

user1 = User("lizzy")
print(user1.profile)