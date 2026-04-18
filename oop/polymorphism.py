
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

class EmailNotifier:
    def send(self, message: str):
        print(f"Email: {message}")

class SmsNotifier:
    def send(self, message: str):
        print(f"SMS: {message}")

def notify(notifer, message: str):
    notifer.send(message)


notify(EmailNotifier(), "Welcome!")
notify(SmsNotifier(), "Welcome!")

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
