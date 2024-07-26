#sort a dictionary by value in python (lambda function)by name
def main():
    name_list = [
    {'name':'shreya','age':15},
    {'name':'pratiksha','age':13},
    {'name':'prerna','age':15}
    ]

    name_list.sort(key=lambda x : x['name'])
    print(name_list)
if __name__ =="__main__":
       main()



#sort a dictionary by value in python (lambda function)by age
def main():
    name_list = [
    {'name':'shreya','age':15},
    {'name':'pratiksha','age':13},
    {'name':'prerna','age':15}
    ]

    name_list.sort(key=lambda x : x['age'])
    print(name_list)
if __name__ =="__main__":
       main()
