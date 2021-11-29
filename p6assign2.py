from random import randint
import random
from typing import

FirstValue = random.randint (0, 99) 
SecondValue = random.randint (0, 99)

ThirdValue = random.randint (0, 99) 
FourthValue = random.randint (0, 99)

FifthValue = random.randint (0, 99) 
SixthValue = random.randint (0, 99)

SeventhValue = random.randint (0, 99) 
EighthValue = random.randint (0, 99)

NinethValue = random.randint (0, 99) 
TenthValue = random.randint (0, 99)

EleventhValue = random.randint (0, 99) 
TwelfthValue = random.randint (0, 99)

ThirteenthValue = random.randint (0, 99) 
FourtheenthValue = random.randint (0, 99)

FifteenthValue = random.randint (0, 99) 
SixteenthValue = random.randint (0, 99)

SeventheenthValue = random.randint (0, 99) 
EightheenthValue = random.randint (0, 99)

NinetheenthValue = random.randint (0, 99) 
TwentiethValue = random.randint (0, 99)


def FirstQuestion():
    points = 0
    print(f"{FirstValue} + {SecondValue}")
    sum = int(input("Enter your answer: "))
    if sum == FirstValue + SecondValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def SecondQuestion():
    points = 0 
    print(f"{ThirdValue} + {FourthValue}")
    sum1 = int(input("Enter your answer: "))
    if sum1 == ThirdValue + FourthValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def ThirdQuestion():
    points = 0
    print(f"{FifthValue} + {SixthValue}")
    sum = int(input("Enter your answer: "))
    if sum == FifthValue + SixthValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def FourthQuestion():
    points = 0
    print(f"{SeventhValue} + {EighthValue}")
    sum = int(input("Enter your answer: "))
    if sum == SeventhValue + EighthValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def FifthQuestion():
    points = 0
    print(f"{NinethValue} + {TenthValue}")
    sum = int(input("Enter your answer: "))
    if sum == NinethValue + TenthValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def SixthQuestion():
    points = 0
    print(f"{EleventhValue} + {TwelfthValue}")
    sum = int(input("Enter your answer: "))
    if sum == EleventhValue + TwelfthValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def SeventhQuestion():
    points = 0
    print(f"{ThirteenthValue} + {FourtheenthValue}")
    sum = int(input("Enter your answer: "))
    if sum == ThirteenthValue + FourtheenthValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def EighthQuestion():
    points = 0
    print(f"{FifteenthValue} + {SixteenthValue}")
    sum = int(input("Enter your answer: "))
    if sum == FifteenthValue + SixteenthValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def NinethQuestion():
    points =0
    print(f"{SeventheenthValue} + {EightheenthValue}")
    sum = int(input("Enter your answer: "))
    if sum == SeventheenthValue + EightheenthValue:
       points += 1 
        
    else:
        points += 0
        
    return points

def TenthQuestion():
    points =0
    print(f"{NinetheenthValue} + {TwentiethValue}")
    sum = int(input("Enter your answer: "))
    if sum == NinetheenthValue + TwentiethValue:
       points += 1 
        
    else:
        points += 0
        
    return points

Question1 = FirstQuestion() 
Question2 = SecondQuestion()
Question3 = ThirdQuestion()
Question4 = FourthQuestion()
Question5 = FifthQuestion()
Question6 = SixthQuestion()
Question7 = SeventhQuestion()
Question8 = EighthQuestion()
Question9 = NinethQuestion()
Question10 = TenthQuestion()

Result= Question1 + Question2 + Question3 + Question4 + Question5 + Question6 + Question7 + Question7 + Question8 + Question9 + Question10
print(f'Your total score is {Result} out of 10!')








        
   





