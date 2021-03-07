import matplotlib.pyplot as plt
from cs101audio import *

### Let's plot the predicted high temperatures for the next week:
days = ["Fri", "Sat", "Sun", "Mon", "Tues", "Wed", "Thurs"]
highs = [ 26,   21,     26,    38,     47,    57,    53]

# First, let's make a bar chart
# plt.bar(days, highs)
# plt.show()

# Make a line chart!
plt.plot(days, highs)
# plt.show()

lows = [14,   13,   10,       31,      36,   47,    37]

plt.plot(days, lows)
plt.legend(("High Temp", "Low Temp"))

plt.show()


### Plot some x-y pairs for the function y = 2^x

x_values = []
y_values = []
for x in range(15):
    x_values.append(x)
    y = 2 ** x
    y_values.append(y)
    
# print(x_values)
# print(y_values)

plt.plot(x_values, y_values, color="orange", marker="o", linestyle="none")

plt.plot(x_values, y_values, color="green")

plt.show()


### Create some audio and visualize it
### Start with an old Nintendo song
zelda = Audio()
zelda.open_audio_file("zelda.wav")
# zelda.play()

# ms_100 = zelda[100:200]
ms_5 = zelda[100:105]

# ms_100.play()
ms_5.play()

### This will give us the actual audio samples
sample_list = ms_5.get_sample_list()

# print(sample_list)
# print(len(sample_list))

plt.plot(sample_list)
plt.show()


### Do the same thing with generated audio

wave = generate_music_note("c4", 500, "sawtooth")
wave.play()

wave_samples = wave.get_sample_list()
plt.plot(wave_samples)
plt.show()

# Let's zoom in:
short_wave = wave_samples[5000:5440]
plt.plot(short_wave)
plt.show()


### Visualize a snare drum
snare = Audio()
snare.open_audio_file("Snare.wav")

snare.play()
sample_list = snare.get_sample_list()
print(len(sample_list))

plt.plot(sample_list[2000:3000])
plt.show()




