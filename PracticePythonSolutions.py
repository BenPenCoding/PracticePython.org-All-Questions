#1 - character input
'''
name,age = str(input("Please enter your name: ")),int(input("Please enter your age: "))
message = f"\nHello {name}, you are {age} years old and will turn 100 in around {(2024)+(100-age)}\n"
print(message)
num = int(input("How many more times shall we show you that message?"))
for i in range(num): print(message)
'''

#2 - odd or even
'''
#part1
num = int(input("Please enter a number: "))
if num%4 == 0: print("Your number is divisible by 4!")
else:   
    if num%2 == 0: print("Your number is even!")
    else: print("Your number is odd!")

#part2
num1, num2 = int(input("Enter a number: ")), int(input("Enter a number to divide it by: "))
if num1%num2 == 0: print(f"Your number: {num1}, is divisible by: {num2}")
else: print(f"Your number: {num1}, is not divisible by: {num2}")
'''

#3 - list less then ten
'''
a=[1,1,2,3,5,8,13,21,34,40,55,89]
b = []
num = int(input("Please enter your max number you want in the list: "))
b.append([x for x in a if x<=num])
print(b)
'''

#4 - divisors

'''
import math
while True:
    try: num = int(input("Please enter a number: "));break
    except: pass
divs,div =[],math.ceil(num/2)
divs.append(num)
while div != 0:
    if num%div == 0: divs.append(int(div))
    div -=1  
print(divs)
'''

#5 - list overlaps

'''
from random import *
a,b,c = [],[],[]
for i in range(15): a.append(randint(0,30))
for i in range(10): b.append(randint(0,30))
def largerList(p1,p2):
    if len(p1)>len(p2): return p1,p2
    else: return p2,p1
for i in largerList(a,b)[0]:
    if i in largerList(a,b)[1]: c.append(i)
print(a,b,c)
'''

#6 - string lists

'''
var = str(input("Please enter your word: "))
if var[::-1] == var: print("word is a palindrome!")
else: print("Word is not a palindrome")
'''

#7 - list comprehensions

'''
from random import *
a,b =[],[]
for i in range(100): a.append(randint(1,100))
b.append([x for x in a if x%2==0]);print(b)
'''

#8 - rock paper scissors

'''
#rock paper scissors, 8
r = ['s','p']
s = ['p','r']
p = ['r','s']
#list = ['rock','paper','scissors']
print("Welcome to the game! Rules: type 'scissors' for scissors, etc.")
while True:
    start = str(input("\nPress enter to play! Or type exit to leave: "))
    if start.lower() == "exit": print("Bye!");break
    input1,input2 = "",""
    while True:
        input1 = str(input("\nPlayer 1's go: "))
        input1 = input1.lower()
        if input1 == 'rock' or input1 == 'paper' or input1 == 'scissors': break
        else:print("\nThat's not a valid choice!\n")   
    print("\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------\n----------")
    while True:
        input2 = str(input("\nPlayer 2's go: "))
        input2 = input2.lower()
        if input2 == 'rock' or input2 == 'paper' or input2 == 'scissors':break
        else:print("\nThat's not a valid choice!\n")
    if input1 == input2:print("You both said the same thing! Let's go again. ")
    else:
        if input1[0] == 'r':
            if input2[0] == "s":print("\nPlayer 1 wins!")
            else:print("\nPlayer 2 wins!")
        if input1[0] == 's':
            if input2[0] == "p":print("\nPlayer 1 wins!")
            else:print("\nPlayer 2 wins!")
        if input1[0] == 'p':
            if input2[0] == "r":print("\nPlayer 1 wins!")
            else:print("\nPlayer 2 wins!")
'''

#9 - guessing game one

'''
from random import *
guesses = 0
while True:
    num, uNum = randint(1,9),str(input("Please enter your guess, or type 'exit' to exit. "))
    if uNum.lower() == 'exit': break
    else:
        if uNum == str(num): print("You got it right!")
        else: print("You got it wrong!")
    guesses +=1
print(f"You took {guesses} guesses to guess a correct number!")
'''

#10 - list overlap comprehensions

'''
from random import *
a,b,c = [],[],[]
for i in range(20): a.append(randint(1,99));b.append(randint(1,99))
for x in a:
    if x in b and x not in c: c.append(x)
print(c)
'''

#11 - check primality functions 

