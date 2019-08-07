from peewee import *
import random
import time

db = SqliteDatabase('names.db')


class PastName(Model):
    PastName = CharField(max_length=255, unique=True)

    class Meta:
        database = db


if __name__  ==  '__main__':
    db.connect()
    db.create_tables([PastName], safe=True)

def sleep():
    time.sleep(1)

def load():
    for i in range(3):
        print("Loading...")
        time.sleep(.500)


first_names = [
    "Anogia", "Artorius", "Boreal", "Brutus", "Captain",
    "Conquerus", "DeathBringer", "Donatello", "Defeater",
    "Doom", "Ezqueal", "Eazy-E", "Ernie"
]


last_names = [
    "Ailbright", "Angelic", "Barfqueeze", "Crook", "Cracking",
    "Killman", "Doomsday", "Fartmen", "Toxicity"
]


print("""\n\n
Welcome to Name-O-Tron 5700.  Today we're going to predict your name
if you were born in a post-apocalyptic world.
""")

first_name = input("Enter your first name only:\n")
last_name = input("Enter your last name only:\n")

load()
sleep()

print("""
Your name has been entered into our machine, 
and is being analyzed for a suitable dystopian name.
""")

new_first_name = random.choice(first_names)
new_last_name = random.choice(last_names)
new_name = new_first_name + " " + new_last_name

sleep()
load()
sleep()

print(f"In a destroyed world, your name would be {new_name}")
