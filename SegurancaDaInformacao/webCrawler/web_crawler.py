from bs4 import BeautifulSoup # HTML e XML
import requests # Requisição HTTP
from collections import Counter # Manipulaçao de lista, tuplas ...
import operator # Operações +-*/ AND OR

def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        #print("% s : % s " % (key, value))
        print(f"{key}: {value}")
    
    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


def clean_wordlist(wordlist):

    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-+{[]}|;:"<>?/., '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)

def start(url):

    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')

    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)

        clean_wordlist(wordlist)

if __name__ == '__main__':
    start('https://www.geeksforgeeks.org/python-programming-language-tutorial/')
