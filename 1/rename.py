import os
import random
import string

# This function will generate a random string of 16 bytes
def random_bytes():
    letters = string.ascii_letters
    return (''.join(random.choice(letters) for i in range(16)))
    
def main():
    
    # Store the path to your files directory in this variable
    path = os.getcwd()+'/files/' 
    
    #returning list of files from the files directory
    files = os.listdir(path)
    new = []
    new_filename = []
    ext = []
    for i in range(len(files)):
        
        # This will remove file extension and appends new filename to a list
        splice = os.path.splitext(files[i])[0]
        new.append(splice)
        
        # Retrieving file extension
        k = files[i].split('.')
        ext.append(k[1])
        
        # Updating filename
        x = "New___" + new[i] + "___" + random_bytes() + "." + ext[i]
        new_filename.append(x) 

        # Renaming files in the directory
        os.rename(path + files[i], path + new_filename[i])
        
if __name__ == '__main__':
    main()
    