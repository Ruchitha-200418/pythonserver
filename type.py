#typecasting

#name = "Bro code"
#age = 25
#gpa = 3.2
#is_student = True

#name = bool(name)

#print(name)
#input()
#name = input("what is your name?: ")
#age = input("how old are you?: ")
#age = int(age)
#age = age+1

#print(f"hello {name}!")
#print(f"happy birthday")
#print(f"you are {age} years old")
#length = float(input("enter the length: "))
#width = float(input("enter the width: "))
#area = length * width
#print(f"the area is: {area}cm2")

#item = input("what item would you like to buy?: ")
#price = float(input("what is the price?: "))
#quantity = int(input("how many would you like?: "))
#total = price * quantity

#print(total)
#x = "awesome"

#def myfunc():
 # x = "fantastic"
  #print("Python is " + x)

#myfunc()

#print("Python is " + x)

x = 5
print(type(x))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

import random

print(random.randrange(1,20))

age = 36
txt = f"My name is John, I am {age}"
print(txt)

x = 5
y = 3

print(x + y)

x = 5
y = 3

print(x - y)

x = 5
y = 3

print(x * y)

x = 12
y = 3

print(x / y)

x = 5
y = 2

print(x % y)

x = 2
y = 5

print(x ** y) #same as 2*2*2*2*2

x = 15
y = 2

print(x // y)

#the floor division // rounds the result down to the nearest whole number
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# Simple Python Quiz Game

def quiz():
    print("Welcome to the Python Quiz Game!")
    print("Answer the questions by typing the correct option (a/b/c/d).")
    print("-" * 50)

    questions = [
        {
            "question": "1. Who developed the Python programming language?",
            "options": {"a": "Dennis Ritchie", "b": "Guido van Rossum", "c": "James Gosling", "d": "Bjarne Stroustrup"},
            "answer": "b"
        },
        {
            "question": "2. Which of the following is a mutable data type in Python?",
            "options": {"a": "tuple", "b": "string", "c": "list", "d": "frozenset"},
            "answer": "c"
        },
        {
            "question": "3. What is the correct file extension for Python files?",
            "options": {"a": ".pyth", "b": ".pt", "c": ".py", "d": ".p"},
            "answer": "c"
        },
        {
            "question": "4. Which keyword is used to define a function in Python?",
            "options": {"a": "define", "b": "function", "c": "def", "d": "fun"},
            "answer": "c"
        },
        {
            "question": "5. What does the len() function do?",
            "options": {"a": "Counts characters", "b": "Returns the length", "c": "Adds numbers",
                        "d": "Converts to string"},
            "answer": "b"
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for key, value in q["options"].items():
            print(f"   {key}) {value}")

        answer = input("Your answer: ").lower()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was '{q['answer']}) {q['options'][q['answer']]}'")

    print("\n" + "-" * 50)
    print(f"Your final score is {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Excellent! You got all correct!")
    elif score >= 3:
        print("👍 Good job!")
    else:
        print("😢 Better luck next time!")


if __name__ == "__main__":
    quiz()


    # Concession Stand Program

    def concession_stand():
        print("🎬 Welcome to the Concession Stand! 🎉")
        print("Here’s our menu:")
        print("-" * 40)

        menu = {
            "Popcorn": 5.00,
            "Nachos": 4.50,
            "Soda": 2.00,
            "Candy": 1.50,
            "Hot Dog": 3.50
        }

        for item, price in menu.items():
            print(f"{item:10} - ${price:.2f}")

        print("-" * 40)

        order = {}
        while True:
            choice = input("Enter an item to order (or type 'done' to finish): ").title()

            if choice.lower() == "done":
                break

            if choice in menu:
                quantity = int(input(f"How many {choice}(s) would you like? "))
                if choice in order:
                    order[choice] += quantity
                else:
                    order[choice] = quantity
            else:
                print("❌ Item not on the menu. Please try again.")

        print("\n🧾 Your Receipt:")
        print("-" * 40)

        total = 0
        for item, qty in order.items():
            cost = menu[item] * qty
            print(f"{item:10} x {qty:<3} = ${cost:.2f}")
            total += cost

        print("-" * 40)
        print(f"TOTAL: ${total:.2f}")
        print("✅ Thank you for your purchase! Enjoy your snacks! 🍿🥤")


    if __name__ == "__main__":
        concession_stand()





