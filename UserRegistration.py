import re
class UserRegistration:

    #UC1- Validate First Name
    def validateFirstName(self):
        patternforFirstname = '^[A-Z]{1}[a-z]{3,}$'
        if re.search(patternforFirstname, firstName):
            return 'valid'
        else:
            return 'invalid'
        
    #UC2- Validate Last Name
    def validateLastName(self):
        patternforLastname = '^[A-Z]{1}[a-z]{3,}$'
        if re.search(patternforLastname, firstName):
            return 'valid'
        else:
            return 'invalid'

    #UC3- Validate Pattern for Email id
    def validateEmail(self):
        patternforEmail = "^([a-zA-Z]{3,}([.|_|+|-]?[a-zA-Z0-9]+)?[@][a-zA-Z0-9]+[.][a-zA-Z]{2,3}([.]?[a-zA-Z]{2,3})?)$"
        if re.search(patternforEmail, email):
            return 'valid'
        else:
            return 'invalid'

     #UC4- Validate Phone Number
    def validatePhoneNo(self):
        patternforPhoneNo = "^[91 ]{3}[7-9]{1}[0-9]{9}$"
        if re.search(patternforPhoneNo, phoneNo):
            return 'valid'
        else:
            return 'invalid'
        
    #UC5- Password with 8 letters
    def passwordRule1(self):
        patternforPassword1 = "^[a-zA-Z]{8}$"
        if re.search(patternforPassword1, password1):
            return 'valid'
        else:
            return 'invalid'

     #UC6- Password with at least one upper case letter
    def passwordRule2(self):
        patternforPassword2 = "^(?=.*[A-Z]).{8,}$"
        if re.search(patternforPassword2, password2):
            return 'valid'
        else:
            return 'invalid'
        
    #UC7- Password with at least one numeric value
    def passwordRule3(self):
        patternforPassword3 = "^(?=.*[A-Z])(?=.*?[0-9]).{8,}$"
        if re.search(patternforPassword3, password3):
            return 'valid'
        else:
            return 'invalid'
    
    #UC8- Password with one special character
    def passwordRule4(self):
        patternforPassword4 = "^(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        if re.search(patternforPassword4, password4):
            return 'valid'
        else:
            return 'invalid'

if __name__ == '__main__':
    print("Welcome to User Registration")
    userreg = UserRegistration()

    firstName = input("Enter first name:")
    print(userreg.validateFirstName())

    lastName = input("Enter last name:")
    print(userreg.validateLastName())

    email = input("Enter email id:")
    print(userreg.validateEmail())

    phoneNo = input("Enter phone no:")
    print(userreg.validatePhoneNo())

    password1 = input("Enter password:")
    print(userreg.passwordRule1())

    password2 = input("Enter password:")
    print(userreg.passwordRule2())

    password3 = input("Enter password:")
    print(userreg.passwordRule3())
    
    password4 = input("Enter password:")
    print(userreg.passwordRule4())
