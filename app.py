from data import validate_input, extra_data
from weather import get_location, get_temperature


def main():
    
    try:
        # Get location and check if valid
        location = get_location()

        # Return temperature of location
        temperature, data = get_temperature(location)

        print(f"The current temperature in {location} is: {temperature} degrees.")
        print()

        # Validate input
        status = validate_input()

        if not status:
            print("Goodbye.")
            return

        if status:
            result = extra_data(data)
        
        # Index into extra data
        time = result.get("local_time")
        condition = result.get("condition")
        windspeed = result.get("windspeed")

        print(f"The current time in {location} is {time}")
        print(f"The current condition in {location} is: {condition}")
        print(f"The windspeed in {location} is currently {windspeed} kph")
        print()

    except Exception as e:
        print(f"Error happened: {e}")


if __name__=="__main__":
    main()