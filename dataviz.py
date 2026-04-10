import numpy as np
import pandas as pd
import librosa as lb
import matplotlib.pyplot as plt
import scipy

# load audio sample, None keeps the original sample rate
data, sample_rate = lb.load("data/01 - Divinity.flac", sr=11250, duration=0.065) # fourth of a second clip @ 11.25khz
data_sample_size = len(data)

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
lb.display.waveshow(data, sr=sample_rate, color="red",ax=ax1)
ax2.hist(data,bins=35)
ax1.set_title("Waveform of Divinity Sample")
ax1.set_xlabel("Time (S)")
ax1.set_ylabel("Amplitude")
ax2.set_title("Distribution of Amplitudes")
ax2.set_xlabel("Amplitude")
ax2.set_ylabel("Frequency")
plt.show()

