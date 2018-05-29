import os
import nltk.data
from tkinter import filedialog
from tkinter import *

_sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def create_file(newfilename):
    file = open(newfilename, 'w', encoding="utf-8")
    file.close()


def split_sentence(filename, text):
    sentences = _sent_detector.tokenize(text)
    needle = 0
    base=os.path.basename(filename)
    newfilename = os.path.splitext(base)[0] + "_sentences.txt"

    create_file(newfilename)
    
    for sent in sentences:
        start = text.find(sent, needle)
        end = start + len(sent) - 1
        needle += len(sent)
        file = open(newfilename, 'r', encoding="utf-8")

        content = file.readlines()
        content.append(sent + "\n")
        content.append(str(start) + "\n")
        content.append(str(end) + "\n")
        content.append(str(len(sent)-1) + "\n")
        content.append("----------\n")
        file = open(newfilename, 'w', encoding="utf-8")
        file.writelines(content)
        file.close()


if __name__ == '__main__':
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("All files","*.*")))
    fp = open(root.filename)
    data = fp.read()
    split_sentence(root.filename, data)