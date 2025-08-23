from load_data import load_data
from update_video import update_video 
from list_all_videos import list_all_videos 
from delete_video import delete_video 
from add_video import add_video 

def main():
    """Main function Where we can take input from users and can show them according to the input"""
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1- List all youtube Videos ")
        print("2- Add a youtube Video ")
        print("3- update a youtube video details ")
        print("4- Delete a Youtube Video ")
        print("5- Exit the app ")
        choice = input("Enter Your Choice: ")
        match choice :
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break 
            case _ :
                print("Invalid Choice")

if __name__ == "__main__":
    main()