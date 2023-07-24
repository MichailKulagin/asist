import pyttsx3		#pip install pyttsx3


#Инициализация голосового "движка" при старте программы
#
#Голос берется из системы, первый попавшийся
#
#Доп материал:
#https://pypi.org/project/pyttsx3/
#https://pyttsx3.readthedocs.io/en/latest/
#https://github.com/nateshmbhat/pyttsx3
#На Linux-ax, скорее всего нужно еще:
#sudo apt update && sudo apt install espeak ffmpeg libespeak1

engine = pyttsx3.init()
engine.setProperty('rate', 180)				#скорость речи


def speaker(text: object) -> object:
	'''Озвучка текста'''
	engine.say(text)
	engine.runAndWait()
"""
import torch
import sounddevice as sd
import time
def speaker(text: object) -> object:
	language = 'ru'
	model_id = 'v3_1_ru'
	sample_rate = 48000
	speaker = 'xenia'# xenia aidar baya
	put_accent = True
	put_yo = True
	device = torch.device('cpu')#cpu
	text=text
	model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
										model='silero_tts',
										language=language,
										speaker=model_id)
	model.to(device)  # gpu or cpu

	audio = model.apply_tts(text=example_text,
							speaker=speaker,
							sample_rate=sample_rate)
						
	print("Все ок")

	audio = model.apply_tts(text=text,
							speaker=speaker,
							sample_rate=sample_rate,
							put_accent= put_accent,
							put_yo=put_yo)

	print(text)
	sd.play(audio, sample_rate)
	time.sleep(len(audio)/sample_rate)
	sd.stop()

"""