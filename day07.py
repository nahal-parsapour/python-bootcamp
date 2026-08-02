# temp converter

print("Temperature Converter")

mode = input("Convert from (C)elsius or (F)arenheit? ").lower()

if mode == "c":
    c = foat(input("Enter temperature in Celsius: ")
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")

elif mode == "f"
    f = float(input("Enter temperature in Farenheit :")
    c = (f - 32) * 5/9
    print("f{f}°F = {c}°C")

else:
    print("Invalid mode")
