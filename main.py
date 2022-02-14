import speech_recognition as sr  # распознавание голоса
import datetime  # текущая дата и время
import wikipedia  # для поиска в википедии
import webbrowser  # для взаимодествия с браузером
import playsound  # для воспроизведения файла
from gtts import gTTS  # для преобразования текста в речь
import os  # для удаления файла


def talk():
    input = sr.Recognizer()  # инициализация
    with sr.Microphone() as source:
        input.adjust_for_ambient_noise(source, duration=0.2)
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio, language='ru-RU')
            print("Ваш вопрос: " + data)

        except sr.UnknownValueError:
            pass

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

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(
    "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"))
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

if __name__ == '__main__':
    print("Распознаю...")
    while 1:
        text = talk().lower()

        if text == 0:
            continue

        skyle = ["скайла", "ская", "сказал", "скаи", "кайл", "скилл", 'skill', "сказку", "сказка",
                 "скажи", 'skill', "скала", "скал", "сушистайл", "слушать", "сканер", "сушиста", 'skype', 'skyla',
                 "скайл"]

        for x in skyle:
            if x in text:

                if text == 0:
                    continue


                if "привет" in text or "здарова" in text:
                    respond("Приветствую сэр!")
                elif "найди в википедии" in text:
                    respond('ищу в википедии')
                    text = text.split("найди в википедии ")[-1]
                    print(text)
                    wikipedia.set_lang('ru')
                    results = wikipedia.summary(text, sentences=2)
                    respond("вот что я нашла")
                    print(results)
                    respond(results)
                elif 'сколько время' in text:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    respond(f"сейчас время {strTime}")
                elif 'найди' in text:
                    text = text.split("найди ")[-1]
                    webbrowser.open_new_tab(text)
                elif 'google' in text or 'гугл' in text:
                    webbrowser.get('edge').open_new_tab("https://www.google.com")
                    respond("открываю google")
                elif 'youtube' in text:
                    webbrowser.get('edge').open_new_tab("https://www.youtube.com")
                    respond("открываю youtube")
                elif "word" in text:
                    respond("открываю Microsoft Word")
                    os.startfile("C://Program Files (x86)//Microsoft Office//root//Office16//WINWORD.EXE")
                elif "excel" in text:
                    respond("открываю Microsoft Excel")
                    os.startfile('C://Program Files (x86)//Microsoft Office//root//Office16//EXCEL.EXE')
                elif "one note" in text or "onenote" in text or "ван нот" in text:
                    respond("открываю Microsoft One Note")
                    os.system("explorer.exe shell:appsFolder\Microsoft.Office.OneNote_8wekyb3d8bbwe!microsoft.onenoteim")
                elif "что надо сделать" in text or "задачи" in text or "задач" in text:
                    respond("открываю список задач")
                    os.system("explorer.exe shell:appsFolder\Microsoft.Todos_8wekyb3d8bbwe!App")
                elif "стоп" in str(text) or "пока" in str(text) or "уйди" in str(text):
                    respond("Всего наилучшего сэр!")
                    break
                else:
                    respond("не поняла вопроса")
                    print("Повторите, пожалуйста")
                    break
