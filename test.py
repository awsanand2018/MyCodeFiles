import os

def files(val):
    if os.path.isfile(val):
        print("File with the same name and extension exists already. Enter a different file name ")
        inputfile()
    else:
        with open(val,"w") as f:
            print("System created a file {}".format(val) )
def inputfile():
    q=input("Enter file name: ")
    files(q)
inputfile()