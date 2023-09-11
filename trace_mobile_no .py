import phonenumbers
from phonenumbers import timezone , geocoder ,carrier

number = input("enter number with +__: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone , "en")
registeration = geocoder.description_for_number(phone , "en")

print(phone)
print(time)
print(car)
print(registeration)