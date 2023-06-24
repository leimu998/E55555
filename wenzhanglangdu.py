import pyttsx3
import requests
from bs4 import BeautifulSoup
url = str(input("Paste article url\n"))

def content(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.text,'html.parser')
  articles = []
  for i in range(len(soup.select('.p'))):
    article = soup.select('.p')[i].getText().strip()
    articles.append(article)
    contents = " ".join(articles)
  return contents
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

contents = content(url)
## print(contents)      ## In case you want to see the content

#engine.save_to_file
#engine.runAndWait() ## In case if you want to save the article as a audio file
