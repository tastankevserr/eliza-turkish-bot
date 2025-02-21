import streamlit as st
import re
import random

# Eliza Turkish Class
class ElizaTurkish:
    def __init__(self):
        self.keys = list(map(lambda x: re.compile(x[0], re.IGNORECASE), gPatsTurkish))
        self.values = list(map(lambda x: x[1], gPatsTurkish))

    def translate(self, text, vocabulary):
        words = text.lower().split()
        keys = vocabulary.keys()
        for i in range(len(words)):
            if words[i] in keys:
                words[i] = vocabulary[words[i]]
        return ' '.join(words)

    def respond(self, text):
        for i in range(len(self.keys)):
            match = self.keys[i].match(text)
            if match:
                resp = random.choice(self.values[i])
                pos = resp.find('%')
                while pos > -1:
                    num = int(resp[pos+1:pos+2])
                    resp = resp[:pos] + self.translate(match.group(num), gReflectionsTurkish) + resp[pos+2:]
                    pos = resp.find('%')
                if resp[-2:] == '?.': resp = resp[:-2] + '.'
                if resp[-2:] == '??': resp = resp[:-2] + '?'
                return resp
        return "Bunu tam olarak anlayamadım, biraz daha açabilir misin?"

# Geri dönüşüm sözlüğü
gReflectionsTurkish = {
  "ben": "sen",
  "benim": "senin",
  "bana": "sana",
  "bende": "sende",
  "benden": "senden",
  "sen": "ben",
  "senin": "benim",
  "sana": "bana",
  "sende": "bende",
  "seninki": "benimki",
  "benimki": "seninki"
}

# Eliza'nın yanıt desenleri
gPatsTurkish = [
  [r'Benim (.*) ihtiyacım var', 
   ["Neden %1 ihtiyacın var?", "Gerçekten %1 sana yardımcı olur mu?"]],
  [r'Ben (.*)', 
   ["Bana geldiğin sebep %1 olman mı?", "Ne zamandan beri %1sin?"]],
  [r'Ne (.*)', 
   ["Neden bunu soruyorsun?", "Sen ne düşünüyorsun?"]],
  [r'Nasıl (.*)', 
   ["Sence nasıl?", "Gerçekten neyi sormak istiyorsun?"]],
  [r'Evet', 
   ["Oldukça emin görünüyorsun.", "Tamam, ancak biraz daha ayrıntılı anlatabilir misin?"]],
  [r'çıkış', 
   ["Benimle konuştuğun için teşekkür ederim.", "Hoşça kal."]],
  [r'(.*)', 
   ["Lütfen bana daha fazla anlat.", "Bunu biraz açabilir misin?", "Neden böyle düşünüyorsun?"]]
]

# Streamlit UI
st.title("🧠 ELIZA - Türkçe Terapi Botu")
st.write("Merhaba! Bugün nasıl hissediyorsun?")

# Kullanıcı girişi
user_input = st.text_input("Sen:", "")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Gönder") and user_input:
    eliza = ElizaTurkish()
    response = eliza.respond(user_input)
    
    # Sohbet geçmişine ekle
    st.session_state.chat_history.append(("Sen", user_input))
    st.session_state.chat_history.append(("Eliza", response))

# Sohbet geçmişini göster
for speaker, text in st.session_state.chat_history:
    st.write(f"**{speaker}:** {text}")


