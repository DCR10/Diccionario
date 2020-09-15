from pyquery import PyQuery as pq
import html #to have available function html.unescape 
import re


class RAE:

    def __init__(self,word):
        self.URL = "https://dle.rae.es/"              
        self.word=word
        self.headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def getDefinition(self):
        # This method get definition from word
        dataHtml = pq(self.URL + self.word, headers=self.headers)
        return dataHtml('#resultados')

    def getWordsStart(self):
        # This method get words that start with the word
        dataHtml = pq(self.URL + self.word + "?m=31", headers=self.headers)
        result = dataHtml('#resultados .n1')
        # result is html. We have to transform it to array and parse        
        dataeti_pattern = re.compile(r'data-eti="([^"]+)"')
        output = []
        for item in result.items('a'):  # We Convert to array and go through the this
            match = dataeti_pattern.search(str(item))
            word = html.unescape(match.group(1))
            if match and word!=self.word and word not in output:
                output.append(word)
        return output

    def getWordsEnd(self):
        # This method get words that end with the word
        dataHtml = pq(self.URL + self.word + "?m=32", headers=self.headers)
        result = dataHtml('#resultados .n1')
        # result is html. We have to transform it to array and parse        
        dataeti_pattern = re.compile(r'data-eti="([^"]+)"')
        output = []
        for item in result.items('a'):  # We Convert to array and go through the this
            match = dataeti_pattern.search(str(item))
            word = html.unescape(match.group(1))
            if match and word!=self.word and word not in output:
                output.append(word)
        return output

    def getWordsContent(self):
        # This method get words that content the word
        dataHtml = pq(self.URL + self.word + "?m=33", headers=self.headers)
        result = dataHtml('#resultados .n1')
        # result is html. We have to transform it to array and parse        
        dataeti_pattern = re.compile(r'data-eti="([^"]+)"')
        output = []
        for item in result.items('a'):  # We Convert to array and go through the this
            match = dataeti_pattern.search(str(item))
            word = html.unescape(match.group(1))
            if match and word!=self.word and word not in output:
                output.append(word)
        return output