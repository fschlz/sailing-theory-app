# Sailing Theory Trainer

- I've written a script that scrapes the relevant data from the website using the python lib Scrapy together with xPath
- Also included is a simple programm that runs in your CLI, which will ask you the scraped questions and tell you how well you did when you quit the programm

## Prep env

```shell
cd ./sailing-theory-app
python3 -m venv env
source ./env/bin/activate
python3 -m pip install -r requirements.txt
```

## Get the data

```shell
python3 -m ./src/sailoot/loot.py
```

## Run the app

```shell
python3 -m ./src/sailearn/learn.py
```
