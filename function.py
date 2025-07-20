   
import re

# 1. Remove all non-alphabet characters
s = 'H3ll0_Wor!ld#2025'
result = ''.join([c for c in s if c.isalpha()])
print("Q1:", result)  # Output: HllWorld

b=""
for i in s:
    if i.isalpha():
        b+=i
print(b)
        
    
# ------------------------------------------------------------

# 2. Most frequent word
sentence = 'cat dog dog bird cat cat'
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
most_common = max(freq, key=freq.get)
print("Q2:", most_common)  # Output: cat

for word in words:
    freq[word]=freq.get(word,0)+1

# ------------------------------------------------------------

# 3. Index of first vowel
s = 'crypt'
vowels = 'aeiou'
index = next((i for i, c in enumerate(s) if c in vowels), -1)
print("Q3:", index)  # Output: -1

# ------------------------------------------------------------

# 4. Move vowels to end
s = 'education'
vowels = 'aeiou'
consonants = ''.join([c for c in s if c not in vowels])
vowel_part = ''.join([c for c in s if c in vowels])
print("Q4:", consonants + vowel_part)  # Output: dctneuaio

# ------------------------------------------------------------

# 5. Character frequency dictionary
s = 'banana'
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1
print("Q5:", freq)  # Output: {'b':1, 'a':3, 'n':2}

# ------------------------------------------------------------

# 6. Replace vowels with uppercase
s = 'hello world'
vowels = 'aeiou'
result = ''.join([c.upper() if c in vowels else c for c in s])
print("Q6:", result)  # Output: hEllO wOrld

# ------------------------------------------------------------

# 7. Check continuous ascending digits
s = '12345'
is_continuous = all(int(s[i]) + 1 == int(s[i+1]) for i in range(len(s)-1))
print("Q7:", is_continuous)  # Output: True

# ------------------------------------------------------------

# 8. Count words longer than 4 letters
sentence = 'This is a beautiful sunny day'
count = sum(1 for word in sentence.split() if len(word) > 4)
print("Q8:", count)  # Output: 2

# ------------------------------------------------------------

# 9. Mask all but last 4 characters
s = 'mysecretpassword1234'
masked = '*' * (len(s) - 4) + s[-4:]
print("Q9:", masked)  # Output: ****************1234

# ------------------------------------------------------------

# 10. Staircase pattern
s = 'python'
staircase = '\n'.join([' ' * i + s[i] for i in range(len(s))])
print("Q10:\n" + staircase)
# Output:
# p
#  y
#   t
#    h
#     o
#      n

# ------------------------------------------------------------

# 11. Reverse words
s = 'open ai builds tools'
reversed_words = ' '.join(s.split()[::-1])
print("Q11:", reversed_words)  # Output: tools builds ai open

# ------------------------------------------------------------

# 12. Characters at even indices
s = 'a1b2c3'
even_chars = ''.join([s[i] for i in range(0, len(s), 2)])
print("Q12:", even_chars)  # Output: abc
    
    
    



# 1. Greet user
def greet_user(name):
    return f"Hello, {name}!"

print("Q1:", greet_user(name="Ayesha"))

# ------------------------------------------------------------

# 2. Check temperature
def check_temperature(temp):
    return "Fever" if temp > 99 else "Normal"

print("Q2:", check_temperature(temp=101))

# ------------------------------------------------------------

# 3. Get last fruit from list
def get_last_fruit(fruits):
    return fruits[-1] if fruits else None

print("Q3:", get_last_fruit(['apple', 'banana', 'cherry']))


def gt_ft(frut):
    return frut[-2] if frut else None
print("gewt 2nd last",gt_ft(["apple","kela","naspasti"]))

# ------------------------------------------------------------

# 4. Get price tag
def get_price_tag(price):
    return "Expensive" if price > 1000 else "Affordable"

print("Q4:", get_price_tag(price=750))

# ------------------------------------------------------------

# 5. Format user info
def format_user_info(name, age):
    return f"Name: {name}, Age: {age}"

print("Q5:", format_user_info(name="Rahul", age=22))

# ------------------------------------------------------------

# 6. Uppercase if string
def uppercase_if_string(value):
    return value.upper() if isinstance(value, str) else "Invalid input"

print("Q6:", uppercase_if_string("hello"))
print("Q6:", uppercase_if_string(123))

# ------------------------------------------------------------

