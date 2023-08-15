import os 

faculty_lst = []

profs_list =[]

class faculty :
    def __init__(self,id,name,number_of_department):
        print(f"id {id} , name {name} ,number_of_department {number_of_department}")
    @staticmethod
    def create_faculty ():
        id = input("please enter faculty id : ")
        name = input("please enter faculty name : ")
        number_of_department = input("please enter num_of_department: ")
        faculty_lst.append({'Id':id , 'name':name ,"n_dpts" : number_of_department})

    @staticmethod
    def update_faculty ():
        searchId = input("please enter id : ") 

        for fac_id in faculty_lst:
          
           if fac_id['Id'] == searchId:
            x = input("enter new id ")
            y = input("enter new numebr of depts ")
            
            fac_id['Id'] = x
            fac_id['n_dpts'] = y

    @staticmethod              
    def read_fauclty ():
        searchId = input("Please Enter faculty Id: ")
    
        for fac in faculty_lst:
            if fac['Id'] == searchId :

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
        enter = input(" Press any button to add the next Professor")    

    print(profs_list)


faculty.create_faculty()
print(faculty_lst)
faculty.update_faculty()
print(faculty_lst)
faculty.read_fauclty()
print(faculty_lst)
faculty.link_Professor_Faculty()