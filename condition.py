#1. 
'''
a=(input("Enter 1st value"))
b=input("Enter 2nd value")
eval("{a}")
eval("{b}")
print("before swap \n",a,b)
a,b = b,a
print("after swap \n",a,b)
'''

#2
'''
print("Welcome to Treasure Land")
dir=str(input("You want to go left or right:"))
if dir =='right':
    print("Game Over")
elif dir =='left':
    do=str(input("Do you want to swim or wait:"))
    if do=='swim':
        print("Game Over")
    elif do=='wait':
        col=str(input("choose red,blue ot yellow:"))
        if col=='red' or col=='blue':
            print("Game Over")
        elif col=='yellow':
            print("You Win")
        else:
            print("please choose from the option")
    else: 
        print("please choose from the option")  
else:
    print("please choose from the option")

'''
#4. 
'''
x=(input("Enter a integer"))
if x>0:
    print("True")
elif x<0:
    print("False")
elif x==0:
    print("Zero")
else:
    print("please enter a integer")
    '''
#5. 
'''
num=int(input("Enter a number"))
if num%2==0:
    print("It is even number")
else:
    print("It is odd number")
'''
#6
'''
res=int(input("Enter your marks:"))
if res>=70 and res<=100:
    print("Distinction")
elif res>=60 and res<=70:
    print("First class")
elif res>=40 and res<=60:
    print("Pass")
elif res<0 or res>100:
    print("enter valid marks")
else:
    print("Fail")
'''

#7
'''
tax=int(input("What's the price of the bike"))
if tax<=50000:
    print("You have to pay 5% tax")
elif tax >50000 and tax<=100000:
    print("You have to pay 10% tax ")
else:
    print("You have to pay 15% tax")
    '''

#8
'''
a=int(input("Enter the age of 1st person:"))
b=int(input("Enter the age of 2nd person:"))
c=int(input("Enter the age of 3rd person:"))
d=int(input("Enter the age of 4th person:"))
e=min(a,b,c,d)
print("The youngest one is ",e)

#9
a=int(input("Enter the age of 1st person:"))
b=int(input("Enter the age of 2nd person:"))
c=int(input("Enter the age of 3rd person:"))
d=int(input("Enter the age of 4th person:"))
e=max(a,b,c,d)
print("The o;dest one is ",e)
'''

#10
'''
grd=int(input("enter your mark:"))
if grd<25 and grd>=0:
    print("D")
elif grd>=25 and grd<45:
    print("C")
elif grd>=45 and grd<50:
    print("B")
elif grd>=50 and grd<60:
    print("B+")
elif grd>=60 and grd<80:
    print("A")
elif grd>80 and grd<=100:
    print("A+")
else:
    print("please enter your marks between 0 to 100")
'''

#11
'''
exp=float(input("Enter the time peroid in company of serive for bonus"))
if exp<6 and exp>0:
    print("Your bonus is 5%")
elif exp>=6 and exp<=10:
    print("Your bonus is 8%")
elif exp<=0:
    print("You are not eligible for bonus")
else:
    print("Your bonus is 10%")
'''

#12
'''
day=int(input("Days you took book from library:"))
if day==5:
    print("you have to pay rs 2")
elif day>5 and day<=10:
    fine= day*3
    print("you have to pay rs ",fine)
elif day>10 and day<=15:
    fine= day*4
    print("you havr to pay rs ",fine)
elif day>=15:
    fine= day*5
    print("you have to pay rs ",fine)
else:
    print("you dont have to pay")
    '''

#13
'''
sal=int(input("Enter your salary:"))
tm=int(input("How many years you have worked for the company:"))
if tm>5:
    bon=sal+(sal*15)/100
    print(bon)
else:
    print("you dont get bonus")
    '''

#14
'''
import math
rad=float(input("Enter the radius of circle"))
area=math.pi*rad**2
print("the area of circle is ",area)
'''

