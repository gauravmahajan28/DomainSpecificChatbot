from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

stopwords = [ "a", "about", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at",
              "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do",
              "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having",
              "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
              "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself",
              "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought",
              "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should",
              "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then",
              "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
              "to", "too", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what",
              "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's",
              "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
name_entity_map = {}
path = "./train.txt"

def training():
    file = open(path,'rt')

    for lines in file:
        name_entity_list = lines.split('\t')
        name_entity_list[1] = name_entity_list[1].strip('\n')
        name = name_entity_list[0].split(" ")

        for word in name:
            name_entity_map[word] = name_entity_list[1]

        #for k,v in name_entity_map.items():
            #print(k,"--",v)

def preprocess_query(query):
    query = query.lower()
    query = query.split()

    processed_query = []
    for word in query:
        processed_query.append(wordnet_lemmatizer.lemmatize(word))
    return processed_query


#input => Camera of xiaomi redmi note 4s pro
#output => [['camera', 'attribute'], ['xiaomi', 'data'], ['redmi note 4 pro', 'model']]

def get_ner(query):
    temp = []
    result = []

    training()
    query = preprocess_query(query)

    for word in query:
        tag = name_entity_map.get(word,"NA")
        temp.append([word,tag])

    composite_tag = temp[0][0]
    pre_tag = temp[0][1]

    for i in range(1,len(temp)):
        if temp[i][1] == pre_tag:
            composite_tag += " " + temp[i][0]
        else:
            result.append([composite_tag,pre_tag])
            composite_tag = temp[i][0]

        pre_tag = temp[i][1]

    if composite_tag!="":
        result.append([composite_tag,pre_tag])

    length = len(result)
    i=0
    while i < length:
        if result[i][0] in stopwords:
            del result[i]
        length = len(result)
        i+=1

    return result

def main():
    q1 = "Camera of xiaomi redmi note 4s pro"
    q2 = "All phones of xiaomi"
    q3 = "phones with snapdragon processor"
    q4 = "compare iphone x and redmi 4 screen"

    print("\n")
    result = get_ner(q1)
    print(q1)
    print(result)
    print("\n")

    result = get_ner(q2)
    print(q2)
    print(result)
    print("\n")

    result = get_ner(q3)
    print(q3)
    print(result)
    print("\n")

    result = get_ner(q4)
    print(q4)
    print(result)
    print("\n")


if __name__ = "__main__"
    main()

