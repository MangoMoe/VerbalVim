import speech_recognition as sr
import keyboard

# TODO make a way to add a custom list of words to recognize as other words (for example, saying "yank" almost always leads to the word "yet" instead)
def get_phrase_from_mic(recognizer, mic):
    result = "#ERROR#"
    if not isinstance(recognizer, sr.Recognizer):
        print("Recognizer was not an instance of the Recognizer class")
        return result
    if not isinstance(mic, sr.Microphone):
        print("Mic was not an instance of the Microphone class")
        return result
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Say something...")
            audio_input = r.listen(source)
            result = r.recognize_sphinx(audio_input)
    except sr.UnknownValueError:
        print("Speech couldn't be recognized")
        return result
    return result

if __name__ == "__main__":
    mic = sr.Microphone()
    r = sr.Recognizer()
    while True:
        phrase = get_phrase_from_mic(r, mic)
        print(phrase)
        if phrase == "#ERROR#":
            continue
        elif phrase == "input":
            keyboard.press_and_release("i")
        elif phrase == "escape":
            keyboard.press_and_release("esc")
        elif phrase.lower() == "exit":
            print("Well bye then")
            break
        else:
            keyboard.write(phrase)

#n thatskatand this could be workingmaybe it is worthe a#ERROR#tenjaybutupbuild upgo upi don't know what to do although you aredoes this work betterc. n. but it does work betterit seems like it does work betterwith so little bitat least a little bitspace
        

# >>> with harvard as source:
# ...     audio1 = r.record(source, duration=4)
# ...     audio2 = r.record(source, duration=4)
# ...
# >>> r.recognize_google(audio1)
# 'the stale smell of old beer lingers'
# >>> r.recognize_google(audio2)
# 'it takes heat to bring out the odor a cold dip'