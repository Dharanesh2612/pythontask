
"""2 Question:Write a program which will take input from the user and Returns(Using function)
1)Addition on the list
Example: [2,3,4,5,6,7]  --> 27
Note: don't use sum()
2)Maximum from the list
Example: [2,3,4,5,6,7]  --> 7
Note: don't use max()"""
def sum(list1,size):
    sum=0
    for i in range(size):
        sum=sum+list1[i]
    return sum

def max(list1,size):
    max1=0
    for i in range(size):
        if(list1[i]>max1):
            max1=list1[i]
    return max1


def main():
    choice= int(input("enter your choice"))
    list1=[]
    size=int(input("enter the size: "))
    for i in range(size):
        value=int(input("enter the value: "))
        list1.append(value)
    while(True):
        if(choice==1):
           print(sum(list1,size))
           break
        elif(choice==2):
            print(max(list1,size))
            break
        else:
            print("you have enter the wrong choice")
            break



if __name__=="__main__":
    main()











