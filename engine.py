import nltk
from nltk.stem import WordNetLemmatizer
import json, numpy, random
from nltk.stem.porter import PorterStemmer

def engine(userInput):
    #ambil data pattern response dari json
    with open("data.json") as file:
        data = json.load(file)

    #tangani jika user input null / exit
    if userInput == "":
        print("Response           : Ok Bye!")
        exit()
    elif userInput == "exit":
        print("Response           : Ok Bye!")
        exit()

    #hapus tanda baca
    def removePunctuation(txt):
            punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
            text_nopunct = "".join([c for c in txt if c not in punctuation])
            return text_nopunct
    userInput = removePunctuation(userInput.lower())

    #tokenisasi
    userInput = userInput.split()
    
    #stopword remove
    sw_list = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    def stopword_removal(tokens, sw_list):
        cleaned_token = []
        for t in tokens:
            if t not in sw_list:
                cleaned_token += [t]
        return cleaned_token
    userInput = stopword_removal(userInput, sw_list)
    
    #tempat hasil akhir
    hasil = {"Cosin": 0, "Index": 0}

    #hitung cosin antara setiap userinput dan pattern unutk dapatkan response
    for z, x in enumerate(data['data']):
        #remove stopword     
        data['data'][z]['pattern'] = stopword_removal(data['data'][z]['pattern'], sw_list) #pattern hapus stopword
        
        #lematization
        def lemma(token):
            lemmatizer = WordNetLemmatizer()    
            return [lemmatizer.lemmatize(t) for t in token]
        userInput = lemma(userInput)
        data['data'][z]['pattern'] = lemma(data['data'][z]['pattern'])

        #stemming
        def stemming(token):
            ps = PorterStemmer()
            return [ps.stem(t) for t in token]
        userInput = stemming(userInput)
        data['data'][z]['pattern'] = stemming(data['data'][z]['pattern'])
        
        
        #buat vocab  
        vocab = userInput + data['data'][z]['pattern']
        vocab = list(dict.fromkeys(vocab)) #hilangkan duplicate

        #buat bow antara userinput dan vocab
        frekuensiUserInput = [0] * len(vocab)
        for i, v in enumerate(vocab):
                for t in userInput:
                    if t == v:
                        frekuensiUserInput[i] += 1
        # print("BOW userInput : ", numpy.array(frekuensiUserInput))

        #buat bow antara pattern dan vocab
        frekuensiPattern = [0] * len(vocab)
        for i, v in enumerate(vocab):
                for t in data['data'][z]['pattern']:
                    if t == v:
                        frekuensiPattern[i] += 1
        frekuensiPattern = numpy.array(frekuensiPattern)
        # print("BOW pattern : ", frekuensiPattern)

        #hitung dot product
        dotProduct = sum(frekuensiPattern * frekuensiUserInput)
        # print(dotProduct)

        #hitung cosine
        jumlahKata = 0
        for x in frekuensiPattern:
            jumlahKata += x**2
        jumlahKata = jumlahKata**0.5
        # print(jumlahKata)
        jumlahKata2 = 0
        for x in frekuensiUserInput:
            jumlahKata2 += x**2
        jumlahKata2 = jumlahKata2**0.5
        # print(jumlahKata2)
        cosin = dotProduct / (jumlahKata * jumlahKata2)
        # print(cosin)

        #ambil hasil tertinggi masukkan ke var hasil
        if cosin > hasil['Cosin']:
            hasil['Cosin'] = cosin
            hasil['Index'] = z
    #ambil response secara random
    r = random.randint(0, len(data['data'][hasil['Index']]['response'])-1)
    return data['data'][hasil['Index']]['response'][r]
