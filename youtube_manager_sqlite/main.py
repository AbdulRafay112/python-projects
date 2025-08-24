import sqlite3
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def listing_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
def add_video(name , time):
    cursor.execute("INSERT INTO videos (name , time) VALUES (?, ?)" , (name , time))
    conn.commit()
def update_video(id , new_name , new_time):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?" , (new_name , new_time , id))
    conn.commit()
def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?" , (id , )) 


def main():
    """Main function serve as home for our app"""
    while True:
        print("Youtube Manager App | Choose An Option")
        print("1- Listing All Youtube Videos")
        print("2- Add A Youtube Video")
        print("3- Update A Youtube Video")
        print("4- Delete A Youtube Video")
        print("5- Exit The Loop")
        choice = input("Enter Your Choice: ")
        if choice == '1':
            listing_all_videos()
        elif choice == '2':
            name= input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            add_video(name , time)
        elif choice == '3':
            id = input("Enter video Id You wants to Update: ")
            new_name = input("Enter New Video Name: ")
            new_time = input("Enter new Video Time: ")
            update_video(id , new_name , new_time)
        elif choice == '4':
            id = input("Enter Youtube Video Id You wants to delete: ")
            delete_video(id)
        elif choice == '5':
            break 
        else:
            print("Invalid Choice")
    conn.close()
if __name__ == "__main__":
    main()