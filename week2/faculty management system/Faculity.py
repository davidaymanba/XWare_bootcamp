import os

from Department import *

fauclty_lst =[]

def create_faculty():
    Id = input("please enter Id faculty :")
    name = input("please enter name faculty: ")
    num_of_department = input("enter number of departmenets : ")
    fauclty_lst.append({'Id':Id , 'name':name ,"n_dpts" : num_of_department})
    print(f"Id:{Id} ,name:{name}")
    print(fauclty_lst)

def updatefaculty ():
    searchId= input("please enter id : ") 
    for fac_id in fauclty_lst:
        if fac_id['Id'] == searchId:
            x = input("enter new id ")
            y = input("enter new numebr of depts ")
            
            fac_id['Id'] = x
            fac_id['n_dpts'] = y
            
    print(fauclty_lst)

def read_fauclty ():
    searchId = input("Please Enter faculty Id: ")
    
    for fac in fauclty_lst:

        if fac['Id'] == searchId:
            print(f"Faculty Id: {searchId} Faculty Name: {fac['name']}")
            return 
        
    print("the id is not exist !")

def link_Professor_Faculty():
    profs_list = []
    num_Professor = int(input("Please Enter How Many professors you want to enter: "))   
    for count in range(num_Professor):
        print(f"Professor {count + 1 }: ")
        profId = input("Please Enter Professor Id: ")
        profName = input("Please Enter Professor Name: ")
        profDep = input("Please Enter Professor Department: ")
        profs_list.append({'profId': profId, 'profName':profName, 'profDep': profDep})
        print(" added successfully")
        # enter = input(" Press any button to add the next Professor")    

    print(profs_list)

    #print(profs_list)



create_faculty()
create_depart()
updatefaculty()
read_fauclty()
link_Professor_Faculty()

