"""task_ass="this is my name"
print("thie output is:",task_ass,id(task_ass))
task_ass1="this is my name"
print("thie output is:",task_ass1,id(task_ass1))
task_ass1="this is my gender"
print("thie output is:",task_ass1,id(task_ass1))"""




"""
numa=40
numb=20
numc=30

if numa > numb and numa > numc:
   print("a is bigger")

elif numb > numa and numb > numc:
     print("b is bigger")
else:
    print("c is larger")
    """
menu_card = ['mutton fry ','mutton gravy','mutton crispy']
 
def display_menu():
    print('Menu Card:',menu_card)
 
def add_starter(starter):
    menu_card.append(starter)
    print(f'{starter} added to the menu card.')
 
def update_starter(prev_starter, new_starter):
    index = menu_card.index(prev_starter)
    menu_card[index] = new_starter
    print(f'{prev_starter} updated to {new_starter}.')
 
def remove_starter(starter):
    menu_card.remove(starter)
    print(f"{starter} removed from menu card.")
 

def main():
    print("Select option")
    print("1.Display Menu Card")
    print("2.Add to Menu Card")
    print("3.Update in Menu Card")
    print("4.Remove from Menu Card")
 
    choice = input("Enter your choice (1-4): ")
 
    if choice == '1':
        display_menu()
    elif choice == '2':
        starter = input("Enter the starter to add: ")
        add_starter(starter)
    elif choice == '3':
        prev_starter = input("Enter old starter: ")
        new_starter = input("Enter new starter: ")
        update_starter(prev_starter, new_starter)
    elif choice == '4':
        starter = input("Enter starter to remove: ")
        remove_starter(starter)
    else:
        print("Invalid option.")
 
 
 
if __name__=="__main__":
    main()