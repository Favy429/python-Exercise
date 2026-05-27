# converting units of temperature, pressure, mass etc

#converting temperature from celsius to fahrenheit and kelvin
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius  + 273.15
print(f"{celsius}℃ to {fahrenheit}°F")
print(f"{celsius}℃ to {kelvin}K")


#converting pressure from atm to kilopascals
atm = float(input("Enter pressure in atm: "))
kilopascals = atm * 101.325
print(f"{atm} atm to {kilopascals} kPa")


#converting mass from KG to Ibs
KG = float(input("Enter mass in KG:"))
Ibs = KG * 2.20462
print(f"{KG} KG to {Ibs} Ibs")







