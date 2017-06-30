AllAnswers = input("Enter you equation, example, 5+2: ")
List = AllAnswers.split(" ")
Num1 = int(List[0])
Num2 = int(List[2])

#Here, it checks what operation will be used in the middle of the list#

if List[1] == "+":#Addition
    Final = Num1 + Num2
    
elif List[1] == "-":#Subtraction
    Final = Num1 - Num2
    
elif List[1] == "*":#Mulitplication
    Final = Num1 * Num2
    
elif List[1] == "/":#Division
    Final = Num1 / Num2
else:
    print("Invalid.")
print(str(Final))
