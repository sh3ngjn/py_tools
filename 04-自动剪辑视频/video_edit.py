import moviepy.editor as mymovie
import os
import time
import random


now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
# 视频文件路径
video_path = './download_video/'

# 音频文件路径
songs_path = './songs/Relax/'

# 打印时间戳
# c_time = time.strftime("%Y-%M-%T-%H", time.localtime())
# print(c_time)

#  创建视频列表
def read_video(path):
    L = [] 
    # 访问 video 文件夹 (假设视频都放在这里面)
    for root, dirs, files in os.walk(path):
        # 按文件名排序
        files.sort()
        # 遍历所有文件
        for file in files:
            # 如果后缀名为 .mp4
            if os.path.splitext(file)[1] == '.mp4':
                # 拼接成完整路径
                filePath = os.path.join(root, file)
                # 载入视频
                video = mymovie.VideoFileClip(filePath)
                # 添加到数组
                L.append(video)
    r_L = random.sample(L, 10)
    return r_L


# 创建音频列表
def read_music(path):
    M = []
    # 访问 music 文件夹 
    for root, dirs, files in os.walk(path):
        # 按文件名排序
        files.sort()
        # 遍历所有文件
        for file in files:
            # 如果后缀名为 .mp3
            if os.path.splitext(file)[1] == '.mp3':
                # 拼接成完整路径
                filePath = os.path.join(root, file)
                # 载入音频
                audio = mymovie.AudioFileClip(filePath)
                # 添加到数组
                M.append(audio)
    r_M = random.sample(M, 20)    
    return r_M

# 生成视频列表
video_list = read_video(video_path)


# 生成音频列表
music_list = read_music(songs_path)

# 拼接视频
video_clip = mymovie.concatenate_videoclips(video_list)
video_clip = video_clip.without_audio()
# 拼接音频
music_clip = mymovie.concatenate_audioclips(music_list)

video_length = video_clip.duration
music_length = music_clip.duration
print(video_length)
print(music_length)

if (video_length > music_length):
    video_clip = video_clip.subclip(0, music_length)
elif (music_length > video_length):
    music_clip = music_clip.subclip(0, video_length)

final_clip = video_clip.set_audio(music_clip)

# final_clip.write_videofile('./outvideo/'+ now +'.mp4', codec='mpeg4', fps=60)
final_clip.write_videofile('./outvideo/'+ now +'.mp4', fps=60)