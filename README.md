# VerbalVim
Turning vim shortcuts into verbal coding for hands-free programming

## requirements
SpeechRecognition python package
PyAudio for microphone
PocketSphinx
    I had to manually download a precompiled wheel for pocketsphinx here:
    https://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx

CMUSphinx is one of the best offline options
    Pocket sphinx package
I'll have to look into kaldi at some point
TODO Might actually have to use vosk/kaldi because the group that made sphinx is working on that one now and it is maintained, unlike sphinx, although the speechrecognition tutorial is recent enough that maybe it is fine. It looks like the pocketsphinx is working fine so far
I might just have to try the old one and switch to the new one if need be


this tutorial was very helpful (And I probably copied some code from it):
https://realpython.com/python-speech-recognition/

seems to work better with a headset, go figure


# TODOS
* Make a way to add a custom list of words to recognize as other words (for example, saying "yank" almost always leads to the word "yet" instead)
* Customizable escape phrases (kind of like remapping jj to escape input mode)
* some way to map arbitrary phrases to certain keybindings (i.e. saying "go to top" would result in "gg")
* figure out how to search the phrase for instances of the word "space" (or another predefined word), also things like "underscore", "dot", etc. Hopefully just make this super customizable (replace phrase x with symbol y)
* figure out how to make logical names for variables (like figure out where to put camelCase or snake_case for a name instead of with spaces)
* pause functionality (say "pause" to stop taking input and "resume" to continue taking input, so that a person using it can stop to talk to people and stuff like that)
* (super in the future) make it so you can do most things on your computer with it (alt-tabbing, switching workspaces, and other hacks like that)