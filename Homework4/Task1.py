def convert_cel_to_far(celsius):
    return round(celsius * 9/5 + 32, 2)
def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)
def main():
    temp_far = float(input("Enter a temperature in degrees Fahrenheit: "))
    temp_cel = convert_far_to_cel(temp_far)
    print(f"{temp_far}°F is {temp_cel}°C")
    temp_cel = float(input("Enter a temperature in degrees Celsius: "))
    temp_far = convert_cel_to_far(temp_cel)
    print(f"{temp_cel}°C is {temp_far}°F")

if __name__ == "__main__":
    main()
