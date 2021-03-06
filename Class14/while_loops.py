from cs101audio import *

## We want to repeatedly play the snare sample for 4 seconds

snare = Audio()
snare.open_audio_file("Snare.wav")

four_second_snare = Audio()
taps = 0

while len(four_second_snare) < 4000:
    four_second_snare += snare
    taps += 1


print("The length in ms is", len(four_second_snare))
print("The number of snare taps is", taps)

four_second_snare.play()
