'''Write a menu driven python program to perform following string operations.(Write functions)

String Concatenation
String Reverse
String Compare
String length
Palindrome
Case Change
'''
def string_len(str1):
    str_l = len(str1)
    print("Lenght of string :",str_l)
    return str_l
def string_com(str1,str2):
    if str1 == str2 :
        print("Both String are equal")
    else :
        print("Both String are not equal")
    return str1 ,str2
def string_pal(str1):
    str_r = str1[::-1]
    if str1 == str_r :
        print("This is palindrome")
    else:
        print("This is not palindrome")
''' -----> What was wrong in this comment code
def string_rev(str1):
    r_str = ""
    for i in str1:
        r_str =  r_str + i
    return r_str
'''
def string_r(str1):
    r_string = str1[::-1]
    return r_string
def string_cas(str1):
    print('''Menu
    1)Upper Case
    2)Lower Case
    ''')
    sel_0 = int(input("Enter the correct SR No:"))
    if sel_0==1:
        print(str1.upper()) 
    if sel_0==2:
        print(str1.lower())
def string_conca(str1,str2):
    str_con = str1 + str2
    print(str_con)
    return str1 ,str2

print( '''Menu
1)String Concatenation
2)String Reverse
3)String Compare
4)String length
5)Palindrome
6)Case Change ''')
sel_1 = int(input("Enter correct SR No:"))
if sel_1 == 1:
    a = input("Enter the First String:")
    b = input("Enter the Second String:")
    string_conca(a,b)
elif sel_1 == 2:
    a = input("Enter the String:")
    print(string_r(a))
elif sel_1 == 3:
    a = input("Enter the First String:")
    b = input("Enter the Second String:")
    string_com(a,b)
elif sel_1 == 4:
    a = input("Enter the String:")
    string_len(a)
elif sel_1 == 5:
    a = input("Enter the String:")
    string_pal(a)
elif sel_1 == 6:
    a = input("Enter the String:")
    string_cas(a)
else:
    print("Please Enter valid Number")
