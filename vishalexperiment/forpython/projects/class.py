from modules import emoji

class Person:
    def __init__(self, name, age, x, y) -> None:
        self.name = name
        self.age = age
        self.x = x
        self.y = y

    def talk_method(self):
        print("Method is " + self.name + self.age) 

    def walk(self):
        for i range(10):
        print(f"{self.name} has taken {i}th step")
                print(f"{self.name} has taken {i} steps")
        for i in emu

john = Person("john", "10", x=10, y=100)
john.talk_method()
john.walk()
print("HID")
message = input("Choose between \n :) or ;) or <3 or hello or hi or goodbye or bye: ").lower()
print(emoji.emoji_conventor(message))
print(john.x)
