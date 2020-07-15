import nltk
import spacy


def ie_process(document):
    sentences = nltk.sent_tokenize(document)
    for sentence in sentences:
        print(sentence)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    print(sentences)
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    print(sentences)


def try_spacy(input_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)
    for sentence in doc.sents:
        token = sentence.root
        print(token.text, "-->", token.dep_, "-->", token.pos_)
        print(token.n_lefts)
        print(token.n_rights)
        for tok in sentence:
            print(tok.text, "-->", tok.dep_, "-->", tok.pos_)
        print("+++++++++++++++++++++++++++++++")


def find_sentence(input_text):
    print(input_text.find("charan"))
    print(input_text.find("sravya"))


if __name__ == "__main__":
    with open('input1.txt', 'r') as f:
        input_text = f.read()
        try_spacy(input_text)
        f.close()
