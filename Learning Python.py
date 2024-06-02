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
print("\x4F\x73")


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

c1 = "Osama"
print(c1.rjust(10))
print(c1.rjust(10, "#"))

d1 = "Osama"
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

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

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



