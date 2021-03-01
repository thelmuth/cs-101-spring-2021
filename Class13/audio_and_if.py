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
  
### Make every other second of the song loud, and every other second soft

# loud_and_soft = Audio()
# for index in range(0, len(song), 1000):
#     print(index)
#     second = song[index : index + 1000]
#     if index % 2000 == 0:
#         second.apply_gain(10)
#     else:
#         second.apply_gain(-10)
#     
#     loud_and_soft += second
#     
# loud_and_soft.play()


### Use fading to fade in and out every second

loud_and_soft = Audio()
for index in range(0, len(song), 1000):
    print(index)
    second = song[index : index + 1000]
    if index % 2000 == 0:
        second.fade_in(1000)
    else:
        second.fade_out(1000)
    
    loud_and_soft += second
    
loud_and_soft.play()



### Let's make a simple beat using bass drum and snare drum samples

bass_drum = Audio()
bass_drum.open_audio_file("Bass-Drum-2.wav")

snare_drum = Audio()
snare_drum.open_audio_file("Snare.wav")

# bass_drum.play()
# snare_drum.play()


### Let's loop the bass drum
# num_beats = 8
# drums = Audio() ## Will accumulate our drums
# for i in range(num_beats):
#     drums += bass_drum
# 
# drums.play()

### We want to be able to set the tempo
beats_per_minute = 103
ms_per_beat = (60 * 1000) / beats_per_minute

bass = bass_drum[ : ms_per_beat]

print("ms_per_beat", ms_per_beat)

### Fixes the tempo
# num_beats = 8
# drums = Audio() ## Will accumulate our drums
# for i in range(num_beats):
#     drums += bass
# 
# drums.play()


### Let's make it so the snare drum plays every 4th beat

# num_beats = 16
# drums = Audio() ## Will accumulate our drums
# for i in range(num_beats):
#     if i % 4 == 3:
#         drums += snare_drum
#     else:
#         drums += bass
# 
# drums.play()

print("length of snare in ms", len(snare_drum))

### We need to lengthen the snare drum sample to be ms_per_beat long
### We will make a new Audio object that is exactly ms_per_beat long, and then
### overlay the snare sample on top of it.
snare = Audio(ms_per_beat) ## This is a silent Audio object ms_per_beat long

snare.overlay(snare_drum)

num_beats = 16
drums = Audio() ## Will accumulate our drums
for i in range(num_beats):
    if i % 4 == 3:
        drums += snare
    else:
        drums += bass

# drums.play()

### What if we want to overlay on Levitating?
### We want our drums to start at 9.587 seconds into the song
# song = Audio()
# song.open_audio_file("levitating.wav")
# 
# silence_then_drums = Audio(9587)
# silence_then_drums += drums
# 
# song.apply_gain(-15)
# song.overlay(silence_then_drums)
# song.play()





