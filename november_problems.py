#Using the Python language, have the function Consecutive(arr) take the array of integers
#stored in arr and return the minimum number of integers needed to make the contents of arr
#consecutive from the lowest number to the highest number. For example: If arr contains [4, 8, 6]
#then the output should be 2 because two numbers need to be added to the array (5 and 7) to
#make it a consecutive array of numbers from 4 to 8. Negative numbers may be entered as parameters
#and no array will have less than 2 elements.

#Find the min and max, then find the distance between them. minus the length of the array from that number, plus one.

def Consecutive(arr):
  mi = min(arr)
  ma =max(arr)
  l =len(arr)
  r = range(mi,ma)
  lr = len(r)
  a = lr - l +1
  print (a)

Consecutive([ -2,10,4])
