def celsius_to_fahrenheit(temperature):
    return (temperature * 9 / 5) + 32

temperature = int(input("Enter temperate in celsius: "))
print("Fahrenheit temperature: ", celsius_to_fahrenheit(temperature))

