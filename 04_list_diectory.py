import  os
print(os.listdir())

# class trip:
a="ankita"

def myfu():
        print("function " + a)

def claa():
    c="akshat"
    print(c)

claa()
myfu()

a=6
b=4
sum=a%b
print(sum)

a=input("enter no")
print(type(a))
c=int(input("enter no"))
print(type(c))

a=34
b=80
c=a>b
print(c)
# wap find avg of the two no entered by the user

c=int(input("enter 1st no"))
d=int(input("enter 1st no"))
e=(c+d)/2
print(e)

# wap to calculate square of a no entered by the user
c=int(input("enter  no"))
d=c**2
print(d)

# wap to reverse of string
a="ankita"
c=a[::-1]
print("reverse string",c)
# string functionk
a="anita"
c="judhef"
# c=a+c
print("a".join(c))
print(len(a))
print(a.upper())
print(a.split(":"))
print(a.count("a"))

# wap to display a user entered name followed by good afternoon using input function

a=input("enter name")
print(a,"good afernoon")

# w a p to fill in a letter template given below with name and date

letter ='''Dear </name/>,
you are selected!

Date:</Date/>
'''
name=input("enter name\n")
date=input("enter date\n")
letter =letter.replace("</name/>",name)
letter=letter.replace("</Date/>",date)
print(letter)


