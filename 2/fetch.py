import os
import ntpath

def fetch(filename):
    path = os.getcwd()
    filelist = []
    nameoffile = []
    ext = []
    
    # Appending list of filenames in a directory and it's sub-directories
    for root, dirs, files in os.walk(path):
        for name in files:
            filelist.append(os.path.join(root, name))
    
    # Retrieving only file names by splitting the path
    for i in range(len(filelist)):
        j = os.path.split(str(filelist[i]))
        nameoffile.append(j)
    
    for k in range(len(nameoffile)):
        ext.append(nameoffile[k][1])
    
    # Reeturns boolean value based on file present in the list
    print(bool(filename in ext))
    
def main():
    filename = input("Enter a filename: ")
    fetch(filename)

if __name__ == '__main__':
    main()