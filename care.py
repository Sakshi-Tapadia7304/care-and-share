import streamlit as st
import datetime
from gtts import gTTS
import io

st.set_page_config(page_title="Care & Share", layout="centered")
st.title("🧸 Care & Share")
st.caption("Growing little hearts with love, wisdom, and safety 🌼")

# 🌐 Language selector
lang = st.selectbox("🗣️ Choose your language", ["English", "हिंदी", "తెలుగు"])
def trn(text): return text.get(lang, text["English"])

# 🗂️ Tab setup
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👪 For Parents",
    "🎨 For Babies",
    "🚫 Unsafe for Babies",
    "📿 Wisdom & Mantras",
    "🧠 Perfect Advisor"
])

# 👪 Tab 1: Daily Parenting Tips
with tab1:
    st.header("👪 Daily Parent Tips")
    st.info("🍼 Nap routines help babies feel safe and predictable.")
    st.info("👩‍👧 Talk often, even if they can't reply—your voice teaches everything.")
    st.info("📿 Use short spiritual stories to build resilience and empathy.")

# 🎨 Tab 2: Tap & Learn Baby Buttons
with tab2:
    st.header("🎨 Tap & Learn")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🐶 Dog"): st.success("Woof woof!")
        if st.button("🔴 Red"): st.success("Red like an apple!")
    with col2:
        if st.button("🐱 Cat"): st.success("Meow meow!")
        if st.button("🟡 Yellow"): st.success("Bright like the sun!")

# 🚫 Tab 3: Baby Safety Guidelines
with tab3:
    st.header("🚫 Unsafe for Babies")
    st.warning("❗ No honey before 12 months – risk of infant botulism")
    st.warning("❗ Avoid whole grapes, nuts, popcorn – choking hazard")
    st.warning("❗ Keep batteries, detergent, and sharp objects far from reach")
    st.info("✅ Choose large, soft, washable, and chew-safe toys")

# 📿 Tab 4: Wisdom, Time Tips, Mantra
with tab4:
    st.header("📿 Daily Wisdom & Mantra")

    # ⏰ Time-of-day parenting prompt
    hour = datetime.datetime.now().hour
    if hour < 9:
        st.info(trn({"English": "🧘 Morning: Chant 'Om' together",
                     "हिंदी": "🧘 सुबह: बच्चे के साथ 'ॐ' जपें",
                     "తెలుగు": "🧘 ఉదయం: పిల్లలతో కలిసి 'ఓం' జపించండి"}))
    elif hour < 13:
        st.info(trn({"English": "🍲 Lunch: Serve warm, simple food",
                     "हिंदी": "🍲 दोपहर: गरम, साधारण भोजन दें",
                     "తెలుగు": "🍲 మధ్యాహ్నం: వేడి, తేలికగా ఉండే ఆహారం ఇవ్వండి"}))
    elif hour < 18:
        st.info(trn({"English": "📖 Storytime: Gita or Ramayana tale",
                     "हिंदी": "📖 दोपहर: गीता या रामायण से कहानी सुनाएं",
                     "తెలుగు": "📖 మధ్యాహ్నం: గీత లేదా రామాయణం కథ చెప్పండి"}))
    else:
        st.info(trn({"English": "🌙 Bedtime: Hug gently and offer a prayer",
                     "हिंदी": "🌙 रात: प्यार से गले लगाकर प्रार्थना करें",
                     "తెలుగు": "🌙 నిద్రకి ముందు హత్తుకొని ప్రార్థన చెప్పండి"}))

    # 📖 Gita Verse of the Day
    verses = [
        {"shloka": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन ।", "meaning": "Do your duty, don't cling to the result. (2.47)"},
        {"shloka": "समत्वं योग उच्यते", "meaning": "Balance is true yoga. (2.48)"},
        {"shloka": "विद्या विनय सम्पन्ने ब्राह्मणे...", "meaning": "See divinity in all. (5.18)"}
    ]
    v = verses[datetime.datetime.now().day % len(verses)]
    st.markdown(f"🪔 *{v['shloka']}*")
    st.success(f"✨ {v['meaning']}")

    st.divider()

    # 🎵 Kindness Mantra
    st.subheader(trn({
        "English": "🎵 Gentle mantra for your child",
        "हिंदी": "🎵 आपके बच्चे के लिए मधुर मंत्र",
        "తెలుగు": "🎵 మీ పాపకు మృదువైన మంత్రం"
    }))
    if st.button("🔊 Play Kindness"):
        phrase = trn({
            "English": "Be gentle like Krishna's flute",
            "हिंदी": "कृष्ण की बांसुरी जैसी मधुरता लाओ",
            "తెలుగు": "కృష్ణుడి బాంసూరిలా మృదువుగా ఉండండి"
        })
        tts = gTTS(phrase, lang='hi' if lang == "हिंदी" else 'te' if lang == "తెలుగు" else 'en')
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        st.audio(audio.getvalue(), format="audio/mp3")

# 🧠 Tab 5: Perfect Advisor Bot
with tab5:
    st.header("🧠 Talk to Perfect Advisor")
    st.markdown(
        """
        <div style='background-color:#fff7e6; padding:1em; border-radius:10px;'>
        <h4 style='color:#4e342e;'>Ask anything about parenting, emotions, or gentle life guidance 🌿</h4>
        <p style='font-size:16px;'>Your soft-spoken friend is here to help.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.components.v1.iframe("https://huggingface.co/chat/assistants/perfect-advisor", height=600, scrolling=True)
