
department_lst = []

class department :
        
        def __init__(self,id,name,number_of_department):
            print(f"id {id} , name {name}")
        @staticmethod
        def create_department ():
            id = input("please enter department id : ")
            name = input("please enter department name : ")
            department_lst.append({'Id':id , 'name':name})

        @staticmethod
        def update_department ():
         searchId = input ("please enter id : ") 
         for fac_id in department_lst:
             if fac_id['Id'] == searchId:
                x = input("enter new id : ")
                y = input("enter new name : ")

                fac_id['Id'] = x
                fac_id['name'] = y

        @staticmethod
        def read_department ():
         searchId = input("Please Enter department Id: ")
    
         for fac in department_lst:
            if fac['Id'] == searchId:
                print(f"department Id: {searchId} , department Name : {fac['name']}")
            else :
                print("the id is not exist !")





department.create_department()   
print(department_lst)
department.update_department()
print(department_lst)
department.read_department()