import os
import sys

if __name__ == "__main__":
    
    path = '../resources/questions.json'

    if os.path.exists(path):
        os.remove(path)

    os.system("scrapy runspider ./src/sailoot/scrape_questions.py -o ./resources/questions.json")
