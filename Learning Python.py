#Python Traning

for az in range(ord('a'), ord('z')+1): print(chr(az))


print("I Love Python")
print("I Love Programming")

# -------------------------------
# Informations About File
# License
# Who Created The File
# When The File Created
# Why The File Created
# Write Beside The Programming Line
# Write Before The Programming Line
# Prevent Code From Run
# --------------------------------
# This is Comment
print("I Love Python")  # This is Inline Comment
print("Programming")  # I Used This Method Because of Bla Bla Bla
print("Programming")  # If You Used Test Method Will Through Error

"""
This is
Not
Multiple
Line
Comments
"""

# --------------------------------------------------------------------------#
# type()
# All Data in Python is Object
# ----------------------------

print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))  # float => Floating Point Number
print(type(1.950950))  # float => Floating Point Number
print(type(-100.9595))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

print(type([1, 2, 3, 4, 5]))  # list => List

print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

print(type(2 == 2))  # bool => Boolean


# --------------------------------------------------------------------------
# -- Variables --
# ---------------
# Syntax => [Variable Name] [Assignment Operator] [Value]
#
# Name Convention and Rules
# [1] Can Start With (a-z A-Z) Or Underscore
# [2] You Cannot With Num Or Special Characters
# [3] Can Include (0-9) Or Underscore
# [4] Cannot Include Special Characters
# [5] Name is Not Like name [ Case Sensitive ]
# --------------------------------------

name = "Ahmed Elmahdy"  # Single Word => Normal
myName = "Ahmed Elmahdy"  # Two Words => camelCase
my_name = "Ahmed Elmahdy"  # Two Words => snake_case

print(name)
print(myName)
print(my_name)

# --------------------------------------------------------------------------#
# -- Variables --
# ---------------
# Source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language
# Compilation : Translate Code Before Run Time
# Run-Time : Period App Take To Executing Commands
# Interpreted : Code Translated On The Fly During Execution
# --------------------------------------------------------

# Reserved Words
help("keywords")

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)


# --------------------------------------------------------------------------#
# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Value
# ----------------------------

# Back Space
print("Hello\bWorld")  # Will Remove o

# Escape New Line + Back Slash
print("Hello \
I Love \
Python")

# Escape Back Slash
print("I Love Back Slash \\")

# Escape Single Quote
print('I Love Single Quote \'Test\' ')

# Escape Double Quotes
print("I Love Double Quotes \"Test\" ")

# Line Feed
print("Hello World\nSecond Line")

# Carriage Return
print("123456\rAbcde")

# Horizontal Tab
print("Hello\tPython")

# Character Hex Value
print("\x41\x68\x6D\x65\x64\x20\x45\x6C\x4D\x61\x68\x79")


# ----------------------------------------------------------------------------#
# -- Concatenation --
# -------------------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)

full = msg + " " + lang
print(full)

e = "First \
Second \
Third"

f = "A \
B \
C"

print(e + "\n" + f)

#print("Hello " + 1)  # Error


# -----------------------------------------------------------------------------#
# -- Strings --
# -------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)

myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"

