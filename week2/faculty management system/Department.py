import os


department_lst =[]

def create_depart():
    Id = input("please enter Id depart :")
    name = input("please enter name dapart : ")

    department_lst.append({'Id' : Id, 'name' : name})
    print(f"id :{Id}, name:{name}")
    print(department_lst)

def update_department ():
    searchId = input ("please enter id : ") 
    for fac_id in department_lst:
        if fac_id['Id'] == searchId:

            x = input("enter new id")
            y = input("enter new name")

            fac_id['Id'] = x
            fac_id['name'] = y

    print(department_lst)        

def read_department ():
    searchId = input("Please Enter department Id: ")
    
    for fac in department_lst:

        if fac['Id'] == searchId:
            print(f"department Id: {searchId} , department Name : {fac['name']}")
            return 
        
    print("the id is not exist !")


create_depart()
update_department()
read_department()

