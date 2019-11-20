print("Welcome to the Quiz")
print("Youll will have 5 question...answer correctly to move on to the next level!")




def state():
    print("  What is the a rough estimate of the population of New York City? ")
    print("a) 1 million")
    print("b) 3 million")
    print("c) 5 million")
    print("d) 8 million")
    print("e) 10 million")
    answer = input("Please enter a character a-e: ")
    correct_answer = 'd'

    if answer == correct_answer:
        print("Correct!")
        return 1
    elif answer != correct_answer:
        print("Incorrect!")
        return 0
    
def rick():
    print("How old is Rick Sanchez?")
    print("a)75 ")
    print("b)70 ")
    print("c)60 ")
    print("d)68 ")
    print("e)timeless ")
    answer = input("Please enter a character a-e: ")
    correct_answer = 'b'

    if answer == correct_answer:
        print("Correct!")
        return 1
    elif answer != correct_answer:
        print("Incorrect!")
        return 0
    


def catchphrase():
    print("The main Rick and Morty what we follow are from universe C - _ _ _ ")
    answer = int(input("Fill in the blanks C - _ _ _ : "))
    correct_answer = int("137")


    if answer == correct_answer:
        print("Correct! It's C-137")
        return 1
    elif answer != correct_answer:
        print("Incorrect!...Jerry")
        return 0
    

def rickbusiness():
    print("How many years was Rick away from his family?")
    answer = int(input("Enter a number of years 0 - ∞:  "))
    correct_answer = int("14")


    if answer == correct_answer:
        print("Correct! It's 14 years!")
        return 1
    elif answer != correct_answer:
        print("Still incorrect!......Jerry")
        return 0


def morty():
    print("Morty has never died on an andveture with Rick")
    answer = int(input("Enter a 0 for False or a 1 for True to the question: "))
    correct_answer = 1
    if answer == correct_answer:
        print("Correct!")
        return 1    
    elif answer != correct_answer:
        print("Incorrect!")
        return 0 


# state()
# print("")
# print("")
# print("")
# rick()
# print("")
# print("")
# print("")
# catchphrase()
# print("")
# print("")
# print("")
# rickbusiness()
# print("")
# print("")
# print("")
# morty()



total_score = 0
r1 = state()
print("")
print("")
print("")
r2 = rick()
print("")
print("")
print("")
r3 = catchphrase()
print("")
print("")
print("")
r4 = rickbusiness()
print("")
print("")
print("")
r5 = morty()
total_score += r1
total_score += r2
total_score += r3
total_score += r4
total_score += r5
print("")
print("")
print("")
print("")



print(f"You scored {total_score} out of 5!")




