import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

mic = sr.Microphone()

with mic as source:
    print("Say something...")
    r.adjust_for_ambient_noise(source)
    audio_input = r.listen(source)
    result = r.recognize_sphinx(audio_input)
    print(result)