print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second 'Test' "Test"
Third'''

myStringSix = """First
Second "Test" \\\ 'Test'
Third"""

print(myStringFive)
print(myStringSix)

# ---------------------------------------------------------------------------#
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )

myString = "I Love Python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1])  # Index -1 => First Character From End
print(myString[-6])  # Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data

print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data

print(myString[::2])
print(myString[::3])


# ---------------------#---------------------#---------------------# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

g = "ahmed"

print(g.upper())

# lower()

h = "Ahmed"

print(h.lower())


# ------------------------------------------------------------------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()

aa = "I Love Python and PHP and MySQL"
print(aa.split())

bb = "I-Love-Python-and-PHP-and-MySQL"
print(bb.split("-"))

cc = "I-Love-Python-and-PHP-and-MySQL"
print(cc.split("-", 3))

dd = "I-Love-Python-and-PHP-and-MySQL"
print(dd.rsplit("-", 3))

# center()

ee = "Ahmed"
print(ee.center(9))  # Spaces
print(ee.center(9, "#"))  # Hashes
print(ee.center(15, "@"))  # @

# count()

ff = "I Love Python and PHP Because PHP is Easy"
print(ff.count("PHP"))  # 2 PHP Words
print(ff.count("PHP", 0, 25))  # Only One PHP Word

# swapcase()

gg = "I Love Python"
hh = "i lOVE pYTHON"

print(gg.swapcase())
print(hh.swapcase())

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()

j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))


# ------------------------------------------------------------------------------
# -- Strings Methods --
# ---------------------

# index(SubString, Start, End)

a1 = "I Love Python"
# print(a1.index("P"))  # Index Number 7
# print(a1.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5))  # Through Error

# find(SubString, Start, End)

b1 = "I Love Python"
print(b1.find("P"))  # Index Number 7
print(b1.find("P", 0, 10))  # Index Number 7
print(b1.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char) adding space or # after or before

c1 = "Ahmed"
print(c1.rjust(10))
print(c1.rjust(10, "#"))

d1 = "Ahmed"
print(d1.ljust(10))
print(d1.ljust(10, "#"))

# splitlines()

e1 = """First Line
Second Line
Third Line"""

print(e1.splitlines())

f1 = "First Line\nSecond Line\nThird Line"

print(f1.splitlines())

# expandtabs()

g1 = "Hello\tWorld\tI\tLove\tPython"
print(g1.expandtabs(2))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "Ahmed"
eight = "Ahmed"
nine = "Ahmed--ElMahdy100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x1 = "AaaaaBbbbbb"
y1 = "AaaaaBbbbbb111"
print(x1.isalpha())
print(y1.isalpha())

u1 = "AaaaaBbbbbb"
z1 = "AaaaaBbbbbb111"
print(u1.isalnum())
print(z1.isalnum())

# ----------------------------------------------------------------------------

# -- Strings Formatting --
# ------------------------

name1 = "Ahmed"
age = 30
rank = 10

print("My Name is: " + name1)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: %s" % "Ahmed")
print("My Name is: %s" % name1)
print("My Name is: %s and My Age is: %d" % (name1, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name1, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "Ahmed"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber)

# Truncate String

myLongString = "Hello Peoples This is Ahmed, I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString)

# ----------------------------------------------------------------------------
#-- Strings Formatting New Ways 
# -------------------------------

name2='Ahmed'
age=36
rank=10
print("My Name is:"+ name2)
# print("My Name is:" + name2 +"and My Age is: " + age) #type Error 
 
print("My Name is: {}" .format("Ahmed"))
print("My Name is: {}" .format("name2"))

# print("My Name is: %s" and My Age is: %d" % (name2, age))
# print("My Name is: %s" % "Ahmed")
# print("My Name is: %s" % "Ahmed")

# {:s} => String
# {:d} => Number
# {:f} => Float
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

print("Massage is {}".format(myLongString))
print("Massage is {:.5s}".format(myLongString))
print("Massage is {:.13s}".format(myLongString))

# Format Money ------------------------------------------------------------------------------------------
myMoney= 54442009966
print("My Mony in bank is:{:d}".format(myMoney))  # we can type {} without :d  it will works fine 
print("My Mony in bank is:{:_d}".format(myMoney))
print("My Mony in bank is:{:,d}".format(myMoney))


# ReArrange Items ------------------------------------------------------------------------------------------

ab, bc, de ="One" , "Two", "Three"
print("Hello {} {} {}".format(ab,bc,de))
print("Hello {1} {2} {0}".format(ab,bc,de)) 
print("Hello {2} {1} {0}".format(ab,bc,de))


q, w, r= 10, 20, 30 
print("Hello {} {} {}".format(q,w,r))
print("Hello {1:d} {2:d} {0:d}".format(q,w,r)) 
print("Hello {2:.2f} {1:.4f} {0:.5f}".format(q,w,r))


# Formating in Version 3.6+

myname= "Ahmed"
MyAge= 36

print("My Name is :{myname} and My Age is :{MyAge}")  # it will print My Name is :myname and My Age is : MyAge
print(f"My Name is :{myname} and My Age is :{MyAge}") # We just need to add f before "" => f""


#-------------------------------------------------------------------------------------------------
# -- Numbers -- 

#Intger 
print(type(10))
print(type(100))
print(type(-10))
print(type(-110))

#-- Float 

print(type(1.500))
print(type(100.99))
print(type(0.99))
print(type(-0.99))

#--Complex 

mycomplexnumber=5+6j
print(type(mycomplexnumber))
print("Real Part Is: {}".format(mycomplexnumber.real))
print("Imaginary Part Is: {}".format(mycomplexnumber.imag))

# [1] You can convert from int to float or complex 
# [2] You can convert from float to int or complex 
# [3] You cannot convert from complex to Any type   

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10.5+0j)
# print(int(10.5+0j)) TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'


#-------------------------------------------------------------------------------------------------
# -- Arithmetic Operators ---
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# Addition [+]
  
print(10+30) #40
print(-10+30) #20
print(1.2+2) #3.2
print(1.3+3.6) #4.9


# [-] Subtraction

print(50-20) #30
print(-50-20) #70
print(-50- -20) #-30
print(-5.60-2.40) #3.20

# Multiplication [*]

print(5+10*100) #1005
print((5+10)*100) #1500

#  Division [/]

print(100/20) # 5.0
print(int(100/20)) # 5.0

# [%] Modulus  باقي القسمة 

print(8%2) # 0  
print(9%2) # 1
print(20%5) # 0
print(22%5) # 2

# [**] Exponent

print(2**5) #32 = print(2*2*2*2*2)32
print(5**4) #625 =print(5*5*5*5)

# [//] Floor Division ==> the same to # [%] Modulus  باقي القسمة 

print(100//20) #5
print(110//20) #5
print(119//20) #5
print(120//20) #6
print(125//20) #6
print(131//20) #6
print(140//20) #7

#-------------------------------------------------------------------------------------------------
# -- Lists --
#------------

myawesomelist=['one', 'two', 'three', 1, 100.5, True]
print(myawesomelist) #whole List
print(myawesomelist[1]) # one
print(myawesomelist[-1]) # true
print(myawesomelist[-3]) # 1

#slicing 
print(myawesomelist[1:4]) # => ["two", "one", 1]
print(myawesomelist[:4]) # from  the begining to the index 4 => ['one, two, three', 1, 100.5, True]
print(myawesomelist[1:]) # from  the index 1 to the end of the list => [1, 100.5, True]


print(myawesomelist[::1]) #normal print => ['one, two, three', 1, 100.5, True]
print(myawesomelist[::2]) # step 2 ignore idex and print index 
# print(myawesomelist[150]) # error index not found

print(myawesomelist)
myawesomelist[1] = 2
myawesomelist[-1] = False
myawesomelist[0:3] = ['A','B','C']  # editing the list index  slice by slice 
myawesomelist[0:3] = ['A','B']
print(myawesomelist)

#--------------------------------------------------------------------------------------------

# append() adding new elment to list 
myfriends= ["omar", "ahmed", "mahdy"]
myoldfriends= ["sameh", "saad", "nooh"]
myfriends.append("Alaa")
myfriends.append(100)
myfriends.append(100.200) #bolum value 
myfriends.append(True)
myfriends.append(myoldfriends) # it will be added as one eliment 


print(myfriends)
print(myfriends[2])
print(myfriends[6])
print(myfriends[7])
print(myfriends[7][2]) #[7]the second list [2] the second eliment of this list 


# extend() 
listA=[1, 2, 3, 4]
listB=['A', 'B', 'C', 'D']
listC=['one', 'two', 'three', 'four']
print(listA)
print(listB)
print(listC)
# listA.extend(listB)
listA.extend(listC)
print(listA)


# Remove()

xy=[1,2,3,4,5,'mahdy',True, 'omar', 'mahdy']
xy.remove("mahdy")
print(xy)


# Sort()
zyx=[1,2,100,120,-10,17,27]
print(zyx)
zyx.sort()
print(zyx)
zyx=[1,2,100,120,-10,17,27]
zyx.sort(reverse=True)
# zyx=[1,2,100,120,-10,17,27,"Ahned"]
# zyx.sort(reverse=True) #  not supported between instances of 'int' and 'str' 
print(zyx)

zyx=['a','z','c']
zyx.sort(reverse=True)
print(zyx)

# reverse()
newlist=[10,1,9,100,"Ahmed",100]
newlist.reverse()
print(newlist)

#clear()
list1=[1,2,3,4]
list1.clear()
print(list1)

#copy()
list2=[1,2,3,4]
list3=list2.copy()

list2.append(5)

print(list2) # Main list 
print(list3) # Copied list 

# Count()
countlist=[1,2,3,4,5,5,6,9,6,7,8,9,1,10,10,]
print(countlist.count(1))

# index()
indexlist=['ahmed','ali','anas','alaa','omr'] 
print(indexlist.index('omr'))

# insert()  like append 
insertlist=[1,23,4,5,6,7,79,74,22,11,47]
insertlist.insert(5,'Test')
insertlist.insert(0,'Test')
insertlist.insert(-1,'Test')
print(insertlist)

# pop()

poplist=[1,2,3,4,5,'A','B']
print(poplist.pop(5)) # it will retreve with eliment index number


#------------------------------------------------------------------------------------------------
#-- Tuple()
#[1] Tuple items are enclosed in parentheses.
#[2] You can Remove The Parentheses if you want.
#[3] Tuple are ordered, To use indes to access item
#[4] Tuple are immutable => You can add or Delete
#[5] Tuple Items not unique 
#[6] Tuple can hava different data types
#[7] Operators used in strings and lists available in Tuple
#---------------------------------------
#Type Syntax  & type Test 
myawesometupleone=('ahmed',"ali",'omar')
myawesometupletwo='ahmed',"ali",'omar'

print(myawesometupleone)
print(myawesometupletwo)

print(type(myawesometupleone))
print(type(myawesometupletwo))


# Tuple Indexing 
myawesometuplethree= 1,2,3,4,5
print(myawesometuplethree[0])
print(myawesometuplethree[3])
print(myawesometuplethree[-2])

# Tuple assign values 
myawesometuplefour= 1,2,3,4,5
# myawesometuplefour[2] ="Three"
# print(myawesometupletfour) # tuple' object does not support item assignment


# Tuple items 
myawesometuplefive= "ali", "nadia", 'alaa',1,2,3,12.25,True
print(myawesometuplefive[1])
print(myawesometuplefive[-1])

# Tuple with one Eliment how to define it as a tuple with only one eliment. we can add , after the eliment 
mytuple1= 'osama',
mytuple2= 'ali',

print (mytuple1)
print (mytuple2)

print (type(mytuple1))
print (type(mytuple2))

print (len(mytuple1)) # to display the number of the elements in the tuple by using len function.
print (len(mytuple2)) # to display the number of the elements in the tuple by using len function.


# Tuple concatenation 

tuple11= 1,2,3,4
tuple22= 5,6
tuple33=tuple11+tuple22 
tuple44=tuple11+('a','b')+tuple22 # adding some items to two tuple

print(tuple33)
print(tuple44)

# Tuple , list , string repeat (*)

string1='ahmed'
listy= [1,2]
tupley= 'a','b','c'

print (string1*6)
print (listy*6)
print (tupley*6)

# Method => Count()

tuplex=2,2,44,23,5,66,78,88,44,23,44
print(tuplex.count(44))

# Method => index() with formating.

tupleb=(1,2,3,4,5,6,7,8,9)
print(tupleb.index(4))
# print("The Positon is :"+tupleb.index(7)) # Error 
print("The Positon is :{:d}".format(tupleb.index(7))) 
print(f"The Positon is :{tupleb.index(7)}")

# Tuple Destruct 
tuple0= ("A","B","C","D")
x2,y2,z2 = 'a','b','c'
print(x2,y2,z2)

x2,y2,z2,_, = tuple0 # _ will ignore this varuable position 
print(x2,y2,z2)


#------------------------------------------------------------------------------------------------
#-- Set () ---
#[1] set items are enclosed in curly braces 
#[2] set items are not oredered and not indexed 
#[3] set indexing and slicing can'y be done 
#[4] set has only immutable data type (number, strings, tuples) list and dict are not 
#[5] set item is uniqe 
#---------------------------------------

mysetone= {"ahmed","osama","omar", 100}
print (mysetone)
# print(mysetone[0])

# # Slicing Can't be done on set ()
# mysetwo= {1,2,3,4,5,6}
# print(mysettwo[0:3])


# has only immutable data type 
# mysetthree={"omar","ahmed",100, 100.5,True [1, 2, 3]} # unhashable type: 'list' [1, 2, 3] list not hashable type 
mysetfour={"osama", 100, 100.5, True, (1,2,3)} #convert list to tuple [1, 2, 3] > (1,2,3)

print (mysetfour)

#set item is uniqe 
mysetfour={1,2,"omar","one",1,100.5}
print(mysetfour)


#------------------------------------------------------------------------------------------------
#-- Set Method ---
#-------------------------

# clear()
aaa= {1,2,3}
aaa.clear()
print(aaa)

# Union()

bb={'one','two','three'}
cc={'1','2','3'}
dd={'Zero','Cool','amazing'}

print(bb|cc)
print(bb.union(dd,cc))


# add()

cc={'1','2','3','4'}
cc.add(5)
cc.add(6)
print(cc)

#copy()

e={1,2,3,4}
f=e.copy()  #shalow copy 
print(e)
print(f)

# remove()
g= {1,2,3,4}
g.remove(1)
# g.remove(5) # it will prompet error
print(g)

# discard()
h= {1,2,3,4}
h.discard(1)
h.discard(5) 
print(h)

# pop()

i={'a',True, 1, 2, 3, 4, 5}
print(i.pop())

# update()

j= {1,2,3}
k={1,'a','b',2}
j.update(k) 
j.update(['html','css']) 
print(j)








































