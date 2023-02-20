def opening ():
    print('Hello!')    

def countdown(num_choice):
     while num_choice >= 0:
        print(num_choice)
        num_choice -= 1

def factorial(num_choice):
    if num_choice == 0:
        print("The factorial of 0 is 1");
    elif num_choice < 0:
        print("Let's not choose a negative number..!!");
    else:
        factor = 1;
        for i in range(1, num_choice+1):
            factor = factor*i;
        print("The factorial of", num_choice, "is", factor);

while(True):
    opening()

    num_choice = int(input('Enter any number greater than 1: '))
    if num_choice <= 1 : # error message because user can't follow directions
        print("ERROR!!! Greater than 1 please.") 
        num_choice = int(input('Enter any number greater than 1: '))
        num_choice2 = int(input('Now pick 1 for your chosen number countdown or 2 for the factorial of your chosen number: '))
    elif num_choice > 1 :
        num_choice2 = int(input('Now pick 1 for your chosen number countdown or 2 for the factorial of your chosen number: '))
    
    if num_choice2 <= 0: 
        print("Error!!! Your choices are number 1 or number 2. Your choice? ")
        num_choice2 = int(input('Now pick 1 for your chosen number countdown or 2 for the factorial of your chosen number: '))

    if num_choice2 == 1:
        countdown(num_choice)

    if num_choice2 == 2:
        factorial(num_choice)

    if(input("Done! Would you like to replay?(y/n): ")=='y'):
        continue
    else:
        break
