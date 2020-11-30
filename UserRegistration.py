import re
class UserRegistration:

    def validateFirstName(self):
        patterforFirstname = '^[A-Z]{1}[a-z]{3,}$'
        if re.search(patterforFirstname, firstName):
            return 'valid'
        else:
            return 'invalid'

if __name__ == '__main__':
    print("Welcome to User Registration")
    firstName = input("Enter first name:")
    userreg = UserRegistration()
    print(userreg.validateFirstName())
