import spacy
from nltk.corpus import stopwords
from scipy.spatial.distance import cosine
import re

stop_words = list(stopwords.words('english'))

sentence1 = "Sachin Ramesh Tendulkar ( born 24 April 1973) is an Indian former international cricketer who served as captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket.[5] He is the highest run scorer of all time in International cricket. Considered as the world's most prolific batsman of all time,[6] he is the only player to have scored one hundred international centuries, the first batsman to score a double century in a One Day International (ODI), the holder of the record for the most runs in both Test and ODI cricket, and the only player to complete more than 30,000 runs in international cricket.[7] In 2013, he was the only Indian cricketer included in an all-time Test World XI named to mark the 150th anniversary of Wisden Cricketers' Almanack.[8][9][10] He is affectionately known as Little Master or Master Blaster.[11][12][13][14].Tendulkar took up cricket at the age of eleven, made his Test debut on 15 November 1989 against Pakistan in Karachi at the age of sixteen, and went on to represent Mumbai domestically and India internationally for close to twenty-four years. In 2002, halfway through his career, Wisden Cricketers' Almanack ranked him the second-greatest Test batsman of all time, behind Don Bradman, and the second-greatest ODI batsman of all time, behind Viv Richards.[15] Later in his career, Tendulkar was a part of the Indian team that won the 2011 World Cup, his first win in six World Cup appearances for India.[16] He had previously been named 'Player of the Tournament' at the 2003 edition of the tournament, held in South Africa."
sentence2 = "Sourav Chandidas Ganguly  born 8 July 1972), affectionately known as Dada (meaning 'elder brother' in Bengali), is an Indian cricket administrator, commentator and former national cricket team captain who is the 39th and current president of the Board of Control for Cricket in India. During his playing career, Ganguly established himself as one of the world's leading batsmen and also one of the most successful captains of the Indian national cricket team.[1][2][3] While batting, he was especially prolific through the off side, earning himself the nickname God of the Off Side for his elegant stroke play square of the wicket and through the covers.[4] As a cricketer he played as a left-handed opening batsman and was captain of the Indian national team. He was elected as a president of the BCCI in 2019.[5][6] and President of the Editorial Board with Wisden India.[7] Before being elected as the President of BCCI, he was the President of Cricket Association of Bengal, governing body for cricket in West Bengal, India."
nlp = spacy.load('en_core_web_lg')


def pre_process_text(input_text):
    # text_to_process = text_to_process.replace("[0-9]", "")
    text_to_process = re.sub("[0-9]", "", input_text)
    text_to_process = text_to_process.replace("[]", "")
    text_to_process = re.sub('[!,"*)@#%(&$_?.^]', ' ', text_to_process)
    words = text_to_process.split(" ")
    processed_words = []
    for each in words:
        if each not in stop_words:
            processed_words.append(each)
    return " ".join(processed_words)


def key_word_extraction(input_text):
    text_to_process = pre_process_text(input_text)
    each_nlp = nlp(text_to_process)
    svo_list = []
    for tok in each_nlp:
        if "subj" in tok.dep_ or "obj" in tok.dep_ or "ROOT" in tok.dep_:
            svo_list.append(tok.text)
            # print(tok.text, tok.dep_, tok.pos_)
    return " ".join(svo_list)


if __name__ == '__main__':
    svo_sentence1 = key_word_extraction(sentence1)
    svo_sentence2 = key_word_extraction(sentence2)
    vector1 = nlp(svo_sentence1).vector
    vector2 = nlp(svo_sentence2).vector
    query = "who scored more centuries"
    svo_query = key_word_extraction(query)
    query_vector = nlp(svo_query).vector
    svo_similarity1 = 1 - cosine(query_vector, vector1)
    svo_similarity2 = 1 - cosine(vector1, query_vector)
    svo_similarity3 = 1 - cosine(query_vector, vector2)
    svo_similarity4 = 1 - cosine(vector2, query_vector)
    print(f'{svo_similarity1}, {svo_similarity2},{svo_similarity3},{svo_similarity4}')
    print(svo_sentence1)
    print(svo_sentence2)
    print(svo_query)
