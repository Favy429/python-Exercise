<<<<<<< HEAD
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


# Refactoring into functions with docstrings and a main() function
def celsius_to_fahrenheit (celsius):
    """convert celsius to fahrenheit"""
    return celsius * 9/5 + 32

def celsius_to_kelvin (celsius):
    """convert celsisius to kelvin"""
    return celsius + 273.15

def atm_to_kilopascals (atm):
    """convert atm to kilopascals"""
    return atm * 101.325

def kg_to_Ibs (kg):
    """convert kg to Ibs"""
    return kg * 2.20462

def main():
    celsius = float(input("Enter temperature in celsius: "))
    print(f"{celsius}℃ to {celsius_to_fahrenheit(celsius)}°F")
    print(f"{celsius}℃ to {celsius_to_kelvin(celsius)}K")
    
    atm = float(input("Enter pressure in atm:"))
    print(f"{atm}atm to {atm_to_kilopascals(atm)}kPa")

    kg = float(input("Enter mass in KG: "))
    print(f"{kg} KG to {kg_to_Ibs(kg)} Ibs")

if __name__  == "__main__":
        main()





=======
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







>>>>>>> 178fe70811b07436c2d1f87ec6f97ef2e30d6fba
