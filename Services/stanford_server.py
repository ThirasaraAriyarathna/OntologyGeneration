import subprocess


class StanfordServer:
    # LEFT3WORDS_PATH = './lib/english-left3words-distsim.tagger'
    # BIDIRECTIONAL_PATH = '../../libraries/english-bidirectional-distsim.tagger'
    JAR_PATH = '../Libraries/stanford-corenlp-full-2017-06-09'

    def __init__(self, jar_path: str = JAR_PATH, model_path: str = LEFT3WORDS_PATH, port: int = 9000) -> None:
        super().__init__()
        self.port = port
        self.jar_path = jar_path
        self.classpath = 'edu.stanford.nlp.pipeline.StanfordCoreNLPServer'
        self.model_path = model_path

    def __enter__(self):
        # Start Stanford Server
        print('Starting Stanford Server on Port %d ...' % self.port, end='', flush=True)
        self.subprocess = subprocess.Popen(
            ('java', '-mx4g', '-cp', '"*"', self.jar_path, self.classpath, '-annotators', '"tokenize,ssplit,pos,lemma,parse,sentiment"', '-port',
             str(self.port), 'timeout', '30000'), stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE)
        status = True
        # Wait while Server is Started, or terminate if error occurred
        try:
            out = self.subprocess.communicate(timeout=4)[0].decode('ascii')
            status = False
            print('... ERROR!')
            print(out)
        except subprocess.TimeoutExpired:
            # wait until some console output is given
            pass
        if status:
            print('... DONE!')
        else:
            self.subprocess.terminate()
            exit(0)

    def __exit__(self, type, value, traceback):
        # Terminate Server Process
        self.subprocess.terminate()

stfdserver = StanfordServer()
stfdserver.__enter__()