
# Q1
# Write a code to get the input in the given format and print the output in the given format.
#
# Input Description:
# A single line contains a string.
#
# Output Description:
# Print the characters in a string separated by comma.
#
# Sample Input :
# guvi
#
# Sample Output :
# g,u,v,i

c = input()                    # Q 1 CODE
d = ",".join(c)
print(d)                       # Q 1 CODE

# Q2
# Write a code to get the input in the given format and print the output in the given format
#
# Input Description:
# First-line indicates two integers separated by space. Second-line indicates three integers separated by space. Third-line indicates three integers separated by space
#
# Output Description:
# Print the input in the same format.
#
# Sample Input :
# 2 5
# 2 5 6
# 2 4 5

a, b = map(int, input().split())                               # Q 2 CODE


x, y, z = map(int, input().split())

r, s, t = map(int, input().split())


print(a,b)
print(x,y,z)
print(r,s,t)                                                        # Q2 CODE

# Q3
# You will be provided with a number. Print the number of days in the month corresponding to that number.
#
# Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".
#
# Input Description:
# The input is in the form of a number.
#
# Output Description:
# Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

A = int(input())                                                                # Q3 CODE

if A == 1 or A==3 or A==5 or A==7 or A==8 or A==10 or A==12:
    print("{0}". format(31))
elif A ==4 or A==6 or A==9 or A==11:
    print ("{0}". format(30))

elif A == 2:
    print("{0}".format(28))
else:
    print ("Error")                                                            # Q3 CODE


# Q4
# You are provided with a number, "N". Find its factorial.
#
# Input Description:
# A positive integer is provided as an input.
#
# Output Description:
# Print the factorial of the integer.

N =int(input())                                                                 # Q4 CODE
for i in range(1,N):
    N=N*i
print(N)                                                                        # Q4 CODE

# Q5
# Let "A"  be a string. Remove all the whitespaces and find it's length.
#
# Input Description:
# A string is provide as an input
#
# Output Description:
# Remove all the whitespaces and then print the length of the remaining string.

c = input()                                                                 # Q5 CODE
d =""

for char in c:
    if char.isalpha():
        d = char + d

print(len(d))                                                                  # Q5 CODE

# Q6
# Write a code get an integer number as input and print the sum of the digits.
#
# Input Description:
# A single line containing an integer.
#
# Output Description:
# Print the sum of the digits of the integer.

n=int(input())                                                                  # Q6 CODE
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10

print(f"{tot}")                                                                 # Q6 CODE

# Q 7
# Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.
#
# Input Description:
# A single line containing 2 integers separated by space.
#
# Output Description:
# Print the HCF of the integers.

a, b = map(int, input().split())                                              # Q7 CODE
d= []

if 0<a<b:
    for i in range (1,a+1):
        if a%i ==0 and b%i ==0:
            d.append(i)
    print(max(d))

if 0<b<a:
    for i in range (1,b+1):
        if a%i ==0 and b%i ==0:
            d.append(i)
    print(max(d))                                                             # Q7 CODE


# Q8
# You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.
#
# Input Description:
# First line contains a number ‘n’. Then next line contains n space separated numbers.
#
# Output Description:
# Print the difference of indices of largest and smallest array

n = int(input())                                                            # Q8 CODE
val = input()
c = list(map(int,val.split(" ")))
if len(c) == n:
    i = c.index(max(c))-c.index(min((c)))
    print(i)                                                                # Q8 CODE

# Q9
# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.

z = input()                                                                 # Q9 CODE
r,s = map(int,z.split(" "))

a = input()
b = map(int,a.split(" "))
p = list(b)

if len(p) == r:

    if s in p:
        print("yes")
    else:
        print("no")                                                          # Q9 CODE

# Q10
# You are given a string.Your task is to print only the consonants present
# in the string without affecting the sentence spacings if present. If no consonants are present print -1

n = input()                                                                    # Q10 CODE
s = "aeiou"
str = ""
for char in n.casefold():
    if char not in s:
        str += char

print(str)                                                                     # Q10 CODE


