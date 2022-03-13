from moviepy.editor import VideoFileClip
import shutil

def ConvertToMp3(mp4file, mp3file):
    """Метод, преобразовывающий видео в аудио целиком"""
    video=VideoFileClip(mp4file)
    # получаем аудиодорожку
    audio=video.audio
    # сохраняем аудио файл
    audio.write_audiofile(mp3file)
    # уничтожаем объекты чтобы не было ошибок
    audio.close()
    video.close()
    print('[INFO] Видео было конвертировано')

def converttomp3Double(mp4file, mp3file, starttime, endtime):
    """Метод, позволяющий преобразовывать видео в аудио"""
    video=VideoFileClip(mp4file).subclip(starttime, endtime)
    # получаем аудиодорожку
    audio=video.audio
    # сохраняем аудио файл
    audio.write_audiofile(mp3file)
    # уничтожаем объекты 
    # чтобы не было ошибок
    audio.close()
    video.close()
    print('[INFO] Видео было конвертировано')


def MoveFileToSource(path: str):
    """Перемешает полученный результат туда, где находится оригинал видео"""
    path = path.replace("MP4", "mp3")
    file_name = path.split("/")
    move_to = path.replace(file_name[:-1], "")
    print(move_to)
    # shutil.move(path, move_to)
    print("[INFO] File has been moved")


print('Вставьте путь к файлу:')
# Перерабатываю путь к файлу в понятный для скрипта путь
path_to_file = input().replace(f"\"", "").replace("C", "c", 1).replace(":", "", 1).replace("\\", "/")
path_to_file = "/mnt/" + path_to_file

# Разделяю путь к файлу для получения имени
file_name = path_to_file.split("/")
final_name = file_name[-1].replace("mp4", "mp3").replace("MP4", "mp3")

result = input()
if (result == "1"):
    # Обработка видео в аудио и перемешение его туда, где находится основной файл
    print("Start time in seconds: ")
    starttime = input()
    print("End time in seconds: ")
    endtime = input()
    converttomp3Double(path_to_file, final_name, starttime, endtime)
    move_to = path_to_file.replace(file_name[-1], "")
    shutil.move(final_name, move_to)
else:
    # Обработка видео в аудио и перемешение его туда, где находится основной файл
    ConvertToMp3(path_to_file, final_name)
    move_to = path_to_file.replace(file_name[-1], "")
    shutil.move(final_name, move_to)


# "C:\Users\62427\Desktop\audio.mp3"
# /mtn/c/Users/62427/Desktop/audio.mp4