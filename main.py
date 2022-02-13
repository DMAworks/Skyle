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
        input.adjust_for_ambient_noise(source, duration=0.2)
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

    webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

    while (1):
        # respond("Чем могу быть полезна?")
        text = talk().lower()

        if text == 0:
            continue

        skyle = ["скайла", "ская", "сказал", "скаи", "кайл", "сказку", "сказка", "скажи", 'skill', "скала", "скал", "сушистайл", "слушать", "сканер", "сушиста", 'skype', 'skyla']

        for x in skyle:
            if x in text:
                text = text.replace(x, 'skyle')

                if "skyle" in text:

                    if "стоп" in str(text) or "пока" in str(text) or "уйди" in str(text):
                        respond("Всего наилучшего сэр!")
                        break

                    if "найди в википедии" in text:
                        respond('ищу в википедии')
                        text = text.split("найди в википедии ")[-1]
                        print(text)
                        # text = text.replace("найди в википедии", "")
                        wikipedia.set_lang('ru')
                        results = wikipedia.summary(text, sentences=3)
                        respond("вот что я нашла")
                        print(results)
                        respond(results)

                    elif 'сколько время' in text:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        respond(f"сейчас время {strTime}")

                    elif 'найди' in text:
                        text = text.split("найди ")[-1]
                        # text = text.replace("найди", "")
                        webbrowser.get('edge').open_new_tab(text)
                        # time.sleep(5)

                    elif 'google' in text or 'гугл' in text:
                        webbrowser.get('edge').open_new_tab("https://www.google.com")
                        respond("открываю google")
                        # time.sleep(5)

                    elif 'youtube' in text:
                        webbrowser.get('edge').open_new_tab("https://www.youtube.com")
                        respond("открываю youtube")
                        # time.sleep(5)

                    elif "word" in text:
                        respond("открываю Microsoft Word")
                        os.startfile("C://Program Files (x86)//Microsoft Office//root//Office16//WINWORD.EXE")

                    else:
                        # respond("Приложение не доступно")
                        respond("Чем могу быть полезна?")
                        break
                        # break
