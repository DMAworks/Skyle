import time
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import playsound
from gtts import gTTS
import os


def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio, language='ru-RU')
            print("Ваш вопрос: " + data)

        except sr.UnknownValueError:
            print("Повторите, пожалуйста...")

    return data


def respond(output):
    num = 0
    print(output)
    num += 1
    response = gTTS(text=output, lang='ru', slow=False)
    file = str(num) + ".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)


if __name__ == '__main__':
    respond("Приветствую сэр")

    while (1):
        respond("Чем могу быть полезна?")
        text = talk().lower()

        if text == 0:
            continue

        if "стоп" in str(text) or "пока" in str(text) or "уйди" in str(text):
            respond("Всего наилучшего сэр!")
            break

        if 'найди в википедии' in text:
            respond('ищу в википедии')
            text = text.replace("найди в википедии", "")
            wikipedia.set_lang('ru')
            results = wikipedia.summary(text, sentences=3)
            respond("вот что я нашла")
            print(results)
            respond(results)

        elif 'сколько время' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"сейчас время {strTime}")

        elif 'найди' in text:
            text = text.replace("найди", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)

        elif 'открой google' in text:
            webbrowser.open_new_tab("https://www.google.com")
            respond("открываю google")
            time.sleep(5)

        elif 'открой youtube' in text:
            webbrowser.open_new_tab("https://www.youtube.com")
            respond("открываю youtube")
            time.sleep(5)

        elif "открой word" in text:
            respond("открываю Microsoft Word")
            os.startfile("C:\Program Files (x86)\Microsoft Office\\root\Office16\WINWORD.EXE")

        else:
            respond("Приложение не доступно")
