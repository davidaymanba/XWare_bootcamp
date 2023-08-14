
import os
subjects_lst =[]

def create_subject():
    Id = input("please enter Id subject :")
    name = input("please enter name subject : ")
    num_of_subjects = input("enter number of subjects : ")
    subjects_lst.append({'Id':Id , 'name':name ,"n_subjects" : num_of_subjects})
    print(f"Id:{Id} ,name:{name} , n_sub:{num_of_subjects}")
    print(subjects_lst)

def update_subjects ():
    
    searchId= input("please enter id : ") 
    is_found = False
    for fac_id in subjects_lst:
        if fac_id['Id'] == searchId:
            x = input("enter new id ")
            y = input("enter new numebr of subjects ")
            
            fac_id['Id'] = x
            fac_id['n_subjects'] = y
            is_found = True

    if  not is_found:
        print("the item is not found") 

def read_subjects ():
    searchId = input("Please Enter subject Id: ")
    
    for fac in subjects_lst:

        if fac['Id'] == searchId:
            print(f"subject Id: {searchId} subject Name: {fac['name']}")
            return 
        
    print("the id is not exist !")

def link_Professor_subjects():
    profs_list = []
    num_Professor = int(input("Please Enter How Many professors you want to enter: "))   
    for count in range(num_Professor):
        print(f"Professor {count + 1 }: ")
        profId = input("Please Enter Professor Id: ")
        profName = input("Please Enter Professor Name: ")
        profDep = input("Please Enter Professor Department: ")
        profs_list.append({'profId': profId, 'profName':profName, 'profDep': profDep})
        print(" added successfully")
        enter = input(" Press any button to add the next Professor")    

    return  profs_list


create_subject()
update_subjects()
read_subjects()
link_Professor_subjects()