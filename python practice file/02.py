# print("hello")
# try:
#     print(2/0)
# except:
#     print('program is sucessful')
# print('Hello')


# def divide(x,y):
#     if y==3:
#         raise ValueError("cannot divide by 3.")
#     return x/y
# try:
#     result=divide(5,0)
#     print(result)
# except Exception as e:
#     print(e)
# numerator=10
# denominator=0
# try:
#     result=numerator/denominator
#     print(result)
# except Exception as e:
#     print(f"The error{e}")

def div(num1,num2):
    try:
        result=num1/num2
    except ZeroDivisionError:
        print("Error:cannot divide by zero")
    else:
        print(result)
# using finally:

# div(2,0)
def div(num1,num2):
    try:
        result=num1/num2
    except ZeroDivisionError:
        print("Error:cannot divide by zero")
    finally:
        print(result)

div(2,0)