<<<<<<< HEAD
Celsius = float(input("enter temperature in Celsius: "))
fahrenheit_F = (Celsius * 9/5) + 32
print(f"Converting {Celsius}°C celsius to {fahrenheit_F}°F")
kelvin = Celsius + 273.15
print(f"Converting {Celsius: .2f}°C to {fahrenheit_F: .2f}°F")
print(f"Converting {Celsius: .2f}°C to {kelvin: .2f}K")
user_input = input("Enter Celsius temperature (or 'exit'): ")

if user_input.lower() == "exit":
    print("Goodbye!")
else:
    Celsius = float(user_input)

    fahrenheit_F = (Celsius * 9/5) + 32
    kelvin = Celsius + 273.15
    
    print(f"Converting {Celsius: .2f}°C to {fahrenheit_F: .2f}°F")
    print(f"Converting {Celsius: .2f}°C to {kelvin: .2f}K")

while True:
    user_input = input("Enter Celsius temperature (or 'exit'): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    Celsius = float(user_input)

    fahrenheit_F = (Celsius * 9/5) + 32
    kelvin = Celsius + 273.15

    print(f"Converting {Celsius: .2f}°C to {fahrenheit_F: .2f}°F")
    print(f"Converting {Celsius: .2f}°C to {kelvin: .2f}K")
    print()

temperature = 100
print(f"The Boiling point of water is {temperature}℃")



=======
Celsius = float(input("enter temperature in Celsius: "))
fahrenheit_F = (Celsius * 9/5) + 32
print(f"Converting {Celsius}°C celsius to {fahrenheit_F}°F")
kelvin = Celsius + 273.15
print(f"Converting {Celsius: .2f}°C to {fahrenheit_F: .2f}°F")
print(f"Converting {Celsius: .2f}°C to {kelvin: .2f}K")
user_input = input("Enter Celsius temperature (or 'exit'): ")

if user_input.lower() == "exit":
    print("Goodbye!")
else:
    Celsius = float(user_input)

    fahrenheit_F = (Celsius * 9/5) + 32
    kelvin = Celsius + 273.15
    
    print(f"Converting {Celsius: .2f}°C to {fahrenheit_F: .2f}°F")
    print(f"Converting {Celsius: .2f}°C to {kelvin: .2f}K")

while True:
    user_input = input("Enter Celsius temperature (or 'exit'): ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    Celsius = float(user_input)

    fahrenheit_F = (Celsius * 9/5) + 32
    kelvin = Celsius + 273.15

    print(f"Converting {Celsius: .2f}°C to {fahrenheit_F: .2f}°F")
    print(f"Converting {Celsius: .2f}°C to {kelvin: .2f}K")
    print()

temperature = 100
print(f"The Boiling point of water is {temperature}℃")



>>>>>>> 178fe70811b07436c2d1f87ec6f97ef2e30d6fba
