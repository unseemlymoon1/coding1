
# I learned how to strip whitespace from strings.
name = '\t\teric'
#  i store this message and when i say print message it will print hwatever i have stored  
message = " i am jaden stanly "
print(message)
#when i store name and then press print name upper it will print name in upper case 
first_name = 'jaden '
print(first_name.upper())
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dog = dogs[0]
dog = dogs[0]
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dog = dogs[1]
print(dog.title())
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dog = dogs[-1]
print(dog.title())
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dog = dogs[-2]
print(dog.title())
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dog = dogs[-4]
print(dog.title())
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
for dog in dogs :
 print(dog)
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
for dog in dogs:
    print('I like ' + dog + 's.')
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
for dog in dogs:
 print('I like ' + dog + 's.')
 print('No, I really really like ' + dog +'s!\n')
 print("\nThat's just how I feel about dogs.")
 dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
 print("Results for the dog show are as follows:\n")
 for index, dog in enumerate(dogs):
     place = str(index)
print("Place: " + place + " Dog: " + dog.title())
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
for dog in dogs:
   print(dogs)
dogs = ['border collie', 'australian cattle dog', 'labrador retriever'] for dog in dogs:
 for dog in dogs:
    print('I like ' + dogs + 's.')
    dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
    dogs[0] = 'australian shepherd'
    print(dogs)
    dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
    print(dogs.index('australian cattle dog'))
    dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
print(dogs.index('poodle'))
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
print('australian cattle dog' in dogs)
print('poodle' in dogs)
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.append('poodle')
for dog in dogs:
   print(dog.title() + "s are cool.")
   dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
   dogs.insert(1, 'poodle')
   print(dogs)
usernames = []

# Add some users.
usernames.append('bernice')
usernames.append('cody')
usernames.append('aaron')

# Greet all of our users.
for username in usernames:
    print("Welcome, " + username.title() + '!')
    usernames = []

# Add some users.
usernames.append('bernice')
usernames.append('cody')
usernames.append('aaron')

# Greet all of our users.
for username in usernames:
    print("Welcome, " + username.title() + '!')

# Recognize our first user, and welcome our newest user.
print("\nThank you for being our very first user, " + usernames[0].title() + '!')
print("And a warm welcome to our newest user, " + usernames[-1].title() + '!')
students = ['bernice', 'aaron', 'cody']

# Put students in alphabetical order.
students.sort()

# Display the list in its current order.
print("Our students are currently in alphabetical order.")
for student in students:
    print(student.title())

#Put students in reverse alphabetical order.
students.sort(reverse=True)

# Display the list in its current order.
print("\nOur students are now in reverse alphabetical order.")
for student in students:
    print(student.title())
    students = ['bernice', 'aaron', 'cody']

# Display students in alphabetical order, but keep the original order.
print("Here is the list in alphabetical order:")
for student in sorted(students):
    print(student.title())

# Display students in reverse alphabetical order, but keep the original order.
print("\nHere is the list in reverse alphabetical order:")
for student in sorted(students, reverse=True):
    print(student.title())

print("\nHere is the list in its original order:")
# Show that the list is still in its original order.
for student in students:
    print(student.title())
    students = ['bernice', 'aaron', 'cody']
students.reverse()

print(students)
numbers = [1, 3, 4, 2]

# sort() puts numbers in increasing order.
numbers.sort()
print(numbers)

# sort(reverse=True) puts numbers in decreasing order.
numbers.sort(reverse=True)
print(numbers)
numbers = [1, 3, 4, 2]

# sorted() preserves the original order of the list:
print(sorted(numbers))
print(numbers)
numbers = [1, 3, 4, 2]

# The reverse() function also works for numerical lists.
numbers.reverse()
print(numbers)
usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print(user_count)
usernames = []

# Add some users, and report on how many users we have.
usernames.append('bernice')
user_count = len(usernames)

print("We have " + str(user_count) + " user!")

usernames.append('cody')
usernames.append('aaron')
user_count = len(usernames)

