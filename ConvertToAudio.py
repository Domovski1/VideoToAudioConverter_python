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




def CutAndConvert(mp4file, mp3file, starttime, endtime):
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



def ConvertTimeToSeconds(insert_time):
    """Получает время на вход и возвращает результат в секундах"""
    all_time = insert_time.split(":")

    if len(all_time) > 2:
        if int(all_time[1]) > 60 or int(all_time[2] > 60):
            print("Входные данные имели неверные формат")
            exit()
        hour = int(all_time[0]) * 3600
        minutes = int(all_time[1]) * 60
        seconds = int(all_time[2])
        return hour + minutes + seconds
    elif len(all_time) > 1:
        if int(all_time[0]) > 60 or int(all_time[1]) > 60:
            print("Входные данные имели неверные формат")
            exit()
        minutes = int(all_time[0]) * 60
        seconds = int(all_time[1])
        result_time = minutes + seconds
        return result_time
    else:
        seconds = all_time[0]
        if seconds > 60:
            print("неверно указано время")
            exit()
        result_time = seconds
        return result_time


print('Вставьте путь к файлу:')
# Перерабатываю путь к файлу в понятный для скрипта путь
path_to_file = input().replace(f"\"", "").replace("C", "c", 1).replace(":", "", 1).replace("\\", "/")
path_to_file = "/mnt/" + path_to_file

# Разделяю путь к файлу для получения имени
file_name = path_to_file.split("/")
final_name = file_name[-1].replace("mp4", "mp3").replace("MP4", "mp3")

print('1 - Чтобы вырезать время и конвертировать его')
print('2 - Чтобы конвертировать целиком')
result = input()


if (result == "1"):
    # Обработка видео в аудио и перемешение его туда, где находится основной файл
    print("Введите время, с которой нужно начать обрезать видео: ")
    starttime = input()
    starttime = ConvertTimeToSeconds(starttime)
    

    print("End time in seconds: ")
    endtime = input()
    endtime = ConvertTimeToSeconds(endtime)
    CutAndConvert(path_to_file, final_name, starttime, endtime)
    move_to = path_to_file.replace(file_name[-1], "")
    shutil.move(final_name, move_to)


else:
    # Обработка видео в аудио и перемешение его туда, где находится основной файл
    ConvertToMp3(path_to_file, final_name)
    move_to = path_to_file.replace(file_name[-1], "")
    shutil.move(final_name, move_to)


# "C:\Users\62427\Desktop\audio.mp3"
# /mtn/c/Users/62427/Desktop/audio.mp4