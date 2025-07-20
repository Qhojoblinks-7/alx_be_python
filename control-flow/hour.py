# a simple Python if-elif-else statement that, given an hour (an integer from 0 to 23), prints

hour = int(input())

if hour >= 5 and hour <= 11:
    print("Good morning!")
elif hour >= 12 and hour <= 17:
    print("Good afternoon")
elif hour >= 18 and hour <= 22:
    print("Good evening")
else:
    print("Good night")