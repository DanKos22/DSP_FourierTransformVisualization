# -*- coding: utf-8 -*-
"""
@author: Dan Koskiranta
"""

import numpy as np
import matplotlib.pyplot as plt

# Create signal x
# Add code
x = np.array([0, 1, 0, -1])
#x = np.array([0, 1.73, 0, 0, 0, -1.73])
# Print x
# Add code
print(x)

# Add comments to the following lines of code
N = x.size    #N is the total number of samples
fs = 4        #fs is the sampling frequency
n = np.arange(0, N)  # n is an array of time domain indices
nT = n/fs            

# Calculate FFT of x
# Add code
y = np.fft.fft(x)
# Print FFT of x
# Add code
print(y)
# Calculate magnitude of FFT 
# Add code
y_abs = np.abs(y)
# Print magnitude of FFT
# Add code
print(y_abs)
# Calculate the frequencies for x-axis of FFT plot
# Add code
# Frequencies are multiples of Fs/N, where N is the number of samples
freqs = np.fft.fftfreq(N, 1/fs)
# Calculate the inverse FFT
inv = np.fft.ifft(y)
# Print the inverse FFT
# Add code
#print(inv)

# Plot code
fig = plt.figure(figsize = (12, 10))
ax = fig.add_subplot(2, 1, 1)
markerline, stemlines, baseline = ax.stem(nT, x)
plt.setp(stemlines, color='k', linewidth=1)
plt.setp(baseline, color='k', linewidth=2)
plt.setp(markerline, color='k', markersize=5)
ax.tick_params(axis='both', which='both', labelsize=16, length=0, pad=15)
ax.set_yticks([-1, 0, 1])
ax.set_xlabel('Time (s)', fontsize=20, labelpad=15)
ax.set_ylabel('Signal Magnitude', fontsize=20, labelpad=15)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.set_title('Time-Domain Signal', fontsize=20, color='sienna', pad=15)
ax = fig.add_subplot(2, 1, 2)
ax.set_xlabel('Frequency')
ax.set_ylabel('DFT Magnitude')
ax.set_title('DFT')
markerline, stemlines, baseline = ax.stem(freqs, y_abs)
plt.setp(stemlines, color='k', linewidth=1)
plt.setp(baseline, color='k', linewidth=2)
plt.setp(markerline, color='k', markersize=5)
ax.tick_params(axis='both', which='both', labelsize=16, length=0, pad=15)
ax.set_xlabel('Frequency (Hz)', fontsize=20, labelpad=15)
ax.set_ylabel('DFT Magnitude', fontsize=20, labelpad=15)
ax.set_title('Frequency-Domain Signal', fontsize=20, color='sienna', pad=15)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
plt.subplots_adjust(hspace = 0.5)

