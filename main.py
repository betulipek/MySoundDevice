import sounddevice as sd
import soundfile as sf
from tkinter import *
import numpy

def Voice_rec():
    fs = 48000
    duration = 8

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    return sf.write('my_Audio_file.flac', myrecording, fs)


master = Tk()

Label(master, text=" Voice Recoder : "
      ).grid(row=0, sticky=W, rowspan=10)

b = Button(master, text="Start", command=Voice_rec)
b.grid(row=0, column=2, columnspan=2, rowspan=2,
       padx=15, pady=15)

mainloop()