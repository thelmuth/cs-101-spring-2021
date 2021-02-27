# A Pydub based audio library for introductory computer science.

# All files that use the CS101 Audio package must have the following line
# at the top of the file.

# from cs101audio.py import *

from pydub import AudioSegment
from pydub.generators import Sine
from pydub.generators import Sawtooth
from pydub.generators import Square
from pydub.generators import Triangle
from pydub.playback import play
import array

import warnings # For ignoring a PyDub warning that runs everytime you run your code
warnings.filterwarnings("ignore", message="Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work")
warnings.filterwarnings("ignore", message="Couldn't find ffplay or avplay - defaulting to ffplay, but may not work")

from pydub import * # For the Base AudioSegment Class
from pydub.playback import * # For playing back audio
from pydub.generators import * # For generating audio waves


# For Error Checking
def _check_type(param, param_name, target_type):
    if not isinstance(param, target_type):
        raise TypeError("\nThe parameter '" + param_name + "' should be a " +
                        str(target_type.__name__) +
                        " but instead was a " +
                        str(type(param).__name__) + "\n" +
                        param_name + " = " + str(param))


class Audio():
    """
    Wrapper Class for the Pydub AudioSegment Class
    """

    def __init__(self, duration=0, frame_rate=44100):
        """
        Constructor creates a silent audio segement with default duration of 0 milliseconds
        
        Arguments:
        duration -- the length of the new silent audio segment in milliseconds
        Default is 0 seconds (empty segment) (int)
        frame_rate -- the frame_rate of the new audio segment in frames per second.
        Default is 44100 (int)
        """
        self._audioseg = AudioSegment.silent(duration=duration, frame_rate=frame_rate)


    def set_audioseg(self, newaudio):
        """
        Sets the audiosegment attribute of the Audio Object
        
        Arguments:
        newaudio -- new audio segment to replace self's self._audioseg (Audio Object)
        """
        self._audioseg = newaudio

    def get_audioseg(self):
        """
        Returns the Audio Object's audio segment attribute
        """
        return self._audioseg

    def get_sample_list(self):
        """
        Returns the a sample list for the Audio Object's audio segment
        attribute
        """
        return self._audioseg.get_array_of_samples().tolist()
    
    def get_frame_rate(self):
        """
        Returns the Audio Object's frame rate
        """
        return self._audioseg.frame_rate

    def __len__(self):
        """
        Returns the length of the audio file in milliseconds
        """
        return len(self._audioseg)

    def open_audio_file(self, filename):
        """
        Reads filename and sets the Audio object's audio segment to be
        the one read from the file
        
        Arguments:
        filename -- A string containing the name of the audio file to be opened (str)
        """
        
        _check_type(filename, "filename", str)
        try:
            AudioSegment.from_file(filename)
        except FileNotFoundError:
            raise FileNotFoundError("File " + filename + " not found")

        self._audioseg = AudioSegment.from_file(filename)
        
        
    def save_to_file(self, filename):
        """
        Saves this Audio Object's audio segment to filename
        
        Arguments:
        filename -- A string containing the name of the file to save to (str)
        """
        extendindex = filename.find(".")
        file_extension = filename[extendindex + 1:]
      
        self._audioseg.export(out_f=(filename), \
                              format=file_extension)

    def from_sample_list(self, sample_lst, template=None):
        """
        Sets the Audio Object's audio segment to be the one created
        from the sample_lst parameter using the metadata (sample width, frame rate
        frame width, etc.) of the template parameter. If template is not passed, self's
        metadata is used.
        
        Arguments:
        sample_lst -- the list of samples provided to generate the audio (list)
        template -- an audio object that is used as a template for the new audio segment (Audio Object)
        """
        if isinstance(sample_lst, list):
            sample_lst = array.array('h', sample_lst)
            
        if not template:
            template = self
            
        # If an sample list is spliced, it may have a incorret total number of samples
        # When attempting to play this, an error occurs because the total sample
        # count is not a multiple of 4 and the number of channels
        # So if this occurs, we append 0s until it is a multiple
        while len(sample_lst) * template.get_audioseg().channels % 4 != 0:
            sample_lst.append(0)
            
        self._audioseg = template.get_audioseg()._spawn(sample_lst)

    def from_generator(self, freq, duration, wavetype):
        """
        Sets the Audio Object's audio segment to be the audio generated
        by a wave generator.
        
        Arguments
        freq -- the frequency of the wave to be generated (in Hz) (int)
        duration -- the duration of the wave to be generated (in milliseconds) (int)
        wavetype -- the type of wave to be generated. A string containing either
                    Sine, Square, Sawtooth, or Triangle (case insenstivie) (str)
        """
        _check_type(wavetype, "wavetype", str)
        _check_type(freq, "freq", int)
        _check_type(duration, "duration", int)
        self._duration = duration
        if wavetype.upper() == "SINE":
            wave = Sine(freq)
        elif wavetype.upper() == "SAWTOOTH":
            wave = Sawtooth(freq)
        elif wavetype.upper() == "SQUARE":
            wave = Square(freq)
        elif wavetype.upper() == "TRIANGLE":
            wave = Triangle(freq)
        else:
            raise ValueError("Error! Invalid Wavetype \"" + wavetype + "\" passed to from_generator")

        self._audioseg = wave.to_audio_segment(duration)
        #self._audioseg = self._audioseg.fade_in(50).fade_out(100)

    def play(self):
        """
        Plays the Audio Object's audio segment, if it isn't empty.
        """
        if len(self._audioseg) > 0:
            play(self._audioseg)
            

    def __add__(self, other_audio):
        """
        Implements the + operator to concatenate self's
        audio segment and other_audio's audio segment.
        Returns a new Audio Object (self and other_audio are not modified)
        
        Arguments:
        other_audio -- the audio object to concatenate to self (Audio Object)
        """ 
        _check_type(other_audio, "other_audio", Audio)

        result = Audio()

        result.set_audioseg(self._audioseg + other_audio.get_audioseg())

        return result

    def __iadd__(self, other_audio):
        """
        Implements the += operator to concatenate self's audio segment and
        other_audio's audio segment
        Does not return a new Audio Object, but modifies self's audio segment attribute
        
        Arguments:
        other_audio -- the audio object to concatenate to self (Audio Object)
        """
        _check_type(other_audio, "other_audio", Audio)

        self._audioseg += other_audio.get_audioseg()
        return self


    def __mul__(self, loopnum):
        """
        Implements the * operator to loop self's audio segment loopnum times.
        Returns a new Audio Object
        
        Arguments:
        loopnum -- the number of times to loop the audio (int)
        """
        _check_type(loopnum, "loopnum", int)

        result = Audio()
        result.set_audioseg(self._audioseg * loopnum)

        return result

    def __imul__(self, loopnum):
        """
        Implements the *= operator to loop self's audio segment loopnum times.
        Modifies self's audioseg attribute
        
        Arguments:
        loopnum -- the number of times to loop the audio (int)
        """
        _check_type(loopnum, "loopnum", int)

        self._audioseg *= loopnum
        return self

    def __getitem__(self, millisecond):
        """
        Implements [] to index and slice audio segments
        
        Arguments:
        millisecond -- either the millisecond to index or a slice object (int or slice)
        """
        result = Audio()
        result.set_audioseg(self._audioseg[millisecond])

        return result


    def overlay(self, audio2, position=0, loop=False):
        """
        Overlays audio2 onto self's audio.
        
        Arguments
        audio2 -- The audio object to be overlayed onto self (Audio Object)
        position -- The millisecond in self's audio at which to overlay audio2 (int)
        loop -- If true, loops audio2 so that it plays until the end of self's audio (bool)
        """
        self._audioseg = self._audioseg.overlay(audio2.get_audioseg(), position=position, loop=loop)
        
    def apply_gain(self, gain):
        """
        Changes the amplitude (the general loudness) of the audio.
        Gain is specificed in decibels
        
        Arugments:
        gain -- the amount of gain in decibles (can be negative) (int)
        """
        self._audioseg = self._audioseg.apply_gain(gain)
        
    def fade_in(self, fadetime):
        """
        Adds a fade at the beginning of the audio, lasting fadetime milliseconds
        
        Arguments
        fadetime -- the length of the fade in milliseconds (int)
        """
        _check_type(fadetime, "fadetime", int)
        self._audioseg = self._audioseg.fade_in(fadetime)
        
    def fade_out(self, fadetime):
        """
        Adds a fade at the end of audio, lasting fadetime milliseconds
        
        Arguments
        fadetime -- the length of the fade in milliseconds (int)
        """
        _check_type(fadetime, "fadetime", int)
        self._audioseg = self._audioseg.fade_out(fadetime)
        
    def fade(self, fadeintime=0, fadeouttime=0):
        """
        Adds a fade to the beginning and/or end of the audio,
        lasting fadeintime and fadeouttime, respectively, both in milliseconds.
           
        Arguments:
        fadeintime -- the length of the beginning fade in milliseconds (int)
        fadeouttime -- the length of the ending fade in milliseconds (int)
        """
        _check_type(fadeintime, "fadeintime", int)
        _check_type(fadeouttime, "fadeouttime", int)
        self._audioseg = self._audioseg.fade_in(fadeintime).fade_out(fadeouttime)
        

    def change_speed(self, factor):
        """
        Changes the speed of the audio by a multiplier of factor.
        
        Arguments:
        factor -- the multiplier for slowing down(< 1) or speeding up(postive) (int/float)
        """
        if not (isinstance(factor, int) or isinstance(factor, float)):
            raise TypeError("\nThe parameter '" + factor + "' should be a " +
                        "int or float but instead was a " +
                        str(type(factor).__name__) + "\n" +
                        "factor" + " = " + str(factor))
        if factor == 0:
            raise ValueError("Error! Cannot change speed by a factor of 0")

        sound_with_altered_frame_rate = self._audioseg._spawn(self._audioseg.raw_data, overrides={
                                        "frame_rate": int(self._audioseg.frame_rate * factor)})
        
        self._audioseg = sound_with_altered_frame_rate.set_frame_rate(self._audioseg.frame_rate)


