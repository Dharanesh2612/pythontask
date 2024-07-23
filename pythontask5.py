"""
5 question:Write a program to check if a string contains any special character"""

def special_characters(sp):
    special_character = set("!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`")
    
    for char in sp:
        if char in special_character:
            return True
        if char not in special_character:
            return False

string = input("Enter a string:")

if special_characters(string):
    print("String contains special characters.")
else:
    print("String doesn't contain special characters.")