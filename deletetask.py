import os

def delete_task(file_namess):
    os.remove(file_namess)
    print("file is removed successfully")

def main():
    file_namess=input("enter the filename you want to remove")
    delete_task(file_namess)

if __name__ == "__main__":
      main()

