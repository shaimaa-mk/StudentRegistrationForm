"""
By Shaima'a Khashan
"""
# Import requests library
import requests
import json
# APIs Endpoints
create_api = "http://staging.bldt.ca/api/method/build_it.test.register_student"
update_api = "http://staging.bldt.ca/api/method/build_it.test.edit_student"
delete_api = "http://staging.bldt.ca/api/method/build_it.test.delete_student"
exportAll_api = "http://staging.bldt.ca/api/method/build_it.test.get_students"
exportStd_api = "http://staging.bldt.ca/api/method/build_it.test.get_student_details"


# Create Student class
class Student:

    # Create student class and store his details
    def __init__(self, full, ag, lvl, mobile_num, student_id):
        self._full_name = full
        self._age = ag
        self._level = lvl
        self._mobile_no = mobile_num
        self._id = student_id
        print(f"Student {self._full_name} has with ID {self._id}add successfully.\n")


while True:
    # Display Student Registration Menu
    print("1. Registration New Student\n"
          "2. Edit Student Details\n"
          "3. Delete Student\n"
          "4. Export Students to Text File\n"
          "5. Export Student Details to Text File\n"
          "6.Exit")
    # Get the number of service the user want
    choice = int(input("Enter the number:"))

    # Case 1 : Create a New Student Object
    if choice == 1:
        # Get student information from user
        full_name = str(input("Enter the name:"))
        age = int(input("Enter the age:"))
        level = str(input("Enter the level:"))
        mobile_no = str(input("Enter the mobile number:"))
        # Get response after create student object in server
        create_response = requests.post(create_api, data={'full_name': full_name,
                                                          'age': age,
                                                          'level': level,
                                                          'mobile_number': mobile_no})
    # Case 2 : Update student information
    elif choice == 2:
        # Get student ID from user
        update_std_id = str(input("Enter the Student ID please."))
        # Check input is not empty
        if update_std_id:
            # Get student updates
            full_name = str(input("Enter the name:"))
            age = int(input("Enter the age:"))
            level = str(input("Enter the level:"))
            mobile_no = str(input("Enter the mobile number:"))
            # Send student updates
            requests.put(update_api, data={'id': update_std_id,
                                           'full_name': full_name,
                                           'age': age,
                                           'level': level,
                                           'mobile_number': mobile_no})
        else:
            print("No such Student found!")
    # Case 3 : Delete student by ID
    elif choice == 3:
        # Get student ID to delete
        delete_std_id = str(input("Enter the Student ID please."))
        # Check input is not empty
        if delete_std_id:
            result = requests.delete(delete_api, data={'id': delete_std_id})
            print(result.status_code)
        else:
            print("No such student found!")
    # Case 4 : Export students details as text file named Students.txt
    elif choice == 4:
        # Get response after listening to server
        students_response = requests.get(exportAll_api)
        # Check status
        if students_response.status_code:
            # Get students details who's created in server
            students_details = students_response.json()['data']
            # If Students.txt file exists then append new inputs with last one, else create Students.txt file
            file = open("Students.txt", "w")
            # Write each student details separately
            for one in students_details:
                file.write(f"Student ID:{one['id']} Full Name: {one['full_name']} Age: {one['age']} "
                           f"Level: {one['level']} Mobile Number: {one['mobile_number']}\n")
            # close Students.txt file
            file.close()
        else:
            print("Request Failed")
    # Case 5 : Export student details as text file named Student.text
    elif choice == 5:
        # Get student ID to export data
        export_std_id = str(input("Enter the Student ID please."))
        # Check input is not empty
        if export_std_id:
            # Get response after listening to server
            student_response = requests.get(exportStd_api, data={'id': export_std_id})
            result = student_response.text
            # Get students details who's created in server
            std_details = json.loads(result)['data']
            # Check status
            if student_response.status_code == True:
                # If Student.txt file exists then append new inputs with last one, else create Student.txt file
                file = open("Student.txt", "w")
                # Write student details
                file.write(f"Student ID:{std_details['id']} Full Name: {std_details['full_name']} "
                           f"Age: {std_details['age']} Level: {std_details['level']} "
                           f"Mobile Number: {std_details['mobile_number']}")
                # close Students.txt file
                file.close()
            else:
                print("Request Failed!")
        else:
            print("No such student found!")

    elif choice == 6:
        break
