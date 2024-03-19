import moviepy.editor as mymovie
import os
import time


# 视频文件路径
video_path = './portrait_video/download/'

# 音频文件路径
songs_path = './portrait_video/songs/'

# 生成文件列表
#  创建视频列表
def read_video_name(path):
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
                # 添加到数组
                L.append(filePath)
    return L

# 创建音频列表
def read_music_name(path):
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
                # 添加到数组
                M.append(filePath)
    return M

video_list = read_video_name(video_path)
print(video_list)

music_list = read_music_name(songs_path)

for i, x in zip(video_list, music_list):
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    video = mymovie.VideoFileClip(i)
    music = mymovie.AudioFileClip(x)
    video = video.without_audio()
    video_length = video.duration
    music_length = music.duration
    print(video_length)
    print(music_length)

    if (video_length > music_length):
        video = video.subclip(0, music_length)
    elif (music_length > video_length):
        music = music.subclip(0, video_length)

    final_clip = video.set_audio(music)

    # final_clip.write_videofile('./outvideo/'+ now +'.mp4', codec='mpeg4', fps=60)
    final_clip.write_videofile('./portrait_video/out_video/'+ now +'.mp4', fps=60)


