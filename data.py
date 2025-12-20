def validate_input():
    "Checks if user is interested in getting more data about requested location."
    while True:
        answer = input("Do you want to know more? Type 'yes': ").strip().lower()
        print()
        
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Not valid input. Please type again")


def extra_data(data):
    try:
        local_time = data["location"]["localtime"]
        
        condition = data["current"]["condition"]["text"]
        windspeed = data["current"]["wind_kph"]

        indexed_data = {
            "local_time": local_time,
            "condition": condition,
            "windspeed": windspeed
        }
        return indexed_data
    
    except Exception as e:
        print(f"Error trying getting more data from JSON file: {e}")