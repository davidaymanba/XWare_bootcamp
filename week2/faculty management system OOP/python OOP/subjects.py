 
from faculty import * 

subject_lst = []


class subject :
    @staticmethod
    def create_subject():
        Id = input("please enter Id subject :")
        name = input("please enter name subject : ")
        num_of_subjects = input("enter number of subjects : ")
        subject_lst.append({'Id':Id , 'name':name ,"n_subjects" : num_of_subjects})
        print(f"Id:{Id} ,name:{name} , n_sub:{num_of_subjects}")
        

    @staticmethod
    def update_subject (): 
        searchId= input("please enter id : ") 
        is_found = False
        for fac_id in subject_lst:
            if fac_id['Id'] == searchId:
                x = input("enter new id ")
                y = input("enter new numebr of subjects ")
            
                fac_id['Id'] = x
                fac_id['n_subjects'] = y
                is_found = True

        if  not is_found:
            print("the item is not found") 

    @staticmethod
    def read_subject ():
        searchId = input("Please Enter subject Id: ")
    
        for fac in subject_lst:

         if fac['Id'] == searchId:
            print(f"subject Id: {searchId} subject Name: {fac['name']}")
        else:
            print("the id is not exist !")

    @staticmethod
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





subject.create_subject()
print(subject_lst)
subject.update_subject()
print(subject_lst)
subject.read_subject()
subject.link_Professor_subjects()