"""
distribution.py
Author: Jeff
Credit: Google

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

line_ = input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "{0}" is: '.format(line_))
line = line_.lower()
alphabet = string.ascii_lowercase
n = 1
lst = []
qlst = []
while n <= 26:
    q = line.count("{0}".format(alphabet[n - 1]))
    if q != 0:
        lst.append(alphabet[n - 1])
        qlst.append(q)
    n += 1
tupl = zip(lst,qlst)
lnum = len(qlst)
qlst.sort()
print(lst)
print(qlst)
print(lnum)
print(tupl)
while lnum > 0:
    m = qlst[lnum - 1]
    while m > 0:
        print()
        m -= 1
    
    lnum -= 1
print(len("Haha, "))
    

        


