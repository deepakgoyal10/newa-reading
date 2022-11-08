import json
import requests
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':
    def news(category, api):
        url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api}"
        print(url)
        news_text = requests.get(url).text
        parsed = json.loads(news_text)
        speak("Welcome to the news channel")
        count_list = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "tenth"]
        for count, item in enumerate(count_list, 1):
            data = parsed['articles'][count]
            news = data['title']
            news_url = data['url']
            news = f"Today's {item} news: {news}"
            print(f"{news}\nCheck full news at:{news_url}")
            speak(news)
    cat = ["business", "entertainment","general","health","science","sports","technology"]
    print("Categories: ")
    for count, item in enumerate(cat, 1):
        print("\t", count, item)

    speak("Choose your category: ")
    cat_inp = int(input("Choose your category: "))
    category = cat[cat_inp]
    print("your category:", category)
    speak("Enter your api key: ")
    api_inp = input("Enter your api key: ")
    news(category, api_inp)




