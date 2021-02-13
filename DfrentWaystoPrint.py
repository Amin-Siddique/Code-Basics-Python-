#Here's how to print formatted output using a variable!
name = "ok"

#method1:
print("Happy Birthday " + name)

#method2:
print("Happy Birthday {}".format(name))

#method3: Best method!
print(f"Happy Birthday {name}")


################################################## USAGE ###############################################

adj = input("How are you feeling today in one word: ")

bot = f"I am feeling {adj}!"

print(bot)
