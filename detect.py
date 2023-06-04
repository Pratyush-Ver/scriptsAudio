import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

x=list(range(1,220161))

# Load audio file
audio_file = 'output.wav'
y_init, sr_init = librosa.load(audio_file)
print("sr is ",sr_init)
print("y is",y_init)
# Plot waveform of amplitude vs time
#plt.figure(figsize=(14, 5))
fig, ax = plt.subplots(nrows=3, sharex=True)
librosa.display.waveshow(y_init, sr=sr_init, ax=ax[0])
ax[0].set(title='Envelope view, mono')
ax[0].label_outer()

# plt.plot(y_init,x)
# plt.show

# Set loudness threshold
threshold = 0.01

# Find timestamps when the sound goes over the threshold
onset_frames = librosa.onset.onset_detect(y=y_init, sr=sr_init)
onset_times = librosa.frames_to_time(onset_frames, sr=sr_init)
print(y_init.shape)
print("onset times are ",onset_times)
# Print timestamps when the sound goes over the threshold
for onset_time in onset_times:
    if int(onset_time * sr_init) < len(y_init) and y_init[int(onset_time * sr_init)] > threshold:
        print(onset_time)