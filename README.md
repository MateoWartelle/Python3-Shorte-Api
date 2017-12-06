# Python3-Shorte-Api
updated Shorte.st API support for Python 3 by Mateo Wartelle

# Introduction
Shorte.st is a URL shortening service that allows users to shorten urls which serve a 5 second ad to the end consumer prior to being redirected to there original intended destination. 

# Installing 
```
$ git clone https://github.com/MateoWartelle/Python3-Adfly-Api.git
$ cd Python3-Adfly-Api
```
To install dependencies, run
```
$ pip3 install requirements.txt
```
# Config
You will need to go to https://shorte.st/tools/api and grab your API Token<br> 
Replace "YOUR API TOKEN" with the code from this page. 

# Making Calls
```
>>> URLShortened = convert_to_shorte("www.google.com")
>>> print (URLShortended)
http://destyy.com/q43R4C
```
