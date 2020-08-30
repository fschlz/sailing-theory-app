import os
import sys

if __name__ == "__main__":

    os.system("source /usr/local/anaconda3/bin/activate && conda activate py37")
    
    path = '../resources/questions.json'

    if os.path.exists(path):
        os.remove(path)

    os.system("scrapy runspider ./src/sailoot/scrape_questions.py -o ./resources/questions.json")