import nltk
from nltk.stem import WordNetLemmatizer
import json, string, numpy, random
from nltk.tokenize import word_tokenize

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
            text_nopunct = "".join([c for c in txt if c not in string.punctuation])
            return text_nopunct
    userInput = removePunctuation(userInput.lower())

    #tokenisasi
    userInput = word_tokenize(userInput)

    #tempat hasil akhir
    hasil = {"Cosin": 0, "Index": 0}

    #hitung cosin antara setiap userinput dan pattern unutk dapatkan response
    for z, x in enumerate(data['data']):
        #buat vocab
        vocab = userInput + data['data'][z]['pattern']
        vocab = list(dict.fromkeys(vocab)) #hilangkan duplicate
        def lemma(token):
            lemmatizer = WordNetLemmatizer()    
            return [lemmatizer.lemmatize(t) for t in token]
        vocab = lemma(vocab)
        # print("Vocab : ", vocab)

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

