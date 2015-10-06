#Using the Python language, have the function ExOh(str) take the str parameter being passed
#and return the string true if there is an equal number of x's and o's, otherwise return
#the string false. Only these two letters will be entered in the string, no punctuation or
#numbers. For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

string = "xxxooo" #should return true
string_2 = "xxxxxxo" # and our false string

def ExOh(index):
    x_total = 0;   # keep track of totals
    o_total = 0;
    for i in index:
        if i == "x":
            x_total+=1
        else:
            o_total+=1
    if x_total != o_total:
        print("false")
    else:
        print("true")

ExOh(string) #returns true
ExOh(string_2) #returns false
