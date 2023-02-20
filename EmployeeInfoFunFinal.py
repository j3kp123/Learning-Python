lstEmployees = []
lstNames = []
counter = 0

def import_employees():
    my_file1 = open("ems.txt", "r")
    data = my_file1.read()
    data_into_list = data.split('\n')
    print(data_into_list)
    my_file1.close()
    print("\n**Import was successful**")

def export_employees():
    with open("ems.txt", "w") as file:
        for employee in lstEmployees:
            file.write("^".join(employee) + "\n")
    print("\n**Export was successful**")
            
def search_ssn():
    ssn = input('\nEnter employee SSN: ')
    for employee in lstEmployees:
        if ssn == employee[1]:
            print( "" )
            print( "---------------" +employee[0] +"---------------")
            print( "SSN: " + employee[1])
            print( "Phone: " + employee[2])
            print( "Email: " + employee[3])
            print( "Salary: $ " + employee[4])
            print( "---------------------------------------------------------------" )
            print( "" )
            return employee
    return -1
            
def edit_employee():
    search = search_ssn()
    if search == -1:
        print('Employee not found...')
    else:
        name = input('Enter the new Name: ')
        ssn = input('Enter the new SSN: ')
        phone = input('Enter the new Phone Number: ')
        email = input('Enter the new Email: ')
        salary = input('Enter the new Salary: ')
        search[0] = name
        search[1] = ssn
        search[2] = phone
        search[3] = email
        search[4] = salary
        return employee
        print('\n*Employee information has been successfully updated*\n')
    

def add_employee():
    global counter
    while counter<5:
        
        print("  There are ({0:d}) employees in the system.".format(counter))
        print("---------------------------------------------\n")
        name = input('\nEnter employee Name: ')
        lstNames.insert(counter, name)
        ssn = input('Enter employee SSN: ')
        phone = input('Enter employee Phone Number: ')
        email = input('Enter employee Email: ')
        salary = input('Enter employee Salary: $')
        print('\n*Employee information has been successfully entered*\n')
        
        lstEmployees.append([name, ssn, phone, email, salary])
        counter = counter + 1
        
        option = input('Do you want to add another employee, y or n? ')
        if(option == 'y'):
            add_employee()
        else:
            main()        

def print_employee():
    for employee in lstEmployees:
        print( "" )
        print( "" )
        print( "---------------" +employee[0] +"---------------")
        print( "SSN: " + employee[1])
        print( "Phone: " + employee[2])
        print( "Email: " + employee[3])
        print( "Salary: $ " + employee[4])
        print( "---------------------------------------------------------------" )
        print( "" )

def main():
    while True:            
        print('-----------------------------------------------')
        print("")
        print('          Employee Management System           ')
        print("")
        print("---------------------------------------------\n")
        print('[1] Add an Employee: \n')
        print('[2] View All Employees: \n')
        print('[3] Search Employee by SSN: \n')
        print('[4] Edit Employee Information: \n')
        print('[5] Export Employee Information: \n')
        print('[6] Import Employee Information: \n')
        print('[7] Quit\n')

        user_option = input('Please select an option: ')
        if user_option == "1":
            add_employee()
        elif user_option == "2":
            print('\n' * 3)
            print_employee()
            print('\n' * 3)
        elif user_option == "3":
            found = search_ssn()
            if found == -1:
                print('Employee not found...')
        elif user_option == "4":
            edit_employee()
        elif user_option == "5":
            export_employees()
        elif user_option == "6":
            import_employees()
        elif user_option == "7":
            break
        else:
            print('Please select a valid option...')

if __name__ == "__main__":
    main()
