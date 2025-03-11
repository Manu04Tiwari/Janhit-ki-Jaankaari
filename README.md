# News-Bot 🤖
# Introduction 
News-bot is a telegram bot which will show you news from any country, in any language about topics specified by you.
# About the Bot
## Features 📰
* This bot is trained to fetch news from any **country** and in **any language**.
* It is equipped for small talk.
* It is also equipped with a custom keyboard which will show you all the available topics.
* Also, the bot is trained for fuzzy matching i.e. it can identify the topics even if you mispell them. 
  - E.g.  If you mis-spell "sports" as "sprts","spots" etc, the bot can understand that you meant "sports".
## News-Topics 📕
* Top Stories
* World
* Nation
* Business
* Technology
* Entertainment
* Sports
* Science
* Health
## Inside the bot ⚒
It is a Python-Flask application, deployed using Heroku. 
Shortest way to explain my code:
* I trained the bot using **dialogflow**.
* Connected a service account from Google Cloud to the code.
* Added **gnewsclient** which helps the bot fetch news.
* Set up the webhook with Heroku.
# Demo 🎥
Click on the picture to watch the demo:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/tq9lXJCJki0/0.jpg)](https://www.youtube.com/watch?v=tq9lXJCJki0)
# Try it yourself 🏃🏾‍♀️
Search for **user_456bot** on telegram, hopefully it will work. 
PS: There might be a few seconds lag after your first command as the server shuts down when its not in use.
# Tech Stack 👾

<a href="https://python.org/" title="python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="python" width="40px" height="40px"></a>
<a href="https://dialogflow.org/" title="python"><img src="https://github.com/get-icon/geticon/raw/master/icons/dialogflow.svg" alt="dialogflow" width="40px" height="40px"></a>
<a href="https://flask.org/" title="python"><img src="https://github.com/get-icon/geticon/raw/master/icons/flask.svg" alt="flask" width="40px" height="40px"></a>
<a href="https://heroku.org/" title="heroku"><img src="https://github.com/get-icon/geticon/raw/master/icons/heroku.svg" alt="python" width="40px" height="40px"></a>

