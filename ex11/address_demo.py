from address import Address

a = Address("a", "2500", "University Drive", "Some City", "Some State", "12345")
b = Address("b", "12-1200", "College Blvd", "Other City", "Other State", "99102")


a.printAddress()
print("")
b.printAddress()
print("")

print("a comes before b is", a.comesBefore(b))

# class Address:
#     def __init__(self, init_name, init_house_number, init_street, init_city, init_state, init_zip, init_apt_number = None):
#         self._name = init_name
#         self._house_number = init_house_number
#         self._street = init_street
#         self._apt_number = init_apt_number
#         self._city = init_city
#         self._zip = init_zip
#         self._state = init_state
    
#     def printAddress(self):
#         print("Address", self._name, "is: ")
#         print(self._house_number, self._street)
#         print(f'{self._city}, {self._state} {self._zip}')

#     def comesBefore(self):
#         return True