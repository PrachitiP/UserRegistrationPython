import re
class UserRegistration:

    def validateFirstName(self):
        patterforFirstname = '^[A-Z]{1}[a-z]{3,}$'
        if re.search(patterforFirstname, firstName):
            return 'valid'
        else:
            return 'invalid'

    def validateLastName(self):
        patterforLastname = '^[A-Z]{1}[a-z]{3,}$'
        if re.search(patterforLastname, firstName):
            return 'valid'
        else:
            return 'invalid'


if __name__ == '__main__':
    print("Welcome to User Registration")
    firstName = input("Enter first name:")
    lastName = input("Enter last name")
    userreg = UserRegistration()
    print(userreg.validateFirstName())
    print(userreg.validateLastName())
