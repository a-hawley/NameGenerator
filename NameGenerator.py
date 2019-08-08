# Imports
from peewee import *
import random
from time import sleep
from os import system, name


# Create peewee database
db = SqliteDatabase('names.db')


# Set character length and uniqueness
class PastName(Model):
    Past_Names = CharField(max_length=255)

# Make your database connection
    class Meta:
        database = db


# Make sure you can run multiple times without breaking peewee
if __name__ == '__main__':
    db.connect()
    db.create_tables([PastName], safe=True)


# Purely aesthetic
def load():
    for i in range(3):
        print("Loading...")
        sleep(.500)


# Purely aesthetic
def clear():
    # os.system('cls' if os.name == 'nt' else 'clear') usually works for clearing the screen,
    # but not for PyCharm. Instead it inserts an arrow like symbol.
    print("\n" * 100)


# Create name tables
first_names = [
    "Anogia", "Artorius", "Boreal", "Brutus", "Captain",
    "Conquerus", "DeathBringer", "Donatello", "Defeater",
    "Doom", "Ezqueal", "Eazy-E", "Ernie"
]


last_names = [
    "Ailbright", "Angelic", "Barfqueeze", "Crook", "Cracking",
    "Killman", "Doomsday", "Fartmen", "Toxicity"
]


# Our program
def main():
    print("""\n\n
    Welcome to Name-O-Tron 5700.  Today we're going to predict your name
    if you were born in a post-apocalyptic world.
    """)

    first_name = input("Enter your first name only:\n")
    last_name = input("Enter your last name only:\n")
    whole_name = first_name + " " + last_name
    load()
    clear()
    print(f"""
    Alright {whole_name},
    Your name has been entered into our machine, 
    and is being analyzed for a suitable dystopian name.
    """)

    input("Press enter to continue...\n")

    new_first_name = random.choice(first_names)
    new_last_name = random.choice(last_names)
    new_name = new_first_name + " " + new_last_name

    append_new_name = PastName(Past_Names=new_name)
    append_new_name.save()

    load()
    clear()

    print(f"In a destroyed world, your name would be {new_name}!")
    restart = input("Try again? [y/n]:\n")
    if restart.lower() == "y":
        print("\n" * 100)
        main()

    else:
        print("Here is a list of all the unique names you've been assigned!\n")
        for index, name in enumerate(PastName.select(), 1):
            print(f"{index}. {name.Past_Names}")
        print("\nThanks for playing!")
        exit()


# Start program:
main()



