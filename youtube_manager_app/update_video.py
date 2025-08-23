# [(1 , {'video name': xyz , 'video time': xyz})] 
from save_data import save_data
from list_all_videos import list_all_videos
def update_video(videos):
    """Update video details e.g -> {name , time} provided index of a video"""
    list_all_videos(videos)
    index = int(input("Enter video number you wants to update: "))
    if index >= 1 and index <= len(videos):
        video_name = input("Enter Video Name: ")
        video_duration = input("Enter Video Duration: ")
        videos[index - 1] = {'video name' : video_name , 'video time' : video_duration}
        save_data(videos)
    else:
        print("invalid index selected")