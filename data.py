def other_data(input):
    "Checks if user is interested in getting more data about requested location."
    if input == "yes":
        return True
    else:
        print("Not valid input")
        return False


def get_more_data(data, location):
    try:
        local_time = data["location"]["localtime"]
        print(f"The time at {location} is: {local_time}")
        
        condition = data["current"]["condition"]["text"]
        windspeed = data["current"]["wind_kph"]
    
        print(f"The current condition is {condition}, with wind speed at {windspeed} kph.")

    
    except Exception as e:
        print(f"Error trying getting more data from JSON file: {e}")