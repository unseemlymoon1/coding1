# A list of desserts I like.
desserts = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
favorite_dessert = 'apple crisp'
# Print the desserts out, but let everyone know my favorite dessert.
for dessert in desserts:
if dessert == favorite_dessert:
# This dessert is my favorite, let's let everyone know!
print("%s is my favorite dessert!" % dessert.title())
else:
# I like these desserts, but they are not my favorite.
print("I like %s." % dessert)
5 == 5

3 == 5

5 == 5.0

'eric' == 'eric'

'Eric' == 'eric'

'Eric'.lower() == 'eric'.lower()
'5' == 5

'5' == str(5)
3 != 5

5 != 5

'Eric' != 'eric'
5 > 3
5 >= 3

3 >= 3
3 < 5
3 <= 5

3 <= 3
vowels = ['a', 'e', 'i', 'o', 'u']
'a' in vowels

vowels = ['a', 'e', 'i', 'o', 'u']
'b' in vowels
dogs = ['willie', 'hootz', 'peso', 'juno']
if len(dogs) > 3:
print("Wow, we have a lot of dogs here!")
dogs = ['willie', 'hootz']
if len(dogs) > 3:
print("Wow, we have a lot of dogs here!")
dogs = ['willie', 'hootz', 'peso', 'juno']
if len(dogs) > 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = ['willie', 'hootz']
if len(dogs) > 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = ['willie', 'hootz', 'peso', 'monty']
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = ['willie', 'hootz']
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = ['willie', 'hootz', 'peso', 'monty']
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = ['willie', 'hootz']
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = []
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")ws
dogs = ['willie', 'hootz']
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = []
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
else:
print("Okay, this is a reasonable number of dogs.")
dogs = []
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
elif len(dogs) >= 1:
print("Okay, this is a reasonable number of dogs.")
dogs = []
if len(dogs) >= 5:
print("Holy mackerel, we might as well start a dog hostel!")
elif len(dogs) >= 3:
print("Wow, we have a lot of dogs here!")
elif len(dogs) >= 1:
print("Okay, this is a reasonable number of dogs.")
else:
print("I wish we had a dog here.")
dogs = ['willie', 'hootz']
if 'willie' in dogs:
print("Hello, Willie!")
if 'hootz' in dogs:
print("Hello, Hootz!")
if 'peso' in dogs:
print("Hello, Peso!")
if 'monty' in dogs:
print("Hello, Monty!")
dogs = ['willie', 'hootz']
if 'willie' in dogs:
print("Hello, Willie!")
elif 'hootz' in dogs:
print("Hello, Hootz!")
elif 'peso' in dogs:
print("Hello, Peso!")
elif 'monty' in dogs:
print("Hello, Monty!")
dogs_we_know = ['willie', 'hootz', 'peso', 'monty', 'juno', 'turkey']
dogs_present = ['willie', 'hootz']
# Go through all the dogs that are present, and greet the dogs we know.
for dog in dogs_present:
if dog in dogs_we_know:
print("Hello, %s!" % dog.title())
if 0:
print("This evaluates to True.")
else:
print("This evaluates to False.")

if 1:
print("This evaluates to True.")
else:
print("This evaluates to False.")

# Arbitrary non-zero numbers evaluate to True.
if 1253756:
print("This evaluates to True.")
else:
print("This evaluates to False.")
# Negative numbers are not zero, so they evaluate to True.
if -1:
print("This evaluates to True.")
else:
print("This evaluates to False.")

# An empty string evaluates to False.
if '':
print("This evaluates to True.")
else:
print("This evaluates to False.")

# Any other string, including a space, evaluates to True.
if ' ':
print("This evaluates to True.")
else:
print("This evaluates to False.")

# Any other string, including a space, evaluates to True.
if 'hello':
print("This evaluates to True.")
else:
print("This evaluates to False.")
# None is a special object in Python. It evaluates to False.
if None:
print("This evaluates to True.")
else:
print("This evaluates to False.")