# Dictionary for the frequncies of musical notes
music_note_dict = {"C0":16, "C#0":17, "Db0": 17, "D0":18, "D#0":19, "Eb0":19, "E0":21,
                   "F0":22, "F#0":23, "Gb0":23, "G0": 25, "G#0":26, "Ab0":26, "A0":28,
                   "A#0":29, "Bb0":29, "B0":31, "C1":33, "C#1":35, "Db1":35, "D1":37,
                   "D#1":39, "E1":41, "F1":44, "F#1":46, "Gb1": 46, "G1": 49, "G#1":52,
                   "Ab1":52, "A1":55, "A#1":58, "Bb1":58, "B1":62, "C2":65, "C#2":69,
                   "Db2":69, "D2":73, "D#2":78, "Eb2":78, "E2":82, "F2":87, "F#2":92, "Gb2":92,
                   "G2":98, "G#2":104, "Ab2":104, "A2":110, "A#2":116, "Bb2":116, "B2":123,
                   "C3":131, "C#3":139, "Db3":139, "D3":147, "D#3":156, "Eb3":156,"E3":165,
                   "F3":175, "F#3":185, "Gb3": 185, "G3":196, "G#3":208, "Ab3":208, "A3":220,
                   "A#3":233, "Bb3":233, "B3":247, "C4":262, "C#4":277, "Db4":277, "D4":294,
                   "D#4":311, "Eb4":311, "E4":330, "F4":349, "F#4":370, "Gb4":370, "G4":392,
                   "G#4":415, "Ab4":415, "A4":440, "A#4":466, "Bb4":466, "B4": 494, "C5":523,
                   "C#5":554, "Db5":554, "D5":587, "D#5":622, "Eb5":622, "E5":659, "F5":699,
                   "F#5":740, "Gb5":740, "G5":784, "G#5":831, "Ab5":831, "A5":880, "A#5":932,
                   "Bb5":932, "B5":988, "C6":1047, "C#6":1109, "Db6":1109, "D6":1175, "D#6":1245,
                   "Eb6":1245, "E6":1319, "F6":1397, "F#6":1480, "Gb6":1480, "G6":1568, "G#6":1661,
                   "Ab6":1664, "A6":1760, "A#6":1865, "Bb6":1865, "B6":1976, "C7":2093, "C#7":2217,
                   "Db7":2217, "D7":2349, "D#7":2489, "Eb7":2489, "E7":2637, "F7":2794, "F#7":2960,
                   "Gb7":2960, "G7":3136, "G#7":3322, "Ab7":3322, "A7":3520, "A#7":3729, "Bb7":3729,
                   "B7":3951, "C8":4186, "C#8":4435, "Db8":4435, "D8":4699, "D#8":4978, "Eb8":4978,
                   "E8":5274, "F8":5588, "F#8":5920, "Gb8":5920, "G8":6272, "G#8":6645, "Ab8":6645,
                   "A8":7040, "A#8":7459, "B8":7902}



def generate_music_note(note, duration, wavetype, gain=0):
    """
    Function generates a musical note of duration milliseconds, with wavetype type.
    Returns a new audio object with the generated audio
    
    Arguments:
    note -- A string denoting a musical note of the form [A-G](#|b|)[0-8]. Case insenstive. (str)
    duration -- Duration of the note in milliseconds. (int)
    wavetype -- A string denoting the type of wave to generate. Must be either Sine, Square
                Sawtooth or Triangle. Case insensitive. (str)
    gain -- Gain to apply to note (can be negative) (int)
    """
    _check_type(note, "note", str)
    _check_type(duration, "duration", int)
    _check_type(wavetype, "wavetype", str)
    try:
        note = note[0].upper() + note[1:]
        freq = music_note_dict[note]
    except KeyError:
        raise ValueError("Error! Invalid note \"" + note + "\" passed to generate_music_note")

    audio_result = Audio()

    audio_result.from_generator(freq, duration, wavetype)

    audio_result.fade(50, 100)
    audio_result.apply_gain(gain)

    return audio_result
