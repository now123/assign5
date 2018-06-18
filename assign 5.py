#QUE 1-
year = int(input("Enter a year: "))
if (year%4==0):
    print ("it's leap year ")
else:
    print ("not a leap year")

#QUE 2-
a = input ("enter the length")
b = input  ("enter the breadth")
if (a == b):
    print ("it is a square")
else:
    print ("it's a rectangle")

#QUE 3-
a = input("frst age")
b = input ("scnd age")
c = input ("third age")
if (a>b) and (a>c):
    print ("a is elder")
elif (b>c) and (b>a):
   print ("b is elder")
else:
  print ("c is elder")
if (a<b) and (a<c):
  print ("a is younger")
elif (b<a) and (b<c):
  print ("b is y0unger")
else:
  print("c is younger")

#QUE 4-
a = int(input ("enter the no. "))
if (a<=50):
  print ("no prize")
elif (a==51 and a<=150):
  print("congo! you have won wooden dog")
elif (a==151 and a<=180):
  print("congo! you have won book")
elif (a==181 and a<=200):
  print("congo! you have won choclate")
else:
  print ("sorry! no prize time")

#QUE 5-
x= int (input("enter price"))
a = x*0.1
if(a>1000):
  a=x*100-x*0.1*100
print(a)