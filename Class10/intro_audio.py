from cs101audio import *

song = Audio()

song.open_audio_file("drivers_license.wav")

# song.play()

length = len(song)
print("The length of this song in miliseconds is", length)

### Audio objects allow us to access them in 1 milisecond increments
### We can use list operators like indexing and slicing to get
### parts of an audio object.

# intro = song[:8500]
# rest_of_verse = song[8500:22000] ## Guess and check to get first verse
# rest_of_song = song[22000:]
# 
# ### Speed up rest_of_verse
# rest_of_verse.change_speed(1.5)
# 
# ### Glue pieces back together:
# new_song = intro + rest_of_verse + rest_of_song
# new_song.play()
# new_song.save_to_file("chipmunk.wav")


### Concatenate first 2 seconds of song together
# piano_clip = song[:100]
# what_is_this = piano_clip * 20
# 
# what_is_this.play()


### This loops over the indices in song, skipping every second forward
# for index in range(0, len(song), 1000):
#     print(index)
#     ## This slice will give us 1 second of song each time through the loop
#     clip = song[index : index + 1000]
#     clip.play()
# #     piano_clip.play()


# for index in range(0, len(song), 4000):
#     print(index)
#     clip = song[index : index + 1000]
#     clip.play()


# for index in range(0, len(song), 1000):
#     print(index)
#     clip = song[index : index + 1000]
#     
#     ### Change the speed so it speeds up by 1% for each second that plays
#     speed = 1 + (index / 100000)
#     # After 1 second, should be 1.01
#     # After 2 seconds, should be 1.02, etc.
#     clip.change_speed(speed)
#     
#     clip.play()

new_song = Audio()
for index in range(0, len(song), 1000):
    print(index)
    clip = song[index : index + 1000]
    
    ### Change the speed so it speeds up by 1% for each second that plays
    speed = 1 + (index / 100000)
    # After 1 second, should be 1.01
    # After 2 seconds, should be 1.02, etc.
    clip.change_speed(speed)
    
    new_song += clip
    
new_song.play()
    
    


