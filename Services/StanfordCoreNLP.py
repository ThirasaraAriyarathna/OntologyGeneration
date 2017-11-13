import os
import json
from pycorenlp import StanfordCoreNLP

class StanfordServer:

    def __init__(self, host='http://localhost', port=9000):
        self.nlp = StanfordCoreNLP('http://localhost:9000')
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

    def word_tokenize(self, sentence):
        return self.nlp.annotate(sentence, properties={'annotators': 'tokenize', 'outputFormat': 'json'})

    def pos(self, sentence):
        return self.nlp.annotate(sentence, properties={'annotators': 'pos', 'outputFormat': 'json'})

    def ner(self, sentence):
        return self.nlp.annotate(sentence, properties={'annotators': 'ner', 'outputFormat': 'json'})

    def parse(self, sentence):
        return self.nlp.annotate(sentence, properties={'annotators': 'parse', 'outputFormat': 'json'})

    def dependency_parse(self, sentence):
        return self.nlp.annotate(sentence, properties={'annotators': 'pos', 'outputFormat': 'json'})

    def annotate(self, sentence):
        return json.loads(self.nlp.annotate(sentence, properties=self.props))

    @staticmethod
    def tokens_to_dict(_tokens):
        tokens = defaultdict(dict)
        for token in _tokens:
            tokens[int(token['index'])] = {
                'word': token['word'],
                'lemma': token['lemma'],
                'pos': token['pos'],
                'ner': token['ner']
            }
        return tokens

if __name__ == '__main__':
    sNLP = StanfordServer()
    text = 'A blog post using Stanford CoreNLP Server. Visit www.khalidalnajjar.com for more details.'
    # print
    # "Annotate:", sNLP.annotate(text)
    # print
    # "POS:", sNLP.pos(text)
    print
    "Tokens:", sNLP.word_tokenize(text)
    # print
    # "NER:", sNLP.ner(text)
    # print
    # "Parse:", sNLP.parse(text)
    # print
    # "Dep Parse:", sNLP.dependency_parse(text)

