import requests
import json
import pyttsx3
engine = pyttsx3.init()



City = input("Enter the name of the city\n")

url = f'http://api.weatherapi.com/v1/current.json?key=c541bc5796eb44d0a0b121842241907&q={City}'

r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
engine.say(f'The temperature of {City} is  {wdic["current"]["temp_c"]}')
engine.runAndWait()