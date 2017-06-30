AllAnswers = input("Enter you equation, example, 5+2: ")
List = AllAnswers.split(" ")

#If there are 3 sequences of 'strings', do this
if len(List) == 3:
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
    elif List[1] == "**":#Exponet
        Final =  Num1 ** Num2
    else:
        print("Invalid.")
        Final = 0


if len(List) == 5:
    Num1 = int(List[0])
    Num2 = int(List[2])
    Num3 = int(List[4])

    if List[1] == "+":#Addition
        if List[3] == "+":
            #+
            Final = Num1 + Num2 + Num3
            
        elif List[3] == "-":
            #-
            Final = Num1 + Num2 - Num3
            
        elif List[3] == "*":
            #*
            Final = Num1 + Num2 * Num3
            
        elif List[3] == "/":
            #/
            Final = Num1 + Num2 / Num3
            
        elif List[3] == "**":
            #**
            Final = Num1 + Num2 ** Num3
        #--------------------------------#
    
    elif List[1] == "-":#Subtraction
        if List[3] == "+":
            #+
            Final = Num1 - Num2 + Num3
            
        elif List[3] == "-":
            #-
            Final = Num1 - Num2 - Num3
            
        elif List[3] == "*":
            #*
            Final = Num1 - Num2 * Num3
            
        elif List[3] == "/":
            #/
            Final = Num1 - Num2 / Num3
            
        elif List[3] == "**":
            #**
            Final = Num1 - Num2 ** Num3
         #-------------------------------#
    elif List[1] == "*":#Mulitplication
        if List[3] == "+":
            #+
            Final = Num1 * Num2 + Num3
            
        elif List[3] == "-":
            #-
            Final = Num1 * Num2 - Num3
            
        elif List[3] == "*":
            #*
            Final = Num1 * Num2 * Num3
            
        elif List[3] == "/":
            #/
            Final = Num1 * Num2 / Num3
            
        elif List[3] == "**":
            #**
            Final = Num1 * Num2 ** Num3
         #-------------------------------#    
    elif List[1] == "/":#Division
        if List[3] == "+":
            #+
            Final = Num1 / Num2 + Num3
            
        elif List[3] == "-":
            #-
            Final = Num1 / Num2 - Num3
            
        elif List[3] == "*":
            #*
            Final = Num1 / Num2 * Num3
            
        elif List[3] == "/":
            #/
            Final = Num1 / Num2 / Num3
            
        elif List[3] == "**":
            #**
            Final = Num1 / Num2 ** Num3
         #-------------------------------#
    elif List[1] == "**":#Exponet
        if List[3] == "+":
            #+
            Final = Num1 ** Num2 + Num3
            
        elif List[3] == "-":
            #-
            Final = Num1 ** Num2 - Num3
            
        elif List[3] == "*":
            #*
            Final = Num1 ** Num2 * Num3
            
        elif List[3] == "/":
            #/
            Final = Num1 ** Num2 / Num3
            
        elif List[3] == "**":
            #**
            Final = Num1 ** Num2 ** Num3
         #-------------------------------#
    else:
        print("Invalid.")
        Final = 0
print(str(Final))
