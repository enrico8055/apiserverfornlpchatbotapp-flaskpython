<h2>#SimpleNLPChatBotAPI<h2>
API sederhana yang bisa di hit dengan kirim key dan pertanyaan untuk chatbot melalui url dan akan di json berisi waktu request dan jawaban dari pertanyaan. sebagai ilustrasi API ini di buat untuk membantu toko penyedia layanan pemasangan wifi dan rakit pc membatu menjawab pertanyaan umum daru para pelanggannya.

Deployed At Heroku

Cara Hit:
GET https://api-chat-bot-nlp.herokuapp.com/get/melothria/query

NB :
query bisa di ubah jadi pertanyaan untuk chatbot, gunakan %20 untuk menggantikan spasi pada pertanyaan
key = melothria

Algoritma NLP: 
Cosin Similarty untuk hitung kemiripan antara pertanyaan dan beberapa pattern yang sudah ada sehingga kita bisa memilih jawaban random yang ada di lingkup pattern tersebut

