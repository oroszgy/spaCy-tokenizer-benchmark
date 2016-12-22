import glob
from functools import wraps
from time import time
from statistics import mean

from spacy import en


CORPUS_PATH = "./corpus"
EN = en.English(tagger=False, parser=False)

def timed(f):
    f.process_time = []

    @wraps(f)
    def wrapper(*args, **kwds):
        start = time()
        result = f(*args, **kwds)
        elapsed = time() - start
        f.process_time.append(elapsed*1000)
        return result
    return wrapper

@timed
def tokenize(fpath):
    with open(fpath) as f:
        EN.tokenizer(f.read())

if __name__ == "__main__":
    for f in glob.glob(CORPUS_PATH + "/*.txt"):
        tokenize(f)
    print("{:d} files, {:.2f}ms total, {:.2f}ms average, {:.2f}ms min, {:.2f}ms max".format(
        len(tokenize.process_time),
        sum(tokenize.process_time),
        mean(tokenize.process_time),
        min(tokenize.process_time),
        max(tokenize.process_time)
        ))
