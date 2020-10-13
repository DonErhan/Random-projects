#####################################################################
#        Module to create basic random data                         #
#####################################################################

import random

# Populate lists with fake data
first_names = ['Adna', 'Anca', 'Andreea', 'Angelica', 'Anghel', 'Anica', 'Aniela', 'Anisoara', 'Antoaneta', 'Apostol', 'Augustina', 'Aurelia', 'Aurica', 'Aurora', 'Basarab', 'Bogdan', 'Calin', 'Carmen', 'Cecilia', 'Cezar', 'Ciprian', 'lena', 'Eugen', 'Eugenia', 'Felicia']

last_names = ['Damaschin', 'Dănceanu', 'Danciu', 'Dănescu', 'Dănișor', 'Dăscălescu', 'Dascălu', 'Datcu', 'Gheorghe', 'Davidovici', 'Dărănuța', 'Deac', 'Dediu', 'Dejeu', 'Geambașu', 'Geiculescu', 'Georgescu', 'Gheorghilaș', 'Gheorghiu', 'Gherghel', 'Gherghescu', 'Ghideanu', 'Ghinea', 'Lazar', 'Ciobanu']

street_names = ['Trandafirului', 'Balcani', 'Mircea cel Bătrîn', 'Alba Iulia', 'Albișoara', 'Albița', 'Aleksandr Pușkin', 'Cedar', 'Calea Orheiului', 'Chicago', 'Armoniei', 'Armenească']

fake_cities = ['Anenii Noi', 'Basarabeasca', 'Chisinau', 'Cahul', 'Cantemir', 'Călărași', 'Căușeni', 'Cimișlia', 'Criuleni', 'Dondușeni', 'Drochia', 'Dubăsari', 'Edineț', 'Fălești', 'Florești', 'Glodeni', 'Hîncești', 'Ialoveni', 'Leova', 'Nisporeni', 'Ocnița', 'Orhei', 'Rezina', 'Rîșcani', 'Sîngerei']

# Get Email
def get_random_email_and_name(get):
    for i in range(get):
        first = random.choice(first_names)
        last = random.choice(last_names)
        email = first.lower() + last.lower() + '@gmail.com'
        names = first.capitalize() + " " +  last.capitalize()
        print(email)
        print(names)

# Get Address
def get_random_address(get):
    for i in range(get):
        street_num = random.randint(1, 300)
        street = random.choice(street_names)
        city = random.choice(fake_cities)
        zip_code = random.randint(2000, 2999)
        address = f'Or.{city}, St.{street} {street_num}, MD-{zip_code}'
        print(address)

# Get phone number
def get_phone_number(get):
    for i in range(get):
        phone = f'(+373) {random.randint(691, 696)}-{random.randint(100, 999)}-{random.randint(100,999)}'
        print(phone)

       

get_random_address(1)
get_random_email_and_name(1)
get_phone_number(1)