'''
import math
def getInput():
    while True:
        try: pNum = int(input("Please enter a number: "));break
        except: pass
    return pNum
def findPrime(pNum):
    divs,div =[],math.ceil(pNum/2)
    divs.append(pNum)
    while div != 0:
        if pNum%div == 0: divs.append(int(div))
        div -=1
    if len(divs) == 2: return "Woah a prime number!"
    else: return "Nope, not a prime number!"
userInput = getInput()
print(findPrime(userInput))
'''

#12 - list ends

'''
from random import *
def listEnds():
    a,b = [],[]
    for i in range(randint(2,99)): a.append(randint(1,99))
    b.extend([a[0],a[-1]]); print(b)
listEnds()
'''

#13 - fibonacci

'''
def fib(num):
    num1,num2,num3 = 0,1,0
    for i in range(num): print(num1); num3=num1+num2; num1 = num2; num2 = num3
fib(int(input("How many fibonacci numbers should I generate? ")))
'''

#14 - list remove duplicates

'''
#part1, loop
a,b = [1,1,2,3,3,3,3,3,4,4,4,5,6,6,6,7,7,8,8,9],[]
for x in a:
    if b.count(x) == 0: b.append(x)
print(b)

#part2, sets
a,b = [1,1,2,3,3,3,3,3,4,4,4,5,6,6,6,7,7,8,8,9],[]
b = list(set(a));print(b)
'''

#15 - reverse word order

'''
string,a,b = str(input("Please enter your sentence: ")),[],[]
a.append(string.split())
for i in range(len(a[0]),0,-1):b.append((a[0][i-1]))
for x in b: print(x,end=' ')
'''

#16 - password generator

'''
from random import *
def genW():
    a, b= ["chilli","beans","spaghetti","apple","glue","water","gum"], ""
    for i in range(3): b+=(a[randint(0,len(a))])
    return(b)
def genS(length):
    a,b=[],""
    for i in range(length):   
        a.extend([chr(randint(65,90)), chr(randint(97,122)), chr(randint(33,47)), randint(0,9)])
        b+=str(a[randint(0,len(a)-1)])
    print(b)
strength = int(input("Type 0 for weak, 1 for strong: "))
if strength == 1: print(genS(int(input("Enter how many digits: "))))
else: print(genW())
'''

#17 - decode a web page

'''
An issue with the current bs4 library and the NY Times API renders this activity impossible.
'''

#18 - cows and bulls

'''
def find(pGuess,pWord):
    count,cows,bulls = 0,0,0
    for i in pGuess:
        if i == pWord[count]: cows+=1
        else:    
            for j in pWord:
                if i == j: bulls +=1
        count+=1
    return f"{cows} cow(s), and {bulls} bull(s). "
if __name__=="__main__":print(find('1234','1038'))
'''

#19 - decode a web page two

'''
An issue with the current bs4 library and the NY Times API renders this activity impossible.
'''

#20 - element search

'''
a,b,c = [1, 3, 5, 30, 42, 43, 500],3,False

for i in a:
    if i == b: c = True
print(c)
'''

#21 - write to a file

'''
name = str(input("Please enter a name for the file: "))
file = open(name+'.txt',"w");file.write("Hello!")
'''

#22 - read from a file

'''
file = open("names.txt","r")
pList = []
for i in file:
    pList.append(i.replace("\n",""))
done = []
results = []
for i in pList:
    if i in done:
        pass
    else:
        results.append([i,pList.count(i)])
        done.append(i)
        
print(results)
'''

#23 - file overlap

'''
file1 = open("nums1.txt","r")
nums1 = []
for i in file1: nums1.append(i.replace("\n",""))
file2 = open("nums2.txt","r")
nums2 = []
for i in file2: nums2.append(i.replace("\n",""))
overlap = []
for i in nums1:
    if i in nums2:
        overlap.append(i)
        
print(overlap)
'''

#24 - draw a game board

'''
size = int(input("How big would you like the grid? type '3' for a 3x3 for example: "))

def dotRows(pSize):
    string = " - - -   "
    for i in range(pSize):
        print(string,end='')
    print("\n")

def lineRows(pSize):
    string = "|     |  "
    for i in range(pSize):
        print(string,end='')
    print("\n")

for i in range(size):
    dotRows(size)
    lineRows(size)
dotRows(size)
'''

#25 - guessing game two

'''
from random import *
nums = [0,100]
guesses = 0
while True:
    guess = randint(nums[0],nums[1])
    isGuess = str(input(f"Is {guess} your number? Type 'yes' if I'm right: "))
    guesses +=1
    if isGuess.lower() == "yes":
        break
    else:
        change = str(input("Doh! Was I too high? (type: 'too high') Or too low? (type: 'too low'): "))
        if change.lower() == 'too high':
            nums[1] = guess-1
        else:
            nums[0] = guess+1
print(f"Got it! Only took {guesses} try/tries!")
'''

