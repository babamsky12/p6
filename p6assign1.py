    # Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.
# Plus, list all the possible sequence.

print("Welcome to Number Sorter!")


N1 = float(input("Enter your first number: "))
N2 = float(input("Enter your second number: "))
N3 = float(input("Enter your third number: "))
N4 = float(input("Enter your fourth number: "))


if N1 > N2 and N2 > N3 and N3 > N4: 
    print(f"The sequence from highest to lowest is {N1} , {N2} , {N3} , {N4}.")

elif N1 > N2 and N2 > N4 and N4 > N3:
    print(f"The sequence from highest to lowest is {N1} , {N2} , {N4 }, {N3}.")

elif N1 > N3 and N3 > N2 and N2 > N4:
    print(f"The sequence from highest to lowest is {N1} , {N3} , {N2} , {N4}.")

elif N1 > N3 and N3 > N4 and N4 > N2:
    print(f"The sequence from highest to lowest is {N1} , {N3} , {N4 }, {N2}.")

elif N1 > N4 and N4 > N3 and N3 > N2:
    print(f"The sequence from highest to lowest is {N1} , {N4} , {N3} , {N2}.")

elif N1 > N4 and N4 > N2 and N2 > N3:
    print(f"The sequence from highest to lowest is {N1} , {N4} , {N2} , {N3}.")

elif N2 > N1 and N1 > N3 and N3 > N4:
    print(f"The sequence from highest to lowest is {N2} , {N1} , {N3} , {N4}.")

elif N2 > N3 and N3 > N4 and N4 > N1:
    print(f"The sequence from highest to lowest is {N2} , {N3} , {N4} , {N1}.")

elif N2 > N1 and N1 > N4 and N4 > N3:
    print(f"The sequence from highest to lowest is {N2} , {N1} , {N4} , {N3}.")    

elif N2 > N3 and N3 > N1 and N1 > N4:
    print(f"The sequence from highest to lowest is {N2} , {N3} , {N1} , {N4}.")

elif N2 > N4 and N4 > N1 and N1 > N3:
    print(f"The sequence from highest to lowest is {N2} , {N4} , {N1} , {N3}.")

elif N2 > N4 and N4 > N3 and N3 > N1:
    print(f"The sequence from highest to lowest is {N2} , {N4} , {N3} , {N1}.")

elif N3 > N1 and N1 > N2 and N2 > N4:
    print(f"The sequence from highest to lowest is {N3} , {N1} , {N2} , {N4}.")

elif N3 > N1 and N1 > N4 and N4 > N2:
    print(f"The sequence from highest to lowest is {N3} , {N1} , {N4} , {N2}.")

elif N3 > N2 and N2 > N1 and N1 > N4:
    print(f"The sequence from highest to lowest is {N3} , {N2} , {N1} , {N4}.")

elif N3 > N2 and N2 > N4 and N4 > N1:
    print(f"The sequence from highest to lowest is {N3} , {N2} , {N4} , {N1}.")

elif N3 > N4 and N4 > N1 and N1 > N2:
    print(f"The sequence from highest to lowest is {N3} , {N4} , {N1} , {N2}.")

elif N3 > N4 and N4 > N2 and N2 > N1:
    print(f"The sequence from highest to lowest is {N3} , {N4} , {N2} , {N1}.")

elif N4 > N1 and N1 > N2 and N2 > N3:
    print(f"The sequence from highest to lowest is {N4} , {N1} , {N2}, {N3}.")

elif N4 > N1 and N1 > N3 and N3 > N2:
    print(f"The sequence from highest to lowest is {N4} , {N1} ,{N3} , {N2}.")

elif N4 > N2 and N2 > N1 and N1 > N3:
    print(f"The sequence from highest to lowest is {N4} , {N2}, {N1} , {N3}.")

elif N4 > N2 and N2 > N3 and N3 > N1:
    print(f"The sequence from highest to lowest is {N4} , {N2} , {N3} , {N1}.")

elif N4 > N3 and N3 > N1 and N1 > N2:
    print(f"The sequence from highest to lowest is {N4} , {N3} , {N1} , {N2}.")

else:
    print(f"The sequence from highest to lowest is {N4} , {N3} , {N2} , {N1}.")

print("Thank you for using the Number Sorter! Take care!")
    
 

