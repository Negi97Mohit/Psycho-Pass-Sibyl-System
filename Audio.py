# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:12:30 2021

Author: Mohit Negi

"""

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft,ifft


fs=44100 #sample rate
seconds=10 # Duration of recording

myrecording=sd.rec(int(seconds*fs),samplerate=fs,channels=2)
sd.wait()  #wait until reording is finished
print(myrecording.shape)
y=fft(myrecording)
print(y)
plt.figure(1)
plt.plot(y)
write('output.wav',fs,myrecording)
plt.figure(2)
plt.title("Signal Wave")
plt.plot(myrecording)
plt.show()




