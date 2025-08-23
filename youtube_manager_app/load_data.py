import json 
def load_data():
    """Load data from the file and return in the form of array if file not found empty array will return """
    try:
        with open("youtube.txt" , 'r') as file:
            return json.load(file)
    except FileNotFoundError :
        print("file not found")
        return []