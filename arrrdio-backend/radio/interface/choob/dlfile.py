from pydub import AudioSegment
from pydub.playback import play
import subprocess

def play_process_init(link):
    dl_video_to_tmpfs(link)
    subprocess.run(['ffplay', ('E:\\tmp\\{article}.mp3'.format(article=link)), '-nodisp'])

def dl_audio_to_tmpfs(link):
    subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', '.\\{article}.%(ext)s'.format(article=link), link], shell=True)

def dl_audio_to_tmpfs(link):
    subprocess.run(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', 'E:\\tmp\\{article}.%(ext)s'.format(article=link), link], shell=True)

if __name__ == "__main__":
    a = input("Link:")
    print('E:\\tmp\\{article}.mp4'.format(article=a))
    play_process_init(a)