# 7. Safe divide
def safe_divide(num, den):
    return num / den if den != 0 else "Cannot divide"

print("Q7:", safe_divide(num=10, den=2))
print("Q7:", safe_divide(num=10, den=0))

# ------------------------------------------------------------

# 8. Check login
def check_login(credentials):
    return "Login successful" if credentials.get("password") else "Login failed"

print("Q8:", check_login({"username": "user1", "password": "pass123"}))
print("Q8:", check_login({"username": "user2", "password": ""}))

# ------------------------------------------------------------

# 9. Get full name in title case
def get_full_name(first, last):
    return f"{first.title()} {last.title()}"

print("Q9:", get_full_name(first="john", last="doe"))

# ------------------------------------------------------------

# 10. Get discounted price
def get_discounted_price(price, is_member):
    return price * 0.9 if is_member else price

print("Q10:", get_discounted_price(price=1200, is_member=True))
print("Q10:", get_discounted_price(price=1200, is_member=False))





# 1. Favorite fruits
fruits = ['Mango', 'Apple', 'Banana', 'Grapes', 'Orange']
print("Q1: First fruit:", fruits[0])
print("Q1: Last fruit:", fruits[-1])

# ------------------------------------------------------------

# 2. User input: cities visited
cities = input("Enter 3 cities you visited recently (space-separated): ").split()
print("Q2:", cities)

# ------------------------------------------------------------

# 3. Prices above 900 using slicing
prices = [1200, 850, 950, 720]
filtered = [price for price in prices if price > 900]
print("Q3:", filtered)

# ------------------------------------------------------------

# 4. First 5 even numbers + append 12
evens = [2, 4, 6, 8, 10]
evens.append(12)
print("Q4:", evens)

# ------------------------------------------------------------

# 5. Insert 'Python' at second position
languages = ['Java', 'C++', 'Go']
languages.insert(1, 'Python')
print("Q5:", languages)
languages.insert(2,"support")
print(languages)

# ------------------------------------------------------------

# 6. Split sentence into words
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Q6:", words)

# ------------------------------------------------------------

# 7. Remove last month
months = ['Jan', 'Feb', 'Mar', 'Apr']
months.pop()
print("Q7:", months)
months.pop()
print(months)

# ------------------------------------------------------------

# 8. Copy, sort, reverse
vehicles = ['car', 'bus', 'train']
copy_vehicles = vehicles.copy()
copy_vehicles.sort()
copy_vehicles.reverse()
print("Q8:", copy_vehicles)
copy_vehicles=vehicles.copy()
copy_vehicles.sort()
copy_vehicles.sort()
print(copy_vehicles)

# ------------------------------------------------------------

# 9. Count 'apple'
items = ['apple', 'banana', 'apple', 'cherry']
count = items.count('apple')
print("Q9: 'apple' appears", count, "times")
count=items.count("cherry")
print("chery :", {count})

# ------------------------------------------------------------

# 10. Use .format()
name = "Tom"
apples = 3
bananas = 5
print("Q10:", "{} has {} apples and {} bananas".format(name, apples, bananas))
name="md"
app=5
bana=3
print("toatal","{}has{}and{}".format(name,app,bana))

# ------------------------------------------------------------

# 11. List of characters in 'Hello'
chars = list('Hello')
print("Q11:", chars)

ch=list("rashid")
print("total",ch)

# ------------------------------------------------------------

# 12. Sum and average of 3 integers
numbers = [10, 20, 30]
total = sum(numbers)
average = total / len(numbers)
print("Q12: Sum =", total, ", Average =", average)

numb=[20,40,60]
total=sum(numb)
average=total/len(numb)
print("sum=",total,"average",average)

# ------------------------------------------------------------

# 13. Name to reversed character list
user_name = input("Enter your name: ")
char_list = list(user_name)
char_list.reverse()
print("Q13:", char_list)

u_n=input("ente name")
c_l=list(u_n)
c_l.reverse()
print("character",c_l)
# ------------------------------------------------------------

# 14. Check if 'Bob' is in list
names = ['Alice', 'Bob', 'Charlie']
print("Q14: Is 'Bob' in list?", 'Bob' in names)

for name in names:
    if name=="Bob":
        print("found",name)
        break
    else:
        print("not")


# ------------------------------------------------------------

# 15. Clear list
words = ['one', 'two', 'three']
words.clear()
print("Q15:", words)  # Output: []

words.clear()
print("clear",words)
