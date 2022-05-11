this_dict = {}
operation="1"

def add_student():
    s1 = input("Enter the student name= ")
    g1 =float(input("Enter the student grade= "))
    if(0.0<=g1<=100.0):
        this_dict[s1]=g1
    else:
        print("Invalid grade")

def search_student():
    s1 = input("Enter the student name= ")
    if s1 in this_dict.keys():
        print(s1+" grade is "+str(this_dict[s1]))

def delete_student():
    s1 = input("Enter the student name= ")
    if s1 in this_dict.keys():
        this_dict.pop(s1)
    
while(operation in ["1","2","3"]):
    operation = input("Enter your operation 1- add, 2-search, 3-deletion : ")
    if(operation == "1"):
        add_student()
    elif(operation == "2"):
        search_student()
    elif(operation == "3"):
        delete_student()
    else:
        print("Invalid selection or Process end")
        


    