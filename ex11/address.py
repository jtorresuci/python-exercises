class Address:
    def __init__(self, init_name, init_house_number, init_street, init_city, init_state, init_zip, init_apt_number = None):
        self._name = init_name
        self._house_number = init_house_number
        self._street = init_street
        self._apt_number = init_apt_number
        self._city = init_city
        self._zip = init_zip
        self._state = init_state
    
    def printAddress(self):
        print("Address", self._name, "is: ")
        print(self._house_number, self._street)
        print(f'{self._city}, {self._state} {self._zip}')

    def comesBefore(self, b):
        return int(self._zip) < int(b._zip)