# Python-Smart-AI-Voice-Assistant
Visit our Website - [https://JARVIS-Python-Voice-Assistant/](https://harshit-raj-14.github.io/JARVIS-Python-Voice-Assistant/)

The aim of this project is to introduce JARVIS AI Python Assistant, an innovative artificial intelligence (AI) tool that will automate tasks, provide support, and simplify processes. A Python-based voice assistant that can greet you and perform a variety of tasks, including searching the web, opening social media, and creating a to-do list and much more to play with the amazing features.

The AI assistant will automate tasks, provide support, and simplify processes, freeing up valuable time and improving efficiency. 

# Introduction 👨‍💻
It is a voice assistant which can be used to interact with your computer and also you have been seeing it in Iron man movies, but this JARVIS is not that much advanced as shown in movies. 

- Demo video for ***JARVIS*** is available [here](https://youtu.be/SjwXXjhMQWs)

## Cool functionalities of JARVIS 😎 :)

I have wrote code which you can use JARVIS in the following ways :

- It can tell **count of Covid-19 cases for each state in India**
- It can do **Screen Recording with voice recording** stuff.
- It can also do **voice recording**
- It can access your **mobile camera**
- It can access your **web camera**
- It can read **pdf's**
- It can work as a **telephone dictionary**(Add contacts, search contacts)
- It can **generate qr codes** for Links/anyText.
- It can check/find your **Internet speed**
- It can tell your **IP address**
- It can tell the **latest news**
- It can check the **system condition**
- It can send **gmails**
- It can send **whatsapp messages to Individual & group chats**
- It can play **youtube songs**
- It can **download youtube songs** 
- It can **download instagram profiles**
- It can find/tell your **current location** where ever you are
- It can take **screenshots** with a custom filename 
- It can tell **current time**
- It can tell **current day**
- It can tell random **progrmamming jokes**
- It can also tell your **schedule** for each day
- It can be **silent** for a certain number of time if we mention how much time we want it to be silent
- It can **search in wikipedia** and tell about it in 5 lines
- It can tell **procedure/instructions** how to make something(Eg:How to make a cake)
- It can **search for information** in browser which we want
- It can **control system volumes**
- It can **control system power activities**(Eg: shutdown, restart, sleep)
- It can **play music file** in a particular directory where the songs are present
- It can open your **social media and open-source accounts**
- It can open your **college meeting accounts**
- It can open your **OTT platforms accounts**
- It can open your **all google apps**
- It can open presentation tools like **canva, google slide**
- It can open **shopping websites**
- It can open **all the URL links**
- It can open/close **all the pc applications**(*NOTE*: give correct path based on your OS)
- It can **sleep until you say wake up**
- Finally It **can interact with you** and you can also add more commands if you want😎

> **NOTE:** Before running the code you must make sure you have all the modules installed in your python version(***NOTE:*** python version can be >=3.6).

## These are the following modules used in JARVIS📚 :

[SpeechRecognisation](https://pypi.org/project/SpeechRecognition/) | [PyAudio](https://pypi.org/project/PyAudio/) | [pyttsx3](https://pypi.org/project/pyttsx3/) | [pywhatkit](https://pypi.org/project/pywhatkit/) | [datetime](https://pypi.org/project/DateTime/) | [wikipedia](https://pypi.org/project/wikipedia/) | [pyjokes](https://pypi.org/project/pyjokes/) | [cv2](https://pypi.org/project/opencv-python/) | [cv2 tools](https://pypi.org/project/cv2-tools/) | [requests](https://pypi.org/project/requests/) | [smtplib](https://pypi.org/project/secure-smtplib/) | [psutil](https://pypi.org/project/psutil/) | [random](https://pypi.org/project/random2/) | [instaloader](https://pypi.org/project/instaloader/) | [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) | [PyPDF2](https://pypi.org/project/PyPDF2/) | [bs4](https://pypi.org/project/bs4/) | [PyQt5](https://pypi.org/project/PyQt5-Qt5/) | [pywikihow](https://pypi.org/project/pywikihow/) | [speed test](https://pypi.org/project/speedtest-cli/) | [pytube](https://pypi.org/project/pytube/) | [numpy](https://pypi.org/project/numpy/) | [urllib](https://pypi.org/project/urllib3/) | [covid](https://pypi.org/project/covid-india/) | [phonenumbers](https://pypi.org/project/phonenumbers/) | [folium](https://pypi.org/project/folium/) | [opencage](https://pypi.org/project/opencage/) | [pillow](https://pypi.org/project/Pillow/) | [Pywave](https://pypi.org/project/PyWave/) | [win32api](https://pypi.org/project/pywin32/) | [mscvrt](https://docs.python.org/dev/library/msvcrt.html#msvcrt.kbhit)

## API keys 🔑
To run this project you should need some API key's for reading news, for finding phone number location. Register for your API key by clicking the following
- [NewsAPI](https://newsapi.org/) : used for fetching news
- [Open cage](https://opencagedata.com/) : to locate a place in maps

> *Note* : supported OS : **Windows**

## Installation 💻
- You need to first ```fork``` this repository and ```clone``` the repository to your local system 

    ```git clone https://github.com/<your-github-username>/JARVIS-Python-Voice-Assistant.git```
- Make sure to install all the required python modules mentioned above or you can simply install them by 

    ```pip install -r requirements.txt```

- Add your **gmail id** and **password** to send emails(line:797,798)
- Make sure you have registerd in [NewsAPI](https://newsapi.org/) and replace the ```apiKey=```**```YOUR_NEWS_API_KEY```** with your API key(Line: 852) and in [Open cage](https://opencagedata.com/) and replace the ```API_key =``` "**```_OPEN_CAGE_GEOCODE_API_KEY_```**" with your API key(PhoneNumber.py(lineNo: 13))
- For using mobile camera you need to first install an app in mobile called [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US&gl=US) after installing go to **START SERVER** it will open your mobile camara at the bottom of the screen you can see **IPv4** there you can find the IP address and replace ```_IP_Webcam_IP_address_``` with the IP address in ```JARVIS.py``` MobileCamera function(line: 332)

That's it for now **#Enjoy** speaking with your computer friend 😁

## FINAL GUI of JARVIS😎

![Capture](https://user-images.githubusercontent.com/98808802/221436409-5b62f953-4142-47ea-b71d-82bf143df5bd.JPG)


## How does this code work?
This voice assistant is built using a combination of various Python packages, making it easy for you to use and access a wide range of functionality.


## Using ChatGPT with JARVIS
To use ChatGPT, you would need an API key. To get the API Key follow the steps below.

#### How to get your API Key
1. Create an OpenAI account: Go to the OpenAI website [https://openai.com/](https://openai.com/) and click "Sign up" to create an account.
2. Apply for API access: After creating your account, go to the "API" section and apply for API access by filling out the form. OpenAI will review your application and let you know if it has been approved.
3. Generate API Key: Once your API access has been approved, you will be able to generate an API key from the API section of your OpenAI account.
4. Use API Key: Finally, use the API key in your application or tool that integrates with the OpenAI API to access the ChatGPT model.
Note: If you encounter any issues during these steps, you can reach out to the OpenAI support team for assistance.
5. Copy and paste the API Key in the code.


## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or new features to propose, please submit an issue or create a pull request.
**How to contribute**

* Fork the repo in your github by clicking on the fork button.
* Git clone it in your local system. Make appropriate changes.
* Make a pull request.

**Where can you contribute?**
I have already made some good first issues and easy issues in the issue section. You can start contributing from there. You can also add new fucntionality to our JARVIS nad make it more smart.😎

## License

This project is licensed under the [MIT License](LICENSE).    [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


