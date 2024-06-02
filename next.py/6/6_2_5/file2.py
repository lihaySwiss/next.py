from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, recipient="Golov", sender="Shmulik", sender_age=0):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print("Happy birthday!")
        print(f"Sender's age: {self._sender_age}")


if __name__ == "__main__":
    card = BirthdayCard(sender_age=30)
    card.greeting_msg()