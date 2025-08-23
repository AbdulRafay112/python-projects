from list_all_videos import list_all_videos
from save_data import save_data
def delete_video(videos) :
    """Delete a video from all videos provided index of the video"""
    list_all_videos(videos)
    index = int(input("Enter number of video you wants to delete: "))
    if index >= 1 and index <= len(videos):
        del videos[index-1]
        print(f"video successfully deleted at index {index}")
        save_data(videos)
    else:
        print("invalid index")
    