
#You and your date are trying to get a table at a restaurant.
#The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is
#the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no,
#1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes).
#With the exception that if either of you has style of 2 or less, then the result is 0 (no).
#Otherwise the result is 1 (maybe).

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1

# My first try is just a simple for loop checking to see if you are a definite no or yes, i shortened the loop using or.
# From my short googling it seems this anwser is pretty decent. But I would assume you could do it in less code and have a better runtime
def date_fashion(you, date):
  if you <= 2 or date <= 2:
   return 0
  elif you >= 8 or date >=8:
   return 2
  else:
   return 1


#Using the Python language, have the function ArrayAdditionI(arr) take 
#the array of numbers stored in arr and return the string true if any
#combination of numbers in the array can be added up to equal the largest
#number in the array, otherwise return the string false. For example: if
#arr contains [4, 6, 23, 10, 1, 3] the output should return true because
#4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all
#the same elements, and may contain negative numbers.



def ArrayAdditionI(arr):

  # code goes here
  sort = arr.sort()
  largest = arr.pop()
  sumarr = sort.sum()
  if sumarr > largest:
    return true
  else:
    return false