#15
'''
import math
a=int(input("total students in section a:"))
b=int(input("total students in section b:"))
c=int(input("total students in section c:"))
a=math.ceil(a/2)
b=math.ceil(b/2)
c=math.ceil(c/2)
print(f"You need {a+b+c} desks in total")
'''

#16
'''
N=int(input("Enter number of students:"))
K=int(input("Enter number of apples:"))
print(f"Each student gets {K//N} apples.")
print(f"{K%N} apples where remaining in the basket.")
'''

#17
'''
ag=int(input("Enter your age:"))
if ag<18:
  print("not eligible for voting")
else:
  print("Eligible for voting")
'''

#18
'''
cty=str(input("Enter the name of city(delhi,agra,jaipur):"))
if cty=='delhi':
    print("Red Fort")
elif cty=='agra':
    print("Taj Mahal")
elif cty=='jaipur':
    print("Jal Mahal")
else:
    print("Enter the city name as insturcted above.")
    '''

#19
'''
a=int(input("Enter a number"))
if a%2==0 and a%3==0:
    print("It is divisble by both 2 and 3")
else:
    print("It not is divisble by both 2 and 3")
'''

#20
'''
a=int(input("Ënter 1st number:"))
b=int(input("Enter 2nd number:"))
op=input("enter operator(+,-,*,/)")
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
else:
    print("please enter a valid operator")
'''

#21
'''
td=int(input("Total number of days:"))
tda=int(input("Total number of days for absent:"))
pr=((td-tda)*100)/td
if pr<75:
    print("You aren't eligible for exam")
else:
    print("You are eligible for exam")
'''

#22
'''
per=int(input("Enter your percentage:"))
if per<40:
    print("Failed")
elif per>=40 and per<55:
    print("Fair")
elif per>=55 and per<65:
    print("Good")
elif per>=65 and per<=100:
    print("Excellent")
else:
    print("Can't exceed more than 100")
'''

#23
'''
age=int(input("Enter your age:"))
gen=str(input("Enter your gender(m or f):"))
d=int(input("Enter number of days:"))
if age>=18 and age<30:
    if gen=='m':
       print(f"wage is {700*d}")
    elif gen=='f':
        print(f"wage is {750*d}")
    else: print("Unknown")
elif age>=30 and age<=40:
    if gen=='m':
        print(f"wage is {800*d}")
    elif gen=='f':
        print(f"wage is {850*d}")
else:print("Age doesn't match")         
'''      

#24
'''
1.print(c)
True
2.print(d)
True
3.print(not a)
False
4.print(not b)
False
5.print(not c)
False
6.print(not d)
False
7.print(a and b)
True
8.print(a or b)
True
9.print(a and b or c)
True
10.print(not a or b or c)
True
11. print(not a or not b or not c)
False
12.print(not(not a or not b or not c))
True
'''
#25
'''
num=int(input("Enter a number"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(f"{num}")
'''

#26
'''
usnm=str(input("Enter your username:"))
pswd=str(input("Enter your psssword:"))
if usnm=='admin123':
    if pswd=='softwarica123':
        print("LogIn Successfully")
    else:
        print("Your password is incorrect")
else:
    print("Please, Enter valid username")
'''

#27
'''
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
if a is not b: print(f"{max(a,b)} is the greater number")
elif a==b:
    if a<0: print("Negative")
    elif a>0: print("Positive")
    else: print("Zero")
'''

#28
'''
scr=int(input("Enter your subject score"))
if scr>=90 and scr<=100: print("Congratulations")
elif scr<90 and scr>=50: print("You need Improvement")
elif scr>100 or scr<0: print("Enter valid score")
else: print("Retake your exam")
'''

#29
'''
ag=int(input("Enter your age:"))
if ag>=18: 
    dg=str(input("Do you have degree(yes or no):"))
    if dg=='yes':
        exp=float(input("Enter your work experience:"))
        if exp<1: print("Under Review")
        elif exp>=1 and exp<3: print("Eligible")
        else: print("Highly Eligible")
    elif dg=='no': print("You are not Eligible")
    else: print("Choose between yes and no")
else: print("Not Eligible")
'''

