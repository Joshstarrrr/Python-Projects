answer = 0
y = 0
n = 0
# --------- Defining what each thing does to call later ---------

 

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    save(str(a) + " + " + str(b) + " = " + str(answer))

def minus(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
    save(str(a) + " - " + str(b) + " = " + str(answer))

def multi(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))
    save(str(a) + " * " + str(b) + " = " + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))
    save(str(a) + " / " + str(b) + " = " + str(answer))

def mod(a, b):
    answer = a % b
    print(str(a) + " % " + str(b) + " = " + str(answer))
    save(str(a) + " % " + str(b) + " = " + str(answer))

def power(a, b):
    answer = a ** b
    print(str(a) + "^" + str(b) + " = " + str(answer))
    save(str(a) + "^" + str(b) + " = " + str(answer))

def root(a):
    answer = a ** 0.5
    print("The square root of " + str(a) + " = " + str(answer))
    save("The square root of " + str(a) + " = " + str(answer))

def save(answer):
    saveresult = input("Would you like to save the results to Results.txt? ").upper()
    if saveresult == "Y":
        with open("Results.txt", "a") as file: # append mode to prevent overwriting
            file.write(answer + "\n")          # \n new line 
            print("File saved")


print("A. Mathmatical Calculator")
print("B. Conversions") # literally has 1 thing lmfao

Choice1 = input("Choose a mode ").upper()



# --------- Prints out options to choose (stored in choice variable)---------
if Choice1 == "A":
 print("A. Addition")
 print("B. Subtraction")
 print("C. Multiplication")
 print("D. Division")
 print("E. Modular") # Remainder
 print("F. exponentiation") # Power of
 print("G. Root (square)")


# --------- Variables that stores user input---------
 b = 0
 a = 0

 Choice = input("Choose a mode ").upper() # Upper so users can input 'A' and 'a' for example
 a = float(input("Input first number ")) # float to support decimals
 if Choice == ("f").upper():
    b = float(input("Input another number to multiply to the power of ")) # makes it easier to understand i guess

 elif Choice == ("G").upper():
     a == b

 else:
     b = float(input("Input a second number "))

# --------- If/else statements based on earlier input which calls the things from earlier.---------
 if Choice == "A":
     add(a, b)
 elif Choice == "B":
     minus(a, b)
 elif Choice == "C":
     multi(a, b)
 elif Choice == "D":
     div(a, b)
 elif Choice == "E":
     mod(a, b)
 elif Choice == "F":
     power(a, b)
 elif Choice == "G":
     root(a)
 else:
     print("Error. try running the program again.")
# -----------------------------------------------  OPTION 2 (CONVERTSIONS) -----------------------------------------------
elif Choice1 == "B":
    def Celcius(a):
        answer1 = (a * 9/5) + 32
        print(str(a) + "ºC in ºF would be " + str(answer1))
        save(str(a) + "ºC in ºF would be " + str(answer))
    
    print("A. ºC to ºF Converter")
    Choice2 = input("Input your choice ").upper() # Upper so users can input 'A' and 'a' for example
    a = float(input("Input a number ")) # float to support decimals

# -------------- if statements for option 2 -------------

if Choice2 == "A":
     Celcius(a)


        

save(answer)



    