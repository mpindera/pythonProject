# Health Care 

is an application written in python with a GUI application.
It allows users to register and log in to the system,

# Necessary imports
The necessary imports are done, including `os`, `tkinter`, `base64`, `messagebox`, and `uuid`.

# How to run
Run baseRegister.py


# How to use

1. Create Account new Patient ![2023-06-10-23-58-35](https://github.com/mpindera/pythonProject/assets/107795584/96dc4c5e-b3da-42a0-9f45-a7f2713c7398)



2. Sending Emails ![2023-06-10-23-59-34](https://github.com/mpindera/pythonProject/assets/107795584/962ab889-0ebd-41ce-9fe2-632699ba9cdf)



3. Adding UUID to new Admin ![2023-06-11-00-00-01](https://github.com/mpindera/pythonProject/assets/107795584/b6a2477c-34d7-47d9-b84b-df2f02d55d10)

Admin Interface for Health Care Application: This part allows an admin to calculate and send diet information to patients via email. It utilizes the tkinter library for creating a graphical user interface (GUI) and the smtplib library for sending emails. The main functionality includes:

Input fields for patient email, patient name, and dietitian name
Dropdown menus for selecting gender and activity level
Spinbox for entering age
Entry fields for weight and height
Calculation of caloric requirements, protein, fat, and carbohydrates based on the input values
Displaying the calculated values in a table format
Sending an email to the patient with the calculated diet information
# Admin Interface:

Fill in the required information in the input fields (patient email, patient name, dietitian name, gender, activity level, weight, height, and age).
Click on the "Calculate" button to calculate the diet information.
The calculated values will be displayed in a table format.
Click on the "Send" button to send the calculated diet information to the patient via email.
If any required field is missing, an error message will be displayed.
