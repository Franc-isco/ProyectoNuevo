from modelos.geo import Geo

class Address(Geo):
    def __init__(self, idaddress = 0, street = '', suite = '', city = '', zipcode = '', idgeo = 0):
        super().__init__(idgeo)
        self.idaddress = idaddress
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode