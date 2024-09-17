from address import Address
from mailing import Mailing

to_address = Address("12345", "Moscow", "Gogolya", "1", "22")
from_address = Address("54321", "Tula", "Lenina", "2", "33")
mailing = Mailing(to_address, from_address, "5000", "98765432109")

print(mailing)
