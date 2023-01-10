from pytube import YouTube
import pyautogui as pygui

link = pygui.prompt("Coloca el link de el video que quieres descargar: ", title="YT Downloader")

YouTube(link).streams.first().download()

pygui.alert(f"""{YouTube(link).title}
Descargado correctamente!""", title="YT Downloader")
