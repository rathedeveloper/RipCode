storeName = "Wizard and Witches"
yearEst = 1493
magicNumber = 333.2
girl_list = ["Sarah", "Jill","Kara","Shelly"]
place_tup = ('a','b','c')
truth = False;
jobs = {'Doctor','Lawyer','Software Developer'}
quote = "My name is Inigo Montoya "

'''''''''
user_input = input("Enter your age: ")
age = int(user_input)
print(f"Your Age is : {age} ")

cash_input = input("How much cash do you need?")
cash = float(cash_input)
print(f"You are requesting : {cash}")

x = 5
y = 2 * x + 10

k = 10
#Logical Operator
k+= 5
print(k)
print(x> 0 and y < 10)
print(x < 0 or y < 10)
print(not (x < 0))

 #Triple quotes allow multi-line string
#String Method
print(len(storeName))
print(storeName.lower())
print(storeName.upper())
print(storeName.split())

#Slicing
print(quote[0:5])
print(quote[:10])
print(quote[11:])
print(quote[::3])
print(quote[-5])

#String Indexing
first_string = storeName[0]
print(first_string)
last_string = storeName[-1]
print(last_string)

#string concatenation and Repetition
str1 = "Hey"
str2 = "Yall"
combined = str1 + str2
repeater_str = str1 * 4

print(combined)
print(repeater_str)
'''''''''
#List
# what does mutable mean?
# the object state can be altered after it's creation... ie you can change the values
giftFromGods = ["bacon","pickle ball","beer","jeep"]
print(giftFromGods)
# Indexing / Slcing
#Appending 
giftFromGods.append("whisky")
print(giftFromGods)


# Inserting
giftFromGods.insert(1, "soccer")
print(giftFromGods)
# Removing 
del giftFromGods[2]
print(giftFromGods)
giftFromGods.remove("beer")
print(giftFromGods)
# Length
print(len(giftFromGods))

# Sorting

print(giftFromGods.sort())
print(sorted(giftFromGods))

#Nested list
score = [
    [86, 39, 96],
    [77, 88, 92],
    [34, 41, 79]
]
print(score[2])