#30
'''
wei=int(input("Weight of package:"))
urg=str(input("Is it a urgent delivery(yes or no):"))
if wei<5: 
    if urg=='yes': 
        print("$10")
    elif urg=='no':
        print("$5")
elif wei>=5 and wei<20:  
    if urg=='yes': 
        print("$15")
    elif urg=='no':
        print("$10")
else: 
    if urg=='yes': 
        print("$25")
    elif urg=='no':
        print("$20")
'''

#31
'''
ic=float(input("Enter your income:"))
if ic>=50000:
    cs=int(input("Enter your credit score:"))
    if cs<600: print("Your loan has been rejected")
    elif cs>=600 and cs<700: print("Approved with a higher interest rate.")
    else: print("Loan approved")
else:  print("Income is low")
   '''

#32
'''
wet=str(input("How is the weather of today?(sunny or rainy)"))
if wet=='sunny': print("go for hiking or a picnic")
elif wet=='rainy':
    ut=str(input("Do you have raincoat or umbrella?(yes or no):"))
    if ut=='yes':
        print("go to nearby mall or museum")
    elif ut=='no':
        print("stay home and watching movies")
else: print("undefined weather")
'''

#33
'''
print("Welcome to the Haunted House")
io=str(input("Do you want to go upstairs or downstairs?"))
if io=="downstairs": print("Game Over")
elif io=='upstairs':
    es=str(input("Do you want to enter the room or stay outside?"))
    if es=='enter the room':print("Game Over")
    elif es=='stay outside':
        gvw=str(input("Choose between ghost,vampire or werewolf:"))
        if gvw=='ghost' or gvw=='vampire': print("Game Over")
        if gvw=='werewolf': print("You Win")
'''

#34
'''
print("Welcome to the Jungle Adventure")
io=str(input("Do you want to go left or right?"))
if io=="right": print("Game Over")
elif io=='left':
    es=str(input("Do you want to climb a tree or explore the cave?"))
    if es=='climb a tree':print("Game Over")
    elif es=='explore the cave':
        gvw=str(input("Choose between bear,tiger or snake:"))
        if gvw=='bear' or gvw=='tiger': print("Game Over")
        if gvw=='snake': print("You Win")
        '''
#35
'''
print("Welcome to the Magic Forest")
io=str(input("Do you want to go north or south?"))
if io=="south": print("Game Over")
elif io=='north':
    es=str(input("Do you want to cross the river or follow the path?"))
    if es=='cross the river':print("Game Over")
    elif es=='follow the path':
        gvw=str(input("Choose between fairy,orge or elf:"))
        if gvw=='fairy' or gvw=='orge': print("Game Over")
        if gvw=='elf': print("You Win")
'''

#36
'''
print("Welcome to the Space Mission")
io=str(input("Do you want to moon or to mars?"))
if io=="to mars": print("Game Over")
elif io=='to moon':
    es=str(input("Do you want to land on the surface or stay on the orbit?"))
    if es=='land on the surface':print("Game Over")
    elif es=='stay on the orbit':
        gvw=str(input("Choose between alien,asteroid or satellite:"))
        if gvw=='alien' or gvw=='asteroid': print("Game Over")
        if gvw=='satellite': print("You Win")
'''

#37
print("Welcome to the Pairate Island")
io=str(input("Do you want to go left or right?"))
if io=="right": print("Game Over")
elif io=='left':
    es=str(input("Do you want to dig for treasure or sail the ship?"))
    if es=='dig for treasure':print("Game Over")
    elif es=='sail the ship':
        gvw=str(input("Choose between shark,pirate ship or mermaid:"))
        if gvw=='shark' or gvw=='pirate ship': print("Game Over")
        if gvw=='mermaid': print("You Win")
