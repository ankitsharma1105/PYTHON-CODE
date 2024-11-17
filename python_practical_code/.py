#odd and even 
num = int(input("enter the number = "))
if num % 2 ==0:
    print("even")
else:
    print("odd")

#100 years old
name = input("enter the name :")
birth_year = int(input("enter the birth year :"))

from datetime import datetime
current_year = datetime.now().year

year_when_100 = (current_year - birth_year)+100

print(f"{name}  you will turn 100 years old in the year {year_when_100 }")

#Armstrong and Palondrome 

import math
num = input("enter the number = ")
no_digit = len(num)
num = temp = int(num)
Armstrong = 0
Palondrome =0
while(num !=0): 
    no = num%10 
    Armstrong = int(Armstrong+math.pow(no,no_digit))
    Palondrome = Palondrome*10+no
    
    if(Armstrong==temp):
        print("armstron number hai")
    else:
        print("Not armstrong number hai")

    if (Palondrome==temp):
        print("palondrome number")
    else:
        print("not palondrome number")

# factorial 
def factorial(n):
    if n == 0:
        return 1
    else:
       return n * factorial(n - 1)
print(factorial(5))

# 1 char
def isVowel(char):
    input = char.lower()
    vowel ="aeiou"
    if(len(input)>1):
        return print("error  a charcter more then 1")
    else:
        return print(input in vowel)
    
char= input("enter the only one char :")
isVowel(char)

#list and string
def compute_length(list_or_string):
  if not isinstance(list_or_string ,(list ,str)):
    print("input the must the strng")
    return print(len(list_or_string))
compute_length("ankit")
compute_length([2343565])

#fabonacci series
num = int(input("enter the number :"))
num1= 0
num2= 1

for i in range(num):
    print(num1)
    next = num1+num2
    num1 = num2
    num2 = next
#letters
def letters(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        return True
    
    str = input("enter str :")
    if (letters(str) ==True):
        print("yes")
    else:
        print("no")

#Histogrma
def histogram(int_list):
    for num in int_list:
        print(* num)
    histogram(4,9,7)

# less than 5 only given number
a = [1,2,2,3,3,4,5,67,86,234,2,3,5,]
for element in a:
   if element < 5:

      print(element)

# 2 list one is false common 
def common_number(list1 , list2):
    for item in list1 :
        if item in list2:
            return True
        return False
    
list1 =[ 1,2,3,4]
list2 = [3,6,7,8]

# remove el 
def remove_element(lst):
    if i not in (0,2,4,5):
        return [lst[i] for i in range(len(lst)) if i in lst(0,2,4,5)]
    my_list = ['a' ,'b' ,'c','d' ,'e','f' ,'g','h']
    updated_list = remove_element(my_list)
    print(updated_list)