print("We have " + str(user_count) + " users!")
usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print("This will cause an error: " + user_count)
usernames = ['bernice', 'cody', 'aaron']
user_count = len(usernames)

print("This will work: " + str(user_count))
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove the first dog from the list.
del dogs[0]

print(dogs)
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove australian cattle dog from the list.
dogs.remove('australian cattle dog')

print(dogs)
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove australian cattle dog from the list.
dogs.remove('australian cattle dog')

print(dogs)
letters = ['a', 'b', 'c', 'a', 'b', 'c']
# Remove the letter a from the list.
letters.remove('a')

print(letters)
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
last_dog = dogs.pop()

print(last_dog)
print(dogs)
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
first_dog = dogs.pop(0)

print(first_dog)
print(dogs)
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Grab the first three users in the list.
first_batch = usernames[0:3]

for user in first_batch:
    print(user.title())
    usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Grab the first three users in the list.
first_batch = usernames[:3]

for user in first_batch:
    print(user.title())
    usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Grab the first three users in the list.
first_batch = usernames[0:3]

# The original list is unaffected.
for user in usernames:
    print(user.title())
    usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Grab a batch from the middle of the list.
middle_batch = usernames[1:4]

for user in middle_batch:
    print(user.title())
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Grab a batch from the middle of the list.
middle_batch = usernames[1:4]

for user in middle_batch:
    print(user.title())
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Grab all users from the third to the end.
end_batch = usernames[2:]

for user in end_batch:
    print(user.title())
usernames = ['bernice', 'cody', 'aaron', 'ever', 'dalia']

# Make a copy of the list.
copied_usernames = usernames[:]
print("The full copied list:\n\t", copied_usernames)

# Remove the first two users from the copied list.
del copied_usernames[0]
del copied_usernames[0]
print("\nTwo users removed from copied list:\n\t", copied_usernames)

# The original list is unaffected.
print("\nThe original list:\n\t", usernames)
# Print out the first ten numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)
# Print the first ten numbers.
for number in range(1,11):
    print(number)
    # Print the first ten odd numbers.
for number in range(1,21,2):
    print(number)
    # Create a list of the first ten numbers.
numbers = list(range(1,11))
print(numbers)
# Store the first million numbers in a list.
numbers = list(range(1,1000001))

# Show the length of the list:
print("The list 'numbers' has " + str(len(numbers)) + " numbers in it.")

# Show the last ten numbers:
print("\nThe last ten numbers in the list are:")
for number in numbers[-10:]:
    print(number)
ages = [23, 16, 14, 28, 19, 11, 38]

youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

print("Our youngest reader is " + str(youngest) + " years old.")
print("Our oldest reader is " + str(oldest) + " years old.")
print("Together, we have " + str(total_years) + " years worth of life experience.")
# Store the first ten square numbers in a list.
# Make an empty list that will hold our square numbers.
squares = []

# Go through the first ten numbers, square them, and add them to our list.
for number in range(1,11):
    new_square = number**2
    squares.append(new_square)
    
# Show that our list is correct.
for square in squares:
    print(square)
    # Store the first ten square numbers in a list.
# Make an empty list that will hold our square numbers.
squares = []

# Go through the first ten numbers, square them, and add them to our list.
for number in range(1,11):
    squares.append(number**2)
    
# Show that our list is correct.
for square in squares:
    print(square)
    # Store the first ten square numbers in a list.
squares = [number**2 for number in range(1,11)]

# Show that our list is correct.
for square in squares:
    print(square)
    # Make an empty list that will hold the even numbers.
evens = []

# Loop through the numbers 1-10, double each one, and add it to our list.
for number in range(1,11):
    evens.append(number*2)
    
# Show that our list is correct:
for even in evens:
    print(even)
# Make a list of the first ten even numbers.
evens = [number*2 for number in range(1,11)]

for even in evens:
    print(even)
    # Consider some students.
students = ['bernice', 'aaron', 'cody']

# Let's turn them into great students.
great_students = []
for student in students:
    great_students.append(student.title() + " the great!")

# Let's greet each great student.
for great_student in great_students:
    print("Hello, " + great_student)


   
