import re
class UserRegistration:
    
     #UC1- Validate First Name
    def validateFirstName(self):
        patternforFirstname = '^[A-Z]{1}[a-z]{3,}$'
        if re.search(patternforFirstname, firstName):
            return 'valid'
        else:
            return 'invalid'
        
     #UC1- Validate Last Name
    def validateLastName(self):
        patternforLastname = '^[A-Z]{1}[a-z]{3,}$'
        if re.search(patternforLastname, firstName):
            return 'valid'
        else:
            return 'invalid'
        
     #UC1- Validate Email Id
    def validateEmail(self):
        patternforEmail = "^([a-zA-Z]{3,}([.|_|+|-]?[a-zA-Z0-9]+)?[@][a-zA-Z0-9]+[.][a-zA-Z]{2,3}([.]?[a-zA-Z]{2,3})?)$"
        if re.search(patternforEmail, email):
            return 'valid'
        else:
            return 'invalid'
if __name__ == '__main__':
    print("Welcome to User Registration")
    userreg = UserRegistration()
    firstName = input("Enter first name:")
    print(userreg.validateFirstName())
    lastName = input("Enter last name")
    print(userreg.validateLastName())
    email = input("Enter email id")
    print(userreg.validateEmail())



