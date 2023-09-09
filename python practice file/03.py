# def check_quotes(z):
#     quote="today's high temperature will be 75 degrees."
#     z1=quote.split(" ")
#     list_1=[]
#     for i in z1:
#         list_1.append(i)
#         list_2=[]
#     z2=z.split(" ")
#     for j in z2:
#         list_2.append(j)
#     set1=set(list_1)
#     set2=set(list_2)
#     x= set1.issubset(set2)
#     return x
# f=open("datafile.txt",'r')
# z=f.read()
# f.close()
# print(z)
# print(check_quotes(z))

# def count_letters(line):
#     line=line.lower()
#     letters={}
#     for i in line:
#         if i in letters:
#             letters[i]+=1
#         else:
#             letters[i]=1
#     return list(letters.items())
# with open('datafile.txt')as f:
#     line=f.readline().strip()
#     letter_count=count_letters(line)
#     print(letter_count)
