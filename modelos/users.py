from modelos.address import Address as add
from modelos.company import Company as cia

class User(add, cia):
    def __init__(self, iduser = 0, nameuser = '', username = '', email = '', phone = '', website = '', idaddress = 0, idcompany = 0):
        super().__init__(idaddress)
        super().__init__(idcompany)
        self.iduser = iduser
        self.nameuser = nameuser
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website