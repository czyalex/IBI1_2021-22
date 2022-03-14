# What does this piece of code do?
# Answer: get random number for 10 times and print the last time's random number

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0  #Set the original variables that control the loop
while progress<10: # meaning that this loop will cycle  itself for 10 times
	progress+=1  # meaning that this loop will cycle  itself for 10 times
	n = randint(1,100)   # find the random number and out put as int type

print(n)

