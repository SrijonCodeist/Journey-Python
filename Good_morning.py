# Greetings according to the time of the day
import datetime

current_time = datetime.datetime.now()
current_hour = current_time.hour

name = input("Enter your Name: ")

if 0 <= current_hour < 12:
    print(f"\nGood morning, {name}!")
elif 12 <= current_hour < 18:
    print(f"\nGood afternoon, {name}!")
else:
    print(f"\nGood evening, {name}!")
