import glob
from os.path import splitext, basename

CORPUS_PATH = "./UD_English-r1.4/not-to-release/sources/*/*.conllu"
PREFIX="# sentence-text: "
OUT_DIR = "./corpus"

def get_files():
    for f in glob.glob(CORPUS_PATH):
        yield f

def extract_sentences(fpath):
    with open(fpath) as f:
        for line in f:
            if line.startswith(PREFIX):
                yield line[len(PREFIX):].strip()

if __name__ == "__main__":
    for fpath in get_files():
        content = " ".join(list(extract_sentences(fpath)))
        fname = splitext(basename(fpath))[0]
        with open(OUT_DIR + "/" + fname + ".txt", "w") as f:
            f.write(content)
