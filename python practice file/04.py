
num  =1
def calcu():
    """write a program that claculates the sum of first n natural number"""
    
    
    global num
    num = num+1

    if num <5:
        calcu()
        print(num)  

calcu()
n=0
def calcu():
    global n
    n=int(input("Enter the number:"))
    for i in n:
