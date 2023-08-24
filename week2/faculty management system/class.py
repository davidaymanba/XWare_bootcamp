# class david :
#     def __init__(self):
#         print("hello member")
# david()
# david()
# david()        

# david_one = david()
# david_two = david()
# david_three = david()

# print(david_one.__class__)


class skill :

    def __init__(self):

        self.skill = ["html","css"]
    
    def __str__(self):
        
        return f"this is my skils => {self.skill}"
    
    def __len__(self):
        
        return len(self.skill)

profile = skill()
profile.skill.append("django")
profile.skill.append("php")
profile.skill.append("SQL")
#print(len(profile))
#print(profile)
#print(profile.__class__)



#mystring = "david"
# print(type(mystring))
# print(mystring.__class__)
#print(dir(str))
#print(str.upper(mystring))

class member :

    not_allowed_name = ["ddddd" ,"fffff", "kkkkk"]

    users_num = 0

    @classmethod
    def show_count_users (cls):

        return f" we have {cls.users_num} users in our system "
    @staticmethod
    def say_hello():
        
        return f"hello from static method"


    def __init__(self , first_name , middle_name , last_name , gender ):
        self.f_name = first_name
        self.m_name = middle_name
        self.l_name = last_name
        self.gender = gender 
        member.users_num += 1 

    def full_name (self):

        if self.f_name in member.not_allowed_name:

            raise ValueError ("name not allowed")
        else :
            return f"{self.f_name} {self.m_name} {self.l_name}"    


    def welcome_first (self):
         if self.gender == "male":
             return f"hello mr/ {self.f_name}"
         elif self.gender == "female":
             return f"hello mrs/ {self.f_name}"
         else :
             return f"{self.f_name}" 


    def get_all_info(self):

        return f"{self.welcome_first()} , ypur full name is : {self.full_name()} "           

    
    def delete_user (self):

        member.users_num -= 1 

        return f"user {self.f_name}  deleted . "



#print(member.users_num)

member_one = member("david" , "ayman", "bakhet","male")
member_two = member("fathy" , "ahmed" , "sayed","male")
member_three = member("boty" , "ayman" , "bakhet","female")
member_four = member("ddddd" , "fffff" , "bakhet","female")


#print(member_four.delete_user())

#print(member.users_num)

# print(member_one.f_name,member_one.m_name,member_one.l_name)
# print(member_two.f_name , member_two.m_name ,member_two.l_name)
# print(member_three.f_name ,member_three.m_name ,member_three.l_name)
    
# print( "hello ", member_three.full_name())
# print(member_three.welcome_first())


# print(member_one.get_all_info())

#print("#" * 50)

#print(member.show_count_users())
#print(member.say_hello())


class food : # base class
    def __init__(self ,name ,price ):
      
      self.name = name
      self.price=price

      print(f"{self.name}food is created from base class")
    def eat (self):
      print("eat method from base class")

class apple(food) : # derived
    def __init__(self,name,price,amount):

        #food.__init__(self,name)
        #self.name = name
        #self.price=price+200
        self.amount=amount

        super().__init__(name,price)
       
        print(f"{self.name} is created from derived class and the price is {self.price} and the price is {self.amount}")

    def get_from_tree(self):
        print(f"get fron tree and from derived class ")
    def eat (self):
      print("eat method from base class")

        
#food_one = food("pizza")
# food_two = apple("pizza",150,500)
# food_two.eat()
# food_two.get_from_tree()



class base_one:
    
    def __init__(self):

        print(f"welcome base one ")

    def func_one(self):

        print(f"one")

class base_two:
     
     def __init__(self):

        print(f"welcome base two ")

     def func_two(self):

        print(f"two")    

class derived(base_two,base_one):
    pass


# my_var=derived()
# print(derived.mro())


# print(my_var.func_one())
# print(my_var.func_two())

# my_var.func_one()
# my_var.func_two()



