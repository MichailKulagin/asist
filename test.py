'''
import torch
import sounddevice as sd
import time
language = 'ru'
model_id = 'v3_1_ru'
sample_rate = 48000
speaker = 'baya'# xenia aidar baya
put_accent = True
put_yo = True
device = torch.device('cpu')#cpu
input_text = input('Введите предложение которое нужго озвучить: ')
text=input_text


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

пишет слово но только на английском
pag.typewrite("пивет", 0.1)

жмет на ентер
pag.typewrite(['enter'])
'''

import pyautogui as pag
import time
import keyboard as kb
#pag.FAILSAFE = False

text = input('Введите предложение которое   нужго вписать: ')

#pag.typewrite("hihi", 0.1)
#pag.typewrite(['enter'])
time.sleep(2)

kb.write(text)
pag.typewrite(['enter'])
print("Все ок")