import os

# Set the directory path
directory = "/Users/Saksham/Desktop/Problems/Testcases"

# Get all the file names in the directory
files = os.listdir(directory)


def nod(x): #function that finds the number of digits in a number
    nod=0
    while(x!=0):
        nod+=1
        x=x//10
    return nod

def rename_input(): #rename all files to inputXXX.txt
    counter_i = 0
    for filename in files:
        # Construct the new file name
        if(counter_i < 10):
           new_filename = "input0" + str(counter_i) + ".txt"
        else:
            new_filename = "input" + str(counter_i) + ".txt"

        counter_i+=1
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

def rename_output(): #rename all files to outputXXX.txt
    counter_o = 0
    for filename in files:
        # Construct the new file name
        if(counter_o < 10):
            new_filename = "output0" + str(counter_o) + ".txt"
        else:
            new_filename = "output" + str(counter_o) + ".txt"
        counter_o+=1
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))