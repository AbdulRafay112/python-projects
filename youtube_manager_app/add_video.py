from save_data import save_data
def add_video(videos):
    """Add a video in a file"""
    video_name = input("Enter Video Name: ")
    video_time = input("Enter Video Time: ")
    videos.append({'video name' : video_name , 'video time' : video_time})
    save_data(videos)
    print(f"video added successfully {video_name} , {video_time}")

