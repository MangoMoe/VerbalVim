# VerbalVim
Turning vim shortcuts into verbal coding for hands-free programming

## requirements
SpeechRecognition python package
PyAudio for microphone

CMUSphinx is one of the best offline options
    Pocket sphinx package
TODO Might actually have to use vosk/kaldi because the group that made sphinx is working on that one now and it is maintained, unlike sphinx, although the speechrecognition tutorial is recent enough that maybe it is fine. It looks like the pocketsphinx is working fine so far
Had to manually download a precompiled wheel for pocketsphinx here:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx

I might just have to try the old one and switch to the new one if need be


this tutorial was very helpful:
https://realpython.com/python-speech-recognition/