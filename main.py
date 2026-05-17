import os

from dotenv import load_dotenv, dotenv_values
load_dotenv

#### Assigning environment variables to variables in order to easily work with them. ####
desktop_dir = os.getenv("DESKTOP_DIR")
document_dir = os.getenv("DOCUMENT_DIR")
music_dir = os.getenv("MUSIC_DIR")
picture_dir = os.getenv("PICTURE_DIR")
video_dir = os.getenv("VIDEO_DIR")

###Looping through desktop directory & listing files. Also checking if the first character is '.' and 
# if it is, ignore it.###
for file in os.listdir(desktop_dir): 
    print(file)

