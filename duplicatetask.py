import os,filecmp
def comparefiles(file_1,file_2):
    if(not os.path.exists(file_1)):
        print(file_1,'File Not Exists')
    elif(not os.path.exists(file_2)):
        print(file_2,"File Not Exists") 
    else:
        compare=filecmp.cmp(file_1,file_2)  
        if compare == True:
            os.remove(file_2)
            print("the duplicate file is deleted")
        else :
            print("no dupicate found")    
    


def main():
    file_1=input("Enter the first file")
    file_2=input("Enter the second file")

    comparefiles(file_1,file_2)


if __name__  == '__main__':
    main()