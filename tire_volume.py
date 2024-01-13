import math
import datetime

def calculate_tire_volume(width, ratio, diameter):
    if ratio > 0.5:
        volume = math.pi * width * ratio * (width * ratio + 2 * diameter * math.pi) / 1000000
    else:
        volume = math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / 10000000
    volume = round(volume, 2)
    return volume

def main():
    print("This program computes and outputs the")

    # Get user input for tire dimensions
    width = float(input("Enter the width of the tire in mm: "))
    ratio = float(input("Enter the aspect ratio of the tire: "))
    diameter = float(input("Enter the diameter of the wheel in inches: "))

    volume = calculate_tire_volume(width, ratio, diameter)

    # Display the result
    print(f"The approximate volume is {volume} liters")

    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Append data to the volumes.txt file
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {ratio}, {diameter}, {volume}\n")

if __name__ == "__main__":
    main()