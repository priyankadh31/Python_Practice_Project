def add_employee(employee_dict,emp_id,name,department):
    if emp_id not in employee_dict:
        employee_dict[emp_id]={'Name':name ,'Department':department}
        print("Employee added successfully.....")
    else:
        print("Employee ID already exists. ")


def remove_employee(employee_dict ,emp_id):
    if emp_id in employee_dict:
        del employee_dict[emp_id]
        print("Employee removed successfully ....")
    else:
        print("Employe ID not found. ")

def update_employee(employee_dict,emp_id, name=None, department=None):
    if emp_id in employee_dict:
        if name:
            employee_dict[emp_id]['Name'] =name
        if department:
            employee_dict[emp_id]['Department'] = department
        print("Employee updated successfully... ")
    else:
        print("Employee ID not found.")

def list_employee(employee_dict):
    print("\n\n Employee Record \n")
    if not employee_dict:
        print("No employee to display.")
    for emp_id,details in employee_dict.items():
        print(f"ID:{emp_id}, Name:{details['Name']}Department:{details['Department']}") 


 #Main Function
if __name__ == "__main__":
    employee={}

    while True:
        print(
            "\n================Employee Management System===============\n\n")
        print("press 1: To Add Employee....")
        print("press 2: To Remove Employee.....")
        print("press 3: To Update Employee....")
        print("press 4: To List Employee....")
        print("press 5: To Exit....")

    choice = int(input("\nEnter your choice (1, 2,3,4,5)......"))
    if choice == 1:
        id =int(input("Enter employee id....."))
        name=input("Enter employee name....") 
        dpartment =input("Enter employee department....")
        add_employee(employee, id,name,departmnet)

    elif choice == 2:
        id = int(input("Enter employee id....."))
        remove_employee(emloyee,id)

    elif choice == 3:
        id = int(input("Enter employee id...."))
        name =input("Enter new employee name (leave blank to keep current)....")
        department =input("Enter new employee department(leave balnk to keep current)....")
        update_employee(employees,id,name if name else None, departmnet if departmnet else None)

    elif choice == 4:
        list_employee(emploees)

    elif choice == 5:
        print("Existing the system.....")
        

    else:    
        print("Please enter a valid choice.....")

        


                     
