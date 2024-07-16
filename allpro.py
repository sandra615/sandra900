##To print the right angled triangle with * symbol
a=int(input("Enter the number:"))
for i in range(1,a+1):
    print('*' * i)
##To type the message
def typethemessage():
    message='HAPPY BIRTHDAY SHALINI'
    print(message)
typethemessage()
##list to dictionary conversion
l=[1,2,3,4,5,6,7,8,9,10]
d={i:i+1 for i in l}
print(d)
##print the message 5 times
for _ in range(5):
    print("Hello, World!")
a=int(input('enter the number'))
##to check whether the number is prime or not
if a>1:
    for i in range(2,a):
        if (a%i==0):
            print('the number is not a prime number')
            break
        else:
            print('the number is a prime number')
else:
    print('the number is not a prime number')
##to find the factorial
def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
    a=int(input('enter the number'))
    output=fact(a)
    print('factorial of the entered number is',output)
##for invalid input print the output as invalid input
try:
    a = int(input("Enter a number: "))
    print("Input is a valid integer:")
except ValueError:
    print("Invalid datatype. Please enter a valid integer.")
