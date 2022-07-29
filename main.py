import os
import moviepy.editor as moviepy
path_to_video = os.path.abspath('/home/webdev/Downloads/file_example_AVI_1920_2_3MG.avi')

clip = moviepy.VideoFileClip(path_to_video)
clip.write_videofile("/home/webdev/Downloads/file_example_AVI_1920_2_3MG.mp4")
# webm -i /home/webdev/Downloads/file_example_AVI_1920_2_3MG.avi
