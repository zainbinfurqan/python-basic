# print("Zain Ahmed")
# print(2+2)

# num1 = 10
# num2 = 1.5
# print(num1+num2)

# name = 'Zain Ahmed'

# message = 'Hye' + ' ' + name + ' ' + 'greeting'
# message = f'Hye {name}. greeting'


# print(message.lower())
# print(message.upper())
# print(message)


def greeting(num1, num2):
    print(num1 + num2)


# greeting(12, 10)

class UserInfo():
    def __init__(self):
        self.message = 'Pakistan Public School'

    def userData(self, name, email, phoneNo, rollNo):
        print(self.message)
        print('Name:'+' ' + name)
        print('Email:'+' ' + email)
        print('Phone No:'+' ' + phoneNo)
        print('Roll no:' + ' ' + rollNo)


Student_1 = UserInfo()
Student_1.userData('Zain Ahmed', 'zain.ahmed199524@gmail.com',
                   '03022408099', 'EP-1751098')
