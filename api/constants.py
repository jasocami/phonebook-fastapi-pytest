from enum import Enum

CONTACTS = [
    {'id': 1, 'name': "Hashim Moran", 'phone': "+34394352323"},
    {'id': 2, 'name': "Yoko Owens", 'phone': "+34959777373"},
    {'id': 3, 'name': "Thaddeus Barnett", 'phone': "+34482937186"},
    {'id': 4, 'name': "Ciaran Austin", 'phone': "+34804763842"},
    {'id': 5, 'name': "Summer Holland", 'phone': "+34172670430"}
]


class PhoneTypes(str, Enum):
    mobile = 'mobile'
    home = 'home'
    work = 'work'
    other = 'other'
