from pytubefix import YouTube
from pytubefix.cli import on_progress
import yt_dlp
from pydub import AudioSegment

# URL do vídeo
url = "https://www.youtube.com/watch?v=iKBCVZqqooY"

# Diretório de destino para salvar o vídeo
destinoVideos = "videos"
destinoMusica = "audios"


### FORMATADO EM MP4
yt = YouTube(url, on_progress_callback=on_progress) # Cria o objeto YouTube
print(f"Título do vídeo: {yt.title}") # Exibe o título do vídeo
ys = yt.streams.get_highest_resolution() # Obtém o stream de maior resolução
ys.download(output_path=destinoVideos) # Faz o download do vídeo
print("Download concluído!")


'''
### FORMATADO EM M4A
yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)
ys = yt.streams.get_audio_only()
ys.download(output_path=destinoMusica)
'''



# ESSE TRECHO USA A BIBLIOTECA FFMPEG PARA BAIXAR EM FORMATO MP3
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'ffmpeg_location': 'bin/ffmpeg.exe',  # Caminho relativo para o FFmpeg
    'outtmpl': 'audios/%(title)s.%(ext)s',
}

# Realiza o download
with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])

teste = 'um' 
match teste:
    case 'um':
        print(teste)


