from pylab import *
from rtlsdr import *
import time

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sdr.center_freq = 88.2e6
sdr.gain = 45

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=0.5)
ax.set_xlabel('Frequency(MHz)')
ax.set_ylabel('Relative power (dB)')
ax.set_title('Power Spectral Density')

while True:
    samples = sdr.read_samples(256 * 1024)

    # Create a new figure and plot
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot([], [], lw=0.5)
    #ax.set_xlabel('Frequency (MHz)')
    #ax.set_ylabel('Relative power (dB)')
    #ax.set_title('Power Spectral Density')
    
    # Estimate and plot the PSD
    #psd(samples, NFFT=1024, Fs=sdr.sample_rate / 1e6, Fc=sdr.center_freq / 1e6)
    frequencies, psd = plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate / 1e6, Fc=sdr.center_freq / 1e6)
    # Update the plot
    plt.draw()
    plt.pause(0.001)  # Pause for 0.01 seconds
    
    # Check if the figure is closed
    if not plt.fignum_exists(fig.number):
        break

sdr.close()
