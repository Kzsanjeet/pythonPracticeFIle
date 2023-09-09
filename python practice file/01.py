# def exchange():
#     """Write a program that reads a text file named original_text, and writes
# every other line, starting with the first line, to a new file named new_text."""
#     with open('original_text','r') as r1:
#         file=r1.readlines()
#         lines=file
#         print("original file",lines)
#     with open('new_text.txt','w') as n:
#         files=n.write(lines)
#     with open('new_text.txt','r') as r:
#         overwrite=r.read()
#         print(overwrite)

# exchange()


# def count():
#     """count the number of e from the original text."""
#     with open("original_text.txt",'r')as f:
#         file=f.readlines()
#         print(file)
#         count=0
#         for i in file:
#             if i== 'e':
#                 count+=1
#         print(count)

# count()
