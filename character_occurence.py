string = input("Please enter any word:")
char = input("Please enter any character: ")

i = 0
count = 0

while(i < len(string)):
    if(string[i]== char):
        count = count + 1
    i = i + 1

print("The total number of time", char,"has occured =", count)