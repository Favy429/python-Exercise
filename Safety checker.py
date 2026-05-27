#Build a chemical safety checker: ask for temperature and pressure.
#Print the safety level using at least 4 conditions.
temperature = float(input("Enter temperature in celsius:"))
pressure = float(input("Enter pressure in atm:"))
if temperature <0 and pressure <2:
    print("Safety level: Low")
elif temperature <0 and pressure >=2:
    print("Safety level: Moderate") 
elif temperature  >=0 and pressure <2:
    print("Safety level: Moderate")
elif temperature >=0 and pressure >=2:
    print("Safety level: High")
print("=== Chemical Safety Checker ===")

# Ask user for inputs
temperature = float(input("Enter temperature (°C): "))
pressure = float(input("Enter pressure (atm): "))

# Safety checks
if temperature < 0:
    print("Safety Level: LOW")
    print("Chemical is too cold. Monitor storage conditions.")

elif temperature <= 50 and pressure <= 2:
    print("Safety Level: SAFE")
    print("System operating normally.")

elif temperature <= 100 and pressure <= 5:
    print("Safety Level: WARNING")
    print("Elevated conditions detected. Increase monitoring.")

elif temperature <= 150 or pressure <= 8:
    print("Safety Level: DANGER")
    print("High risk of instability. Reduce heat and pressure.")

else:
    print("Safety Level: CRITICAL")
    print("Emergency shutdown required!")

print("=== Chemical Efficiency Checker ===")

# User inputs
temperature = float(input("Enter temperature: "))
pressure = float(input("Enter pressure: "))

# Starting efficiency
efficiency = 95

# Check temperature range
if temperature < 200 or temperature > 300:
    efficiency -= 5

# Check pressure range
if pressure < 80 or pressure > 120:
    efficiency -= 5

# Display result
print(f"System Efficiency: {efficiency}%")

safe = True
ph = float(input("Enter pH level: "))

# pH check
if ph < 6:
    print("⚠️ Solution is too ACIDIC.")
    safe = False

elif ph > 8:
    print("⚠️ Solution is too ALKALINE.")
    safe = False

else:
    print("✅ pH is within safe range.")

# Overall system status
print("\n--- Overall Status ---")

if safe:
    print("🟢 SYSTEM SAFE")
else:
    print("🔴 SYSTEM UNSAFE - Immediate attention required.")
