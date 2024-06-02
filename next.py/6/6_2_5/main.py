from file1 import GreetingCard
from file2 import BirthdayCard


if __name__ == "__main__":
    birthday_card = BirthdayCard(recipient="Lihay", sender="David", sender_age=19)
    greeting_card = GreetingCard(recipient="Mekarer", sender="Naknik")

    birthday_card.greeting_msg()
    greeting_card.greeting_msg()