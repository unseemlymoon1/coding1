# Show a simple message.
print("I like climbing mountains.")
# Show a simple message.
print("I like climbing mountains.")
# Clear the screen.
os.system('clear')
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
# Display a title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
# Display a title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
# Display a bunch of output, representing a long-running program.
for x in range(0,51):
 print("\nWe have done %d fun and interesting things together!" % x)
# Import the sleep function.
from time import sleep
print("I'm going to sleep now.")
# Sleep for 3 seconds.
sleep(3)
print("I woke up!")
from time import sleep
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
# Display a title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']
# Print each name 5 times.
for name in names:
# Pause for 1 second between batches, and then skip two lines.
  sleep(1)
print("\n\n")
for x in range(0,5):
 (name.title())
from time import sleep
import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
# Display a title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']
# Print each name 5 times.
for name in names:
# Clear the screen before listing names.
 os.system('clear')
# Display the title bar.
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
print("\n\n")
for x in range(0,5):
  print(name.title())
# Pause for 1 second between batches.
sleep(1)
from time import sleep
import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.
def display_title_bar():
# Clears the terminal screen, and displays a title bar.
 os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")

# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']
# Print each name 5 times.
for name in names:
 display_title_bar()
print("\n\n")
for x in range(0,5):
 print(name.title())
# Pause for 1 second between batches.
sleep(1)
from time import sleep
import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

### FUNCTIONS ###
def display_title_bar():
# Clears the terminal screen, and displays a title bar.
 os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")

### MAIN PROGRAM ###
# Print a bunch of information, in short intervals
names = ['aaron', 'brenda', 'cyrene', 'david', 'eric']
# Print each name 5 times.
for name in names:
 display_title_bar()
print("\n\n")
for x in range(0,5):
 print(name.title())
# Pause for 1 second between batches.
sleep(1)
import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

### FUNCTIONS ###
def display_title_bar():
# Clears the terminal screen, and displays a title bar.
  os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")

### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
choice = ''
while choice != 'q':
 display_title_bar()
# Let users know what they can do.
print("\n[1] See a list of friends.")
print("[2] Tell me about someone new.")
print("[q] Quit.")
choice = input("What would you like to do? ")
# Respond to the user's choice.
if choice == '1':
 print("\nHere are the people I know.\n")
elif choice == '2':
 print("\nI can't wait to meet this person!\n")
elif choice == 'q':
 print("\nThanks for playing. Bye.")
else:
 print("\nI didn't understand that choice.\n")
import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

### FUNCTIONS ###
def display_title_bar():
# Clears the terminal screen, and displays a title bar.
 os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")

### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
choice = ''
display_title_bar()
while choice != 'q':
# Let users know what they can do.
 print("\n[1] See a list of friends.")
print("[2] Tell me about someone new.")
print("[q] Quit.")
choice = input("What would you like to do? ")
# Respond to the user's choice.
display_title_bar()
if choice == '1':
 print("\nHere are the people I know.\n")
elif choice == '2':
 print("\nI can't wait to meet this person!\n")
elif choice == 'q':
 print("\nThanks for playing. Bye.")
else:
 print("\nI didn't understand that choice.\n")
import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

### FUNCTIONS ###
def display_title_bar():
# Clears the terminal screen, and displays a title bar.
 os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
def get_user_choice():
# Let users know what they can do.
 print("\n[1] See a list of friends.")
print("[2] Tell me about someone new.")
print("[q] Quit.")
 return input("What would you like to do? ")

### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
 choice = ''
 display_title_bar()
 while choice != 'q':
 choice = get_user_choice()
# Respond to the user's choice.
 display_title_bar()
 if choice == '1':
  print("\nHere are the people I know.\n")
 elif choice == '2':
  print("\nI can't wait to meet this person!\n")
 elif choice == 'q':
  print("\nThanks for playing. Bye.")
 else:
 print("\nI didn't understand that choice.\n")
 import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

### FUNCTIONS ###
 def display_title_bar():
# Clears the terminal screen, and displays a title bar.
os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
def get_user_choice():
# Let users know what they can do.
 print("\n[1] See a list of friends.")
print("[2] Tell me about someone new.")
print("[q] Quit.")
return input("What would you like to do? ")

### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
names = []
choice = ''
display_title_bar()
while choice != 'q':
 choice = get_user_choice()
# Respond to the user's choice.
display_title_bar()
if choice == '1':
 print("\nHere are the people I know.\n")
for name in names:
 print(name.title())
 Elif choice == '2':
new_name = input("\nPlease tell me this person's name: ")
names.append(new_name)
print("\nI'm so happy to know %s!\n" % new_name.title())
 Elif choice == 'q':
 print("\nThanks for playing. Bye.")
 Else:
 print("\nI didn't understand that choice.\n")
 import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

### FUNCTIONS ###
 def display_title_bar():
# Clears the terminal screen, and displays a title bar.os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
def get_user_choice():
# Let users know what they can do.
print("\n[1] See a list of friends.")
print("[2] Tell me about someone new.")
print("[q] Quit.")
return input("What would you like to do? ")
def show_names():
# Shows the names of everyone who is already in the list.
print("\nHere are the people I know.\n")
for name in names:
print(name.title())
def get_new_name():
# Asks the user for a new name, and stores the name.
new_name = input("\nPlease tell me this person's name: ")
names.append(new_name)
print("\nI'm so happy to know %s!\n" % new_name.title())
### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
names = []
choice = ''
display_title_bar()
while choice != 'q':
choice = get_user_choice()
# Respond to the user's choice.
display_title_bar()
if choice == '1':
show_names()
elif choice == '2':
get_new_name()
elif choice == 'q':
print("\nThanks for playing. Bye.")
else:
print("\nI didn't understand that choice.\n")
import os
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

