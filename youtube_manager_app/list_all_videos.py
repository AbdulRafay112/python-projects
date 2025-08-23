def list_all_videos(videos):
    """List all videos"""
    print('\n')
    print('*' * 23)
    for index , video in enumerate(videos , start=1) :
        print(f"{index}. Video Name : {video['video name']} , Video Duration : {video['video time']}")
    print('*' * 23)
    print('\n')