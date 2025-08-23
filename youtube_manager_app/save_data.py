import json 
def save_data(videos):
    """Helper function to save data in a file"""
    with open('youtube.txt' , 'w') as file :
        json.dump(videos , file)
