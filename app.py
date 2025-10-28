import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Set API key
key = os.getenv("WEATHER_API")


def get_location():
    "Verify location by calling API on that location and check response code"

    while True:
        try:
            # Get location from user:
            location = input("Please enter a location: ").strip().capitalize()

            # Store location in url
            location_string = f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no"

            # Call API with location and check response
            response = requests.get(location_string)

            # If 200, then OK
            if response.status_code == 200:
                return location

            # If not 200, then reprompt for location.
            if response.status_code != 200:
                print(f"{location} is not a valid location, please try again. ")
                continue

        # Catch exceptions
        except Exception as e:
            print(f"error in getting location: {e}")
            raise



def get_temperature(location):
    "Access the api and return the temperature"

    # Url for calling get_weather API
    base_url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no"
    
    try:
        # Send GET request
        response = requests.get(base_url)

        # Format response to json for indexing
        data = response.json()

        # Index into temperature key
        temperature = data["current"]["temp_c"]

        return temperature

    # Catch exception
    except Exception:
        print(f"Error trying to get temperature for location!")
        raise    


def main():
    
    try:
        # Get location and check if valid
        location = get_location()

        # Return temperature of location
        temperature = get_temperature(location)

        # Print answer
        print(f"The current temperature in {location} is: {temperature} degrees.")

    except Exception as e:
        print(f"Error happened: {e}")


if __name__=="__main__":
    main()