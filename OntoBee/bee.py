import os
from Services.StanfordCoreNLP import StanfordServer
import nltk


class OntoBee:

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = filename = os.path.join(fileDir, '../Docs/test.txt')
    file_handle = open(filename)
    file_content = file_handle.read()
    file_handle.close()

    def weave(self):
        print(self.file_content)

    def __main__(self):
        stnfdnlp = StanfordServer()
        title_repair = self.file_content.split('\n')
        title_repair = '. '.join([sent for sent in title_repair if sent != ""])
        out = stnfdnlp.pos(title_repair)
        pos_sents = []
        for sentence in out["sentences"]:
            pos_sent = []
            for word in sentence["tokens"]:
                pos_sent.append((word["word"], word["pos"]))
            pos_sents.append(pos_sent)
        # print(pos_sents)
        grammar = r"""
                      NP:
                        {(<JJ>* <NN.*>+ <IN>)?}
                      """
        cp = nltk.RegexpParser(grammar)
        np_chunks = []
        for sent in pos_sents:
            np_chunks.append(cp.parse(sent))

        print(np_chunks)

bee = OntoBee()
bee.__main__()
