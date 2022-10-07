#Question1. Write a function to take input from user in days and print it in years, month and days
#input - 397, output - 1 year , 1 month , 1 day

def days():
    num=int(input("enter the days:"))
    years = num//365
    months = (num-years*365)//30
    days =(num- years*365-months*30)
    print(num,"days=",years,"years",months,"months",days,"days")
days()

#Question2. Generate fibnoacci series for 1 to 20

x, y = 1, 1
print("Fibonacci sequence:")
while x < 20:
    print(x)
    z = x + y   
    x = y
    y = z 



#Question3. Create a program to play RPS Game
"""
Inputs:
1. Enter Player name 1
2. Enter Player name 2
3. Enter Player 1 Choice
4. Enter Player 2 Choice


Choices are "Rock", "Scissor", "Paper"

result: who wins?


display result: Player name with choice Rock wins
Player name with choice Scissor Lose


how to manipulate result:
If P1 enter Rock and P2 enters Scissor then P1 Wins
if P1 enter Rock and P2 enters Paper then P2 Wins
if P1 enter Scissor and P2 enters Paper then P1 wins
if both player enters the same choice it should say "Tie"

"""


player1 = (input("Enter the first player"))
player2 = (input("Enter the second player"))
player1_choice = (input("Enter the choice of the first player"))
player2_choice = (input("Enter the choice of the second player"))
if player1_choice == player2_choice:
 print("Tie")
elif player1_choice == "Rock" and player2_choice == "Scissor":
 print(player1,"Wins")
elif player1_choice == "Rock" and player2_choice == "Paper":
 print(player2,"Wins")
elif player1_choice == "Scissor" and player2_choice == "Paper":
 print(player1,"Wins")
elif player1_choice == "Scissor" and player2_choice == "Rock":
 print(player2,"Wins")
elif player1_choice == "Rock" and player2_choice == "Scissor":
 print(player1,"Wins")
elif player1_choice == "Rock" and player2_choice == "Paper":
 print(player2,"Wins")





"""Question4. Write functions to calculate and display grosssalary and netsalary of an employee after getting input as basicsalary
Write separate functions for allowances and deductions to calculate them respectively

netsalary = grosssalary - deductions
grosssalary = basicsalary + allowances

allowances = hra(22% of basicsalary) + da(18% of basicsalary) +ta(10% of basicsalary)

deductions = proftax(if basicsalary > 8000 the 200 else 150) + pf(12% of basicsalary) + insurance(8% of basicsalary)
"""

def allowances():
    allowance=(22/100)*salary+(18/100)*salary+(10/100)*salary
    #print(allowance)
    return allowance

def deductions():
    if(salary>8000):
        profitTax=200
    else:
        profitTax=150
    deduction=profitTax+((12/100)*salary)+((8/100)*salary)
    #print(deduction)
    return deduction
    

    
def grossSalary(basicsalary):
    allowance=allowances()
    gross_salary = basicsalary + allowance
    print("Gross salary is :",gross_salary)
    netsalary(gross_salary)
    

def netsalary(grosssalary):
    deduction=deductions()
    net_salary = grosssalary - deduction
    print("Net salary is :",net_salary)


salary=int(input("enter your basic salary:"))
grossSalary(salary)





#Question5. For the given string 
#Calculate the number of vowels individually i.e number of a, e, i , o and u , calculate total number of consonants without considering any punctuation character

string="""
Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"""
string.lower()

consonants=0
vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in string:
    if i in vowels:
        vowels[i]+=1
    elif(i.isalpha()):
        consonants+=1
for key in vowels:
    print(key,":",vowels[key])
print("consonants:",consonants)






#Question6. Ask user a input string and check if the entered string is palindrome. Ex: Input NitiN -> o/p palindrome

string1=input("Enter the string:")
if(string1==string1[::-1]):
    print(string1,"is palindrome")
else:
    print(string1,"is not palindrome")

#7.
str1 = input("Enter the Email ID : ")
if (str1[0]!='@' and str1[0]!='.') and (str1[:1]!='@' and str1[:1]!='.') and (str1.count('@')==1) and (str1.count('.')==1):
    print(str1,"is Valid ")
else:
    print(str1,"is InValid ")




#8.
def hotel_cost(night):
    return 140*night

def plane_ride_cost(city):
    if city == 'charlotte':
        return 183
    elif city == 'tampa':
        return 220
    elif city == 'pittsburgh':
        return 222
    elif city == 'los angeles':
        return 475
    else:
        print("Invalid ")

def rental_car_cost(days):
    if days >= 7:
        car_cost = (40*days)-50
    elif days >= 3:
        car_cost = (40*days)-20
    else:
        car_cost = 40*days
    return car_cost

def trip_cost(city,days,spending_money):
    cost= int(rental_car_cost(days)+ plane_ride_cost(city) + hotel_cost(days)+spending_money)
    print ("Total Cost : ",cost)

c = input("Enter the city (charlotte,tampa,pittsburgh,los Angeles) : ")
city = c.lower()
days = int(input("Enter the no. of days : "))
spending_money = int(input("Enter the amount : "))
trip_cost(city,days,spending_money)



#9.
bakery_items={"bread":40,"butter":120,"jam":200,"cheese":220,"crossiant":60}
cart={}
def display_cart():
    print(bakery_items)
    

def add_cart():
    item=input('''Enter the item:
                  Bread
                  Butter
                  jam
                  Cheese
                  crossiant
                  :''').lower()
          
    if(item not in bakery_items):
        print("wrong item")
    elif item not in cart:
        cart[item]=1
    else:
        print("already in cart")
        

def view_cart():
    print(cart)

def update_cart():
    item=input('''Enter the item:
                  Bread
                  Butter
                  jam
                  Cheese
                  crossiant
                  :''').lower()
    if(item not in bakery_items):
        print("wrong item")
    elif item in cart:
        qt=int(input("Enter Quantity:"))
        cart[item]=qt
    
    
def remove_cart():
    item=input('''Enter the item:
                  Bread
                  Butter
                  jam
                  Cheese
                  crossiant
                  :''').lower()
    if(item not in bakery_items):
        print("wrong item")
    elif item in cart:
        del cart[item]
    

def bill():
    print("-------Bill information-------")
    print("item \t","cost\n")
    cost=0
    for item in cart:
          print(item,"\t",cart[item]*bakery_items[item],"\n")
          cost=cost+cart[item]*bakery_items[item]
    print("Total cost:",cost)
        
flag=0
while(flag==0):
    choice=int(input('''Enter the choice
                   1. View the bakery items
                   2. Add the item into the cart
                   3. View the cart
                   4. Update item in the cart
                   5. Remove item from the cart
                   6. Checkout and generate bill
                   :
            '''))

    if(choice==1):
        display_cart()
    elif(choice==2):
        add_cart()
    elif(choice==3):
        view_cart()
    elif(choice==4):
        update_cart()
    elif(choice==5):
        remove_cart()
    elif(choice==6):
        bill()
        flag=1




























