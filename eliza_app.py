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
  [  "Neden %1 ihtiyacın var?",
    "Gerçekten %1 sana yardımcı olur mu?",
    "%1 ihtiyacın olduğuna emin misin?"]],

  [r'Neden sen ([^\?]*)\??',
  [ "Gerçekten benim %1 yapmadığımı mı düşünüyorsun?",
    "Belki bir gün ben de %1 yaparım.",
    "Beni %1 yapmaya mı teşvik ediyorsun?"]],

  [r'Neden ben ([^\?]*) yapamıyorum\??',
  [  "Sence %1 yapabilmeli misin?",
    "Eğer %1 yapabilseydin, ne yapardın?",
    "Bilmiyorum -- neden %1 yapamıyorsun?",
    "Gerçekten denedin mi?"]],

  [r'Ben (.*) yapamıyorum',
  [  "%1 yapamayacağını nereden biliyorsun?",
    "Belki denesen yapabilirsin.",
    "%1 yapmak için neye ihtiyacın var?"]],

  [r'Ben (.*)',
  [  "Bana geldiğin sebep %1 olman mı?",
    "Ne zamandan beri %1sin?",
    "%1 olmak hakkında nasıl hissediyorsun?"]],

  [r'Ben (.*)',
  [  "%1 olmak sana nasıl hissettiriyor?",
    "%1 olmaktan keyif alıyor musun?",
    "Neden bana %1 olduğunu söylüyorsun?",
    "Neden %1 olduğunu düşünüyorsun?"]],
  
  [r'Sen ([^\?]*)\??',
  [  "Benim %1 olup olmamam neden önemli?",
    "Benim %1 olmamı ister miydin?",
    "Belki benim %1 olduğuma inanıyorsun.",
    "Belki de %1'im -- ne düşünüyorsun?"]],

  [r'Ne (.*)',
  [  "Neden bunu soruyorsun?",
    "Bunun cevabı sana nasıl yardımcı olurdu?",
    "Sen ne düşünüyorsun?"]],

  [r'Nasıl (.*)',
  [  "Sence nasıl?",
    "Belki de bu sorunun cevabını kendin verebilirsin.",
    "Gerçekten neyi sormak istiyorsun?"]],

  [r'Çünkü (.*)',
  [  "Bu gerçekten sebep mi?",
    "Aklına başka hangi sebepler geliyor?",
    "Bu sebep başka bir şeye de uygulanabilir mi?",
    "Eğer %1, o zaman başka ne doğru olmalı?"]],

  [r'(.*) üzgünüm (.*)',
  [  "Bazen özür dilemek gereksiz olabilir.",
    "Özür dilediğinde ne hissediyorsun?"]],

  [r'Merhaba(.*)',
  [  "Merhaba... Bugün gelebildiğine sevindim.",
    "Selam, bugün nasılsın?",
    "Merhaba, bugün nasıl hissediyorsun?"]],

  [r'Bence (.*)',
  [  "%1 hakkında şüphelerin mi var?",
    "Gerçekten böyle mi düşünüyorsun?",
    "Ama %1 olduğuna emin değil misin?"]],

  [r'(.*) arkadaş (.*)',
  [  "Bana arkadaşların hakkında daha fazla anlat.",
    "Bir arkadaş düşündüğünde aklına ne geliyor?",
    "Neden bana çocukluk arkadaşlarından bahsetmiyorsun?"]],

  [r'Evet',
  [  "Oldukça emin görünüyorsun.",
    "Tamam, ancak biraz daha ayrıntılı anlatabilir misin?"]],

  [r'(.*) bilgisayar(.*)',
  [  "Gerçekten benim hakkımda mı konuşuyorsun?",
    "Bir bilgisayar ile konuşmak sana garip geliyor mu?",
    "Bilgisayarlar seni nasıl hissettiriyor?",
    "Bilgisayarlar seni korkutuyor mu?"]],

  [r'O (.*)',
  [  "Sence o %1 mi?",
    "Belki o %1'dir -- ne düşünüyorsun?",
    "Eğer o %1 olsaydı, ne yapardın?",
    "O gerçekten %1 olabilir."]],

  [r'O (.*)dir',
  [  "Oldukça emin görünüyorsun.",
    "Eğer sana bunun %1 olmadığını söylesem, nasıl hissederdin?"]],

  [r'Yapabilir misin ([^\?]*)\??',
  [  "Neden benim %1 yapamayacağımı düşünüyorsun?",
    "Eğer %1 yapabilseydim, ne olurdu?",
    "Neden bana %1 yapıp yapamayacağımı soruyorsun?"]],

  [r'Yapabilir miyim ([^\?]*)\??',
  [  "Belki de sen %1 yapmak istemiyorsun.",
    "%1 yapabilmek istiyor musun?",
    "Eğer %1 yapabilseydin, yapar mıydın?"]],

  [r'Sen (.*)',
  [  "Neden benim %1 olduğumu düşünüyorsun?",
    "Beni %1 olarak görmek seni mutlu ediyor mu?",
    "Belki benim %1 olmamı istiyorsun.",
    "Belki de aslında kendin hakkında konuşuyorsun?"]],
  
  [r'Sen (.*)',
  [  "Neden benim %1 olduğumu söylüyorsun?",
    "Neden benim %1 olduğumu düşünüyorsun?",
    "Biz senin hakkında mı, yoksa benim hakkımda mı konuşuyoruz?"]],

  [r'Ben (.*) yapmıyorum',
  [  "Gerçekten %1 yapmıyor musun?",
    "Neden %1 yapmıyorsun?",
    "%1 yapmak istiyor musun?"]],

  [r'Ben (.*) hissediyorum',
  [  "Güzel, bana bu hislerin hakkında daha fazla anlat.",
    "Sık sık %1 hissediyor musun?",
    "Genellikle ne zaman %1 hissediyorsun?",
    "%1 hissettiğinde ne yapıyorsun?"]],
  
  [r'Benim (.*) var',
  [  "Bana neden %1 olduğunu söylüyorsun?",
    "Gerçekten %1 mi var?",
    "Artık %1 olduğuna göre, bundan sonra ne yapacaksın?"]],

  [r'Ben (.*) isterdim',
  [  "Neden %1 yapmak istediğini açıklayabilir misin?",
    "Neden %1 yapmak isterdin?",
    "Başka kim %1 yapmak istediğini biliyor?"]],

  [r'Orada (.*) var mı',
  [  "Sence %1 var mı?",
    "Büyük ihtimalle %1 vardır.",
    "%1 olmasını ister miydin?"]],

  [r'Benim (.*)',
  [  "Anlıyorum, senin %1.",
    "Neden %1 hakkında böyle söylüyorsun?",
    "Senin %1 olduğunda nasıl hissediyorsun?"]],

  [r'Sen (.*)',
  [  "Aslında senin hakkında konuşmalıyız, benim değil.",
    "Neden benim hakkımda böyle söylüyorsun?",
    "Benim %1 olup olmamam neden önemli?"]],

  [r'Neden (.*)',
  [  "Bana neden %1 olduğunu söylemek istemiyor musun?",
    "Neden %1 olduğunu düşünüyorsun?"]],

  
  [r'Ben (.*) istiyorum',
  [  "Eğer %1 elde etseydin, senin için ne ifade ederdi?",
    "Neden %1 istiyorsun?",
    "%1 elde edersen ne yaparsın?",
    "Eğer %1 elde edersen, sonra ne yaparsın?"]],

  [r'(.*) anne(.*)',
  [  "Bana annen hakkında daha fazla anlat.",
    "Annenle olan ilişkin nasıldı?",
    "Annen hakkında nasıl hissediyorsun?",
    "Bu, şu anki hislerinle nasıl bağlantılı?",
    "İyi aile ilişkileri önemlidir."]],

  [r'(.*) baba(.*)',
  [  "Bana baban hakkında daha fazla anlat.",
    "Baban sana nasıl hissettirdi?",
    "Baban hakkında nasıl hissediyorsun?",
    "Babanla olan ilişkin şu anki hislerini nasıl etkiliyor?",
    "Ailene duygularını göstermek konusunda zorluk çekiyor musun?"]],

  [r'(.*) çocuk(.*)',
  [  "Çocukken yakın arkadaşların var mıydı?",
    "En sevdiğin çocukluk anın nedir?",
    "Çocuklukta gördüğün rüyalar veya kabuslar var mı?",
    "Diğer çocuklar bazen seninle dalga geçer miydi?",
    "Çocukluk deneyimlerinin şu anki hislerinle nasıl ilişkili olduğunu düşünüyorsun?"]],

  [r'(.*)\?',
  [  "Neden bunu soruyorsun?",
    "Lütfen kendi soruna cevap verebilir misin?",
    "Belki cevap içten geliyordur.",
    "Bana neden sormuyorsun?"]],

  [r'çıkış',
  [  "Benimle konuştuğun için teşekkür ederim.",
    "Hoşça kal.",
    "Teşekkürler, bu hizmetin bedeli $150. İyi günler!"]],

  [r'(.*)',
  [  "Lütfen bana daha fazla anlat.",
    "Konuya biraz daha odaklanalım... Bana ailenden bahseder misin?",
    "Bunu biraz açabilir misin?",
    "Neden böyle düşünüyorsun %1?",
    "Anlıyorum.",
    "Oldukça ilginç.",
    "%1.",
    "Anlıyorum. Peki bu sana ne anlatıyor?",
    "Bu seni nasıl hissettiriyor?",
    "Bunu söylediğinde nasıl hissediyorsun?"]]
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


