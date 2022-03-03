from moviepy import VideoFileClip

def ConvertToMp3(mp4file, mp3file):
    """Метод, преобразующий видео в аудио целиком"""
    video = VideoFileClip(mp4file)
    audio = video.audio
    audio.write_audiofile(mp3file)
    audio.close()
    video.close()
    print('[INFO] Видео было успешно конвертировано в аудио-файл')

    