from cs101audio import *
import sys

print("Press 1 for Drivers License")
print("Press 2 for Levitating")
print("Press 3 to hear a drum sample")
choice = input("Please select a song: ")

song = Audio()

if choice == "1":
    song.open_audio_file("drivers_license.wav")
elif choice == "2":
    song.open_audio_file("levitating.wav")
elif choice == "3":
    song.open_audio_file("Bass-Drum-1.wav")
else:
    print("Hey, you didn't select one of the input options!")
    sys.exit()
    
song.play()


### Want to play all 3 at the same time
song.open_audio_file("drivers_license.wav")
levitating = Audio()
levitating.open_audio_file("levitating.wav")
drum = Audio()
drum.open_audio_file("Bass-Drum-1.wav")

levitating.apply_gain(-15)

song.overlay(levitating)
song.overlay(drum)

levitating.play()