#26 - check tic tac toe

'''
grid = [[2, 2, 0],
    [2, 1, 0],
    [2, 1, 2]]

#check diagonals

if (grid[0][0] == grid[1][1] == grid[2][2])or (grid[0][2] == grid[1][1] == grid[2][0]):
    print(f"{grid[0][0]} wins!")

#check rows
    
for i in range(3):
    if grid[i][0] == grid[i][1] == grid[i][2]:
        print(f"{grid[i][0]} wins!")
        
#check columns
        
for i in range(3):
    if grid[0][i] == grid[1][i] == grid[2][i]:
        print(f"{grid[0][i]} wins!")
'''

#27 - tic tac toe draw

'''
game = [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

goes = 0
player = 0
symbol = ''
print("An example coordinate is entering '0,0', which will place either an X or an O in the top left grid.")

while goes<9:
    if goes%2 == 0:
        player = 1
        symbol = "X"
    else:
        player = 2
        symbol = "O"
    
    while True:
        gridChoice = str(input(f"Player {player}'s go. Please enter your coordinate to place an {symbol} in: "))
        if game[int(gridChoice[0])][int(gridChoice[2])] == 0:
            break
        else:
            print("Something's already there! Try again.")
    
    goes+=1
    game[int(gridChoice[0])][int(gridChoice[2])] = symbol
    print(f"{game[0]}\n{game[1]}\n{game[2]}")
'''

#28 - max of three

'''
num1 = 4
num2 = 8
num3 = 12
biggest = 0

if num1>num2 and num1>num3: print(num1)
if num2>num3 and num2>num1: print(num2)
if num3>num2 and num3>num1: print(num3)
'''

#29 - tic tac toe game

'''
#check diagonals
def checkDiagonals():
    if (grid[0][0] == grid[1][1] == grid[2][2])or (grid[0][2] == grid[1][1] == grid[2][0]):
        if grid[0][0] != '*' and grid[1][1] != '*' and grid[2][2] != '*':
            print(f"{grid[0][0]} wins!")
            return 1
    else: return 0
    
#check rows
def checkRows():  
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            if grid[i][0] != '*' and grid[i][1] != '*' and grid[i][2] != '*':
                print(f"{grid[i][0]} wins!")
                return 1
        else: return 0
        
#check columns
def checkColumns():       
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] != '*' and grid[1][i] != '*' and grid[2][i] != '*':
                print(f"{grid[0][i]} wins!")
                return 1
        else: return 0

grid = [['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']]

goes = 0
player = 0
symbol = ''
print("An example coordinate is entering '0,0', which will place either an X or an O in the top left grid.")

while goes<9:
    if checkDiagonals() == 1 or checkRows() == 1 or checkColumns() == 1:
        break
    if goes%2 == 0:
        player = 1
        symbol = "X"
    else:
        player = 2
        symbol = "O"
    
    while True:
        gridChoice = str(input(f"Player {player}'s go. Please enter your coordinate to place an {symbol} in: "))
        if grid[int(gridChoice[0])][int(gridChoice[2])] == '*':
            break
        else:
            print("Something's already there! Try again.")
    
    goes+=1
    grid[int(gridChoice[0])][int(gridChoice[2])] = symbol
    print(f"{grid[0]}\n{grid[1]}\n{grid[2]}")
    if checkDiagonals() == 1 or checkRows() == 1 or checkColumns() == 1:
        break
'''


#30 - pick word

'''
from random import *
file = open("words.txt","r")
words = []
for i in file:
    words.append(i.replace("\n",""))
print(words[randint(0,len(words)-1)])
'''

#31 - guess letters

'''
from random import *
file = open("words.txt","r")
words = []

for i in file:
    words.append(i.replace("\n",""))

word = words[randint(0,len(words)-1)]
print(word)
display = len(word) * "-"
newdisplay = ''
used = []

while True:
    
    print(f"The current word is: {display}")
    
    if display.upper() == word.upper():
            print("You got it!")
            break
    
    while True:
        uInput = str(input("Please enter a letter to guess: "))
        
        if uInput.upper() in used:
            print("You've already guessed that!")
        
        else:
            if (len(uInput) == 1) and not(uInput.isnumeric()):
                break
     
    used.append(uInput.upper())
    
    if uInput.upper() in word.upper():
        
        newdisplay = ''
        
        for i in range(len(word)):
            
            if uInput.upper() == word[i].upper() and display[i] == '-':
                newdisplay += uInput
            else:
                newdisplay += display[i]
        
        display = newdisplay
    
    else:
        print("That's not a correct letter, try again!")
        
'''        