### FUNCTIONS ###
def display_title_bar():
# Clears the terminal screen, and displays a title bar.
os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
def get_user_choice():
# Let users know what they can do.
print("\n[1] See a list of friends.")
print("[2] Tell me about someone new.")
print("[q] Quit.")
return input("What would you like to do? ")
def show_names():
# Shows the names of everyone who is already in the list.
print("\nHere are the people I know.\n")
for name in names:
print(name.title())
def get_new_name():
# Asks the user for a new name, and stores the name if we don't already
# know about this person.
new_name = input("\nPlease tell me this person's name: ")
if new_name in names:
    print("\n%s is an old friend! Thank you, though." % new_name.title())
else:
names.append(new_name)
print("\nI'm so happy to know %s!\n" % new_name.title())
### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
names = []
choice = ''
display_title_bar()
while choice != 'q':
choice = get_user_choice()
# Respond to the user's choice.
display_title_bar()
if choice == '1':
show_names()
elif choice == '2':
get_new_name()
elif choice == 'q':
print("\nThanks for playing. Bye.")
else:
print("\nI didn't understand that choice.\n")
import pickle
# This program asks the user for some animals, and stores them.
# Make an empty list to store new animals in.
animals = []
# Create a loop that lets users store new animals.
new_animal = ''
while new_animal != 'quit':
print("\nPlease tell me a new animal to remember.")
new_animal = input("Enter 'quit' to quit: ")
if new_animal != 'quit':
animals.append(new_animal)
# Try to save the animals to the file 'animals.pydata'.
try:
file_object = open('animals.pydata', 'wb')
pickle.dump(animals, file_object)
file_object.close()
print("\nI will remember the following animals: ")
for animal in animals:
print(animal)
except Exception as e:
print(e)
print("\nI couldn't figure out how to store the animals. Sorry.")
import pickle
# This program asks the user for some animals, and stores them.
# It loads animals if they exist.
# Try to load animals. If they don't exist, make an empty list
# to store new animals in.
try:
file_object = open('animals.pydata', 'rb')
animals = pickle.load(file_object)
file_object.close()
except:
animals = []
# Show the animals that are stored so far.
if len(animals) > 0:
print("I know the following animals: ")
for animal in animals:
print(animal)
else:
print("I don't know any animals yet.")
# Create a loop that lets users store new animals.
new_animal = ''
while new_animal != 'quit':
print("\nPlease tell me a new animal to remember.")
new_animal = input("Enter 'quit' to quit: ")
if new_animal != 'quit':
animals.append(new_animal)
# Try to save the animals to the file 'animals.pydata'.
try:
file_object = open('animals.pydata', 'wb')
pickle.dump(animals, file_object)
file_object.close()
print("\nI will remember the following animals: ")
for animal in animals:
print(animal)
except Exception as e:
print(e)
print("\nI couldn't figure out how to store the animals. Sorry.")
import os
import pickle
# Greeter is a terminal application that greets old friends warmly,
# and remembers new friends.

### FUNCTIONS ###
def display_title_bar():
# Clears the terminal screen, and displays a title bar.
os.system('clear')
print("\t**********************************************")
print("\t*** Greeter - Hello old and new friends! ***")
print("\t**********************************************")
def get_user_choice():
# Let users know what they can do.
print("\n[1] See a list of friends.")
print("[2] Tell me about someone new.")
print("[q] Quit.")
return input("What would you like to do? ")
def show_names():
# Shows the names of everyone who is already in the list.
print("\nHere are the people I know.\n")
for name in names:
print(name.title())
def get_new_name():
# Asks the user for a new name, and stores the name if we don't already
# know about this person.
new_name = input("\nPlease tell me this person's name: ")
if new_name in names:
print("\n%s is an old friend! Thank you, though." % new_name.title())
else:
names.append(new_name)
print("\nI'm so happy to know %s!\n" % new_name.title())
def load_names():
# This function loads names from a file, and puts them in the list 'names'.
# If the file doesn't exist, it creates an empty list.
try:
file_object = open('names.pydata', 'rb')
names = pickle.load(file_object)
file_object.close()
return names
except Exception as e:
print(e)
return []
def quit():
# This function dumps the names into a file, and prints a quit message.
try:
file_object = open('names.pydata', 'wb')
pickle.dump(names, file_object)
file_object.close()
print("\nThanks for playing. I will remember these good friends.")
except Exception as e:
print("\nThanks for playing. I won't be able to remember these names.")
print(e)
### MAIN PROGRAM ###
# Set up a loop where users can choose what they'd like to do.
names = load_names()
choice = ''
display_title_bar()
while choice != 'q':
choice = get_user_choice()
# Respond to the user's choice.
display_title_bar()
if choice == '1':
show_names()
elif choice == '2':
get_new_name()
elif choice == 'q':
quit()
print("\nThanks for playing. Bye.")
else:
print("\nI didn't understand that choice.\n")