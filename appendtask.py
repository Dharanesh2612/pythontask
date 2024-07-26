#Write an application which will append your existing file

import os

def append(filename1,filename2):
    if  os.path.exists(filename1):
        
        open2 = open(filename1, 'a')
        open2.write(filename2)

        print("appended successfull at filename2")
    else:
        print("file not exist")
def main():
    filename1=input("enter the file that should append")
    filename2=input("enter the file name where the filename1 should be append")
    append(filename1,filename2)

if __name__ == "__main__":
      main()
