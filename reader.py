#We need a way for the program to ask the user for the file name
filename = input("Enter the file name:")
breakPoint = input("Enter the break point")
print("Thank you, we will add a new line for each " +breakPoint )


def function(name,breaker):
    fileOriginal = open(name,"r+")

    fileOriginal.write(fileOriginal.read().replace(breaker, '\n'+breaker))

function(filename,breakPoint)