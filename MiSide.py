import pygame
import time
import psutil
import os
import sys

# 获取资源文件的路径，打包后用于访问嵌入的资源
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 会将资源解压到 _MEIPASS 路径中
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# 播放音乐的函数
def play_music(music_file):
    pygame.mixer.music.load(music_file)  # 加载音乐文件
    pygame.mixer.music.play()  # 播放音乐

# 检查游戏是否在运行的函数
def is_game_running(game_process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if game_process_name.lower() in proc.info['name'].lower():
            return True
    return False

# 设置游戏进程名称和音乐文件路径
game_process_name = "MiSideFull.exe"  # 游戏进程名称（根据实际进程名称填写）
music_file = get_resource_path("MiSIDE.mp3")  # 使用 get_resource_path 获取音乐文件的路径

# 设置音乐播放时长（单位：秒）
music_duration = 22   # 比如音乐播放 22 秒

print("脚本已启动，等待游戏启动...")

# 初始化 pygame
pygame.mixer.init()

# 持续监控游戏进程
while True:
    if is_game_running(game_process_name):  # 检查游戏是否在运行
        print(f"{game_process_name} 已启动，开始播放音乐！")
        play_music(music_file)  # 播放音乐
        time.sleep(music_duration)  # 等待指定的播放时长
        pygame.mixer.music.stop()  # 停止音乐
        print(f"音乐播放完毕，等待游戏退出...")

        # 等待游戏退出
        while is_game_running(game_process_name):
            time.sleep(1)  # 每秒检查一次，直到游戏关闭

        print(f"{game_process_name} 已关闭，准备监控下一次启动。")
    
    time.sleep(1)  # 每秒检查一次游戏进程