#32 - hangman game

'''
from random import *
file = open("words.txt","r")
words = []

for i in file:
    words.append(i.replace("\n",""))

word = words[randint(0,len(words)-1)]
print(word)
display = len(word) * "-"
newdisplay = ''
used = []
count = 0

while True:
    
    if count >=6:
        print(f"That's it! You did not get it. The word was {word}")
        break
    print(f"The current word is: {display}")
    
    if display.upper() == word.upper():
            print("You got it!")
            break
    
    while True:
        uInput = str(input("Please enter a letter to guess: "))
        
        if uInput.upper() in used:
            print("You've already guessed that!")
        
        else:
            if (len(uInput) == 1) and not(uInput.isnumeric()):
                break
     
    used.append(uInput.upper())
    
    if uInput.upper() in word.upper():
        
        newdisplay = ''
        
        for i in range(len(word)):
            
            if uInput.upper() == word[i].upper() and display[i] == '-':
                newdisplay += uInput
            else:
                newdisplay += display[i]
        
        display = newdisplay
    
    else:
        print("That's not a correct letter, try again!")
    count +=1
    print(f"You have {6-count} goes left. ")
'''

#33 - birthday dictionaries

'''
listInfo = []
benInfo = {"name":"Ben","birthday":"11/08/2007"}
listInfo.append(benInfo)
print("I know of:")
for i in listInfo:
    print(i["name"])
uInput = str(input("Whose name would you like to look up: "))
for i in listInfo:
    if i["name"].upper() == uInput.upper():
        print(i["birthday"])
'''

#34 - birthday json

'''
import json

info = {"name":"Ben","birthday":"11/08/2007"}

with open("info.json","w") as file:
    json.dump(info,file)
'''

#35 - birthday months

'''
from collections import Counter

sandwiches = ["chicken club", "pickle and onion", "roast beef", "chicken club", "pickle and onion", "roast beef", "chicken club"]
count = Counter(sandwiches)
print(f"There are lots of sandwiches. There are a total of {count['chicken club']} chicken club sandwhiches!")
'''

#36 - birthday plots

'''
from bokeh.plotting import figure, show, output_file
import json
from collections import Counter

numMonth = {'1':"January",'2':"February",'3':"March",'4':"April",'5':"May",'6':"June",'7':"July",'8':"August",'9':"September",'10':"October",'11':"November",'12':"December"}
x = []

y = []

ydone = []

file = open("bdays.json","r")

data = json.load(file)

keys = list(data["birthdays"][0].keys())

for i in range(len(data["birthdays"][0])):
    
    if ((data["birthdays"][0][(keys[i])]).split("/")[0])[0] == "0":
        
        month = numMonth[str(((data["birthdays"][0][(keys[i])]).split("/")[0])[1])]
    
    else:
        
        month = numMonth[str((data["birthdays"][0][(keys[i])]).split("/")[0])]
    
    x.append(month)

for i in range(len(list(Counter(x).items()))):
    y.append(list(Counter(x).items())[i][1])

output_file("plot.html")
xCats = ["January", "February", "March","April","May","June","July","August","September","October","November","December"]

plot = figure(x_range=xCats)
plot.vbar(x=x, top=y, width=0.5)

show(plot)
'''

#37 - functions refactor

'''
No activities for this exercise.
'''

#38 - f strings

'''
name,age = str(input("Please enter your name: ")),int(input("Please enter your age: "))
message = f"\nHello {name}, you are {age} years old and will turn 100 in around {(2024)+(100-age)}\n"
print(message)
num = int(input("How many more times shall we show you that message?"))
for i in range(num): print(message)
'''

#39 - character input datetime

'''
from datetime import *

name,age = str(input("Please enter your name: ")),int(input("Please enter your age: "))
now = datetime.now()
message = f"\nHello {name}, you are {age} years old and will turn 100 in around {(now.year)+(100-age)}\n"
print(message)
num = int(input("How many more times shall we show you that message?"))
for i in range(num): print(message)
'''

#40 - error checking

'''
import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
    while True:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess > 0 and guess <10:
            break
        else:
            print("That was not in the specified range. Try again")
    
    number_of_guesses += 1
    if guess == number:
        break
print(f"You needed {number_of_guesses} guesses to guess the number {number}")
'''