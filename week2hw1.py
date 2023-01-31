#Excercise 4

#Cube Number Test... Print out all cubed numbers up to the total value 1000.
#Meaning that if the cubed number is
# over 1000 break the loop.

for alist in range(1,11):
    print(alist,alist**3)
    




#Excercise 4
#Get first prime numbers up to 100:

for number in range(1,101):
    if number == 2:
        print(2)
    if number % 2 == 0:
        continue
    if number == 3:
        print(3)
    if number % 3 == 0:
        continue
    if number % 5 == 0:
        continue
    # if number % 6 == 0:
    #     continue
    if number == 7:
        print(7)
    if number % 7 == 0:
        continue
  
    print(number)









#Excercise 3
#Take in a users input for their age, if they are younger than 18 print kids, 
#if they're 18 to 65 print adults, else print seniors:


age = int((input("What is your age?")))
if age <18:
    print('kids')
elif age == 18:
    print('adults')
elif age <=65:
    print('adults')
else: print('seniors')
