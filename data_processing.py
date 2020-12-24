import os
import re
from collections import Counter, defaultdict

def func(matched):
    s = ""
    for word in matched.group():
        if word != '(' and word != '[' and word != ')' and word != ']':
            s += 'I'
    s = 'B' + s[1:]
    return s

def get_text_target(path):
    """
    generate the data for training and testing from source data
    """
    """ get_texts """
    text = []
    with open(os.path.join("data", path), "r", encoding="UTF-8") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            line = re.sub(r"\[\[\[\(\(\(", "", line)
            line = re.sub(r"\)\)\)\]\]\]", "", line)
            text.append(line)
    with open(os.path.join("processed_data", path, "text"), "w", encoding="UTF-8") as f:
        for line in text:
            f.write(line+'\n')
    """ get_target """
    label = []
    pattern = re.compile(r'\[\[\[\(\(\([^\[^\]]*\)\)\)\]\]\]')
    with open(os.path.join("data", path), "r", encoding="UTF-8") as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            line = re.sub(pattern, func, line)
            line = re.sub(r"\[\[\[\(\(\(", "", line)
            line = re.sub(r"\)\)\)\]\]\]", "", line)
            line = re.sub(r"[^BI]", "O", line)
            label.append(line)
    with open(os.path.join("processed_data", path, "target"), "w", encoding="UTF-8") as f:
        for line in label:
            f.write(line+'\n')

def check_data(path):
    """
    checking the data 
    return True or False
    """
    with open(os.path.join("processed_data", path, "text")) as ftext:
        with open(os.path.join("processed_data", path, "target")) as ftarget:
            text_lines = [line.strip() for line in ftext.readlines()]
            target_lines = [line.strip() for line in ftarget]
            for text, target in zip(text_lines, target_lines):
                if(len(text) != len(target)):
                    return False
                for i in target:
                    if i!='B' and i!='I' and i!='O':
                        return False
            return True

def build_vocab():
    """
    build the vocab from train data
    """
    all_words = []
    with open("processed_data/train/text", "r", encoding="UTF-8") as ftext:
        lines = [line.strip() for line in ftext.readlines()]
        for line in lines:
            all_words.extend(line)
    counter = Counter(all_words)
    common_words = counter.most_common() # 4242
    vocab_words = [pair[0] for pair in common_words[:4000]]
    with open("processed_data/vocab", "w", encoding="UTF-8") as f:
        for word in vocab_words:
            f.write(word+'\n')

if __name__ == "__main__":
    print("processing...")
    get_text_target("train")
    get_text_target("dev")
    get_text_target("test")

    print("checking...")
    if check_data("train") is False or check_data("dev") is False or check_data("test") is False:
        print("Error!!!")
    else:
        print("Ok!!!")

    build_vocab()
    print("Finished...")
    