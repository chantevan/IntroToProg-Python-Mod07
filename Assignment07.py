# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Chantal Van den bussche, 3/12/2025, Created Script and edited docstring
# ------------------------------------------------------------------------------------------ #
import json
from encodings.punycode import selective_find

# Data Storage ---------------------------- #
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

class Person:
    '''A class storing a person's data
    
    ChangeLog: (Who, When, What)
    Chantal Van den bussche,3/12/2025,Created Class
    '''

    def __init__(self, student_first_name: str = '',
                 student_last_name: str = ''):
        ''' This constructor sets Person objects attribute value when Person
        object is created.
        
        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created constructor
        '''
        self.__student_first_name = student_first_name
        self.__student_last_name = student_last_name

    @property # getter/accessor
    def student_first_name(self):
        ''' This method is the 'getter' in getter-setter pair for
        student_first_name. It also formats data in title case.

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created method
        '''
        # Formatting data
        return self.__student_first_name.title()

    @student_first_name.setter # setter/mutator
    def student_first_name(self, value: str):
        ''' This method is the 'setter' in getter-setter pair for
        student_first_name. It also manages error handling for
        student_first_name.

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created method
        '''
        # Allow alphabet characters or default empty string
        if value.isalpha() or value == '':
            self.__student_first_name = value
        else:
            raise ValueError("The first name should contain alphabetical "
                             "letters only.")

    @property
    def student_last_name(self):
        ''' This method is the 'getter' in getter-setter pair for
        student_last_name. It also formats data in title case.

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created method
        '''
        return self.__student_last_name.title()

    @student_last_name.setter
    def student_last_name(self, value: str):
        ''' This method is the 'setter' in getter-setter pair for
        student_last_name. It also manages error handling for
        student_last_name.

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created method
        '''
        if value.isalpha() or value == '':
            self.__student_last_name = value
        else:
            raise ValueError("The last name should contain alphabetical "
                             "letters only.")

    def __str__(self):
        ''' A method that returns comma-separated string for Person Object
        class

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created method'''
        return f'{self.student_first_name},{self.student_last_name}'

class Student(Person):
    ''' A child class that inherits data from parent class Person
    
    ChangeLog: (Who, When, What)
    Chantal Van den bussche, 3/12/2025, Created Class'''

    def __init__(self, student_first_name: str = '',
                 student_last_name: str = '', course_name: str = ''):
        super().__init__(student_first_name=student_first_name,
                         student_last_name=student_last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        ''' This method is the 'getter' in getter-setter pair for
        course_name.

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created method
        '''
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str):
        ''' This method is the 'setter' in getter-setter pair for
        course_name. It also manages error handling for
        course_name.

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created method
        '''
        if isinstance(value, str) or value == '':
            self.__course_name = value
        else:
            raise Exception('ERROR! There was an error with your entered data.')

    def __str__(self):
        ''' A method that returns comma-separated string for Student Object
        class

        ChangeLog: (Who, When, What)
        Chantal Van den bussche, 3/12/2025, Created method'''
        return (f'{self.student_first_name},{self.student_last_name},'
                f'{self.course_name}')


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer methods that work with Json files

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    Chantal Van den bussche, 3/12/2025, Edited docstring
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This method reads data from a json file and loads it into a list
        of dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created Method
        Chantal Van den bussche, 3/12/2025, Edited docstring

        :param file_name: string data with name of file to read from
        :param student_data: list of dict rows to be filled with file data

        :return: list
        """

        try:
            file = open(FILE_NAME, "r")
            # student_data = json.load(file)
            # Commented out above line due to need to convert file data \
            # into Student objects
            # Loads file data into list of dict rows named file_data
            file_data = json.load(file)
            # Convert into file_data dict rows into Student objects
            for student in file_data:
                student_obj: Student = Student(student_first_name=
                                               student["FirstName"],
                                               student_last_name=student
                                               ["LastName"],course_name=
                                               student["CourseName"])
                student_data.append(student_obj)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with "
                                             "reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This method writes data to a json file with data from a list of
        dictionary rows

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created method
        Chantal Van den bussche, 3/12/2025, Edited docstring

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            file_data: list = []
            for student in student_data:
                student_json: dict = {'FirstName': student.student_first_name,
                                      'LastName': student.student_last_name,
                                      'CourseName': student.course_name}
                file_data.append(student_json)
            file = open(FILE_NAME, "w")
            json.dump(file_data, file)
            file.close()
            IO.output_student_courses(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += ("Please check that the file is not open by another "
                        "program.")
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer method that manage user input and
    output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input methods
    RRoot,1.3.2030,Added a method to display the data
    RRoot,1.4.2030,Added a method to display custom error messages
    Chantal Van den bussche, 3/12/2025, Edited docstring
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This method displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created method
        Chantal Van den bussche, 3/12/2025, Edited docstring

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This method displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created method
        Chantal Van den bussche, 3/12/2025, Edited docstring


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This method gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created method
        Chantal Van den bussche, 3/12/2025, Edited docstring

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            # Not passing e to avoid the technical message
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This method displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created method
        Chantal Van den bussche, 3/12/2025, Edited docstring

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.student_first_name} '
                  f'{student.student_last_name} is enrolled in '
                  f'{student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This method gets the student's first name and last name, with a
        course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created method
        Chantal Van den bussche, 3/12/2025, Edited docstring

        :param student_data: list of dict rows to be filled with input data

        :return: list
        """

        try:
            student = Student()
            student.student_first_name = input('Enter the student\'s first name: ')
            student.student_last_name = input('Enter the student\'s last name: ')
            student.course_name = input('Please enter the name of the course: ')
            student_data.append(student)
            print()
            print(f"You have registered {student.student_first_name} "
                  f"{student.student_last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the "
                                             "correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with "
                                             "your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
