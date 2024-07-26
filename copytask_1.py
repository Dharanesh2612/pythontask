import os
def copyfile(file_1,file_2):
    if not os.path.exists(file_1):
        print("file is nott exists",file_1)
    else:
        file= open(file_1, 'r')
        cpoy = file.read()
        
        open2 = open(file_2, 'w')
        open2.write(cpoy)

        print("successfully take copied from one file to another file")

def main():
    file_1=input("enter the file name")
    file_2=input("enter the second file name")
    copyfile( file_1,file_2)

if __name__ == "__main__":
      main()