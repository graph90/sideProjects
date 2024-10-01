def calculate_distance(distance_ly):
    speed_of_light = 299792  # km/s
    seconds_per_year = 365.25 * 24 * 60 * 60
    distance_km = distance_ly * speed_of_light * seconds_per_year
    return distance_km

def main():
    try:
        distance_ly = float(input("Enter the distance from Earth to the center of the Milky Way in light-years: "))
        distance_km = calculate_distance(distance_ly)
        print(f"The distance to the center of the Milky Way is approximately {distance_km:.2e} kilometers.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
