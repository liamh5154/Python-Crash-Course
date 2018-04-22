#	If Statements - 5-3 Alien Colors #1 pg88
"""Create a Variable called alien_color and assign it a value of green, 
yellow or red."""
alien_color = 'green'
if 'green' in alien_color:
	print("5 Points!")
if 'red' in alien_color:
	print("10 Points!")
print("\n")

#	If Statements - 5-4 Alien Colors #2 pg88
"""Choose a color for an alien as you did in Exercise 5-3 and write an
if-else chain."""
alien_color_2 = 'red'
if 'green' in alien_color_2:
	print("5 Points!")
else:
	print("10 Points!")

alien_color_2 = 'green'
if 'green' in alien_color_2:
	print("5 Points!")
else:
	print("10 Points!")
print("\n")

#	If Statements - 5-5 Alien Colors #3 pg89
"""Turn your if-else chain from exercise 5-4 into an if-elif-else chain."""
alien_color_3 = 'yellow'
if 'red' in alien_color_3:
	print("15 Points!")
elif 'green' in alien_color_3:
	print("5 Points!")
else:
	print("10 Points!")
print("\n")

#	If Statements - 5-6 Stages of Life pg89
"""Write an if-elif-else chain that determines a person's stage of life.
Set a value for the variable age..."""
age = 18
if age < 2:
	print("You are a Baby.")
elif age < 4:
	print("You are a Toddler.")
elif age < 13:
	print("You are a Child.")
elif age < 20:
	print("You are a Teenager.")
elif age < 65:
	print("You are an Adult.")
else:
	print("You are an Elder.")
print("\n")

#	If Statements - 5-7 Favorite Fruit pg89
"""Make a list of your favorite fruits and then write a series of inde-
pendent if statements that check for certain fruits in your list."""
favorite_fruits = ['oranges', 'bananas', 'grapes']
if 'pears' in favorite_fruits:
	print("Damn! You love Pears!")
if 'oranges' in favorite_fruits:
	print("You Luuurrvv Oranges!")
if 'apples' in favorite_fruits:
	print("Apples too!?")
if 'grapes' in favorite_fruits:
	print("Grapes, we all love Grapes!")
if 'bananas' in favorite_fruits:
	print("Hide the bananas!")
print("\n")


	






