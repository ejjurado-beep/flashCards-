
import streamlit as st
from deck import Deck

st.set_page_config(page_title="Flashcard Forge", page_icon="🧠", layout="centered")

st.title("🧠 Flashcard Forge")
st.write("Baraja, voltea y navega tus tarjetas sin que se reinicie el mazo.")

# --- Persistencia (NO se reinicia en cada click) ---
if "deck" not in st.session_state:
    st.session_state.deck = Deck("flashcards.csv")
    st.session_state.deck.shuffle()
    st.session_state.is_flipped = False

deck = st.session_state.deck
card = deck.get_current_card()

if deck.size() == 0:
    st.error("Tu CSV está vacío o mal formateado. Debe ser: pregunta,respuesta (sin encabezados).")
    st.stop()

# --- Display card ---
st.subheader(f"Carta {deck.current_index + 1} / {deck.size()}")

box_text = card.answer if st.session_state.is_flipped else card.question
label = " Respuesta" if st.session_state.is_flipped else " Pregunta"

st.markdown(f"### {label}")
st.info(box_text)

# --- Buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Shuffle"):
        deck.shuffle()
        st.session_state.is_flipped = False
        st.rerun()

with col2:
    if st.button(" Flip"):
        st.session_state.is_flipped = not st.session_state.is_flipped
        st.rerun()

with col3:
    if st.button(" Next"):
        deck.next_card()
        st.session_state.is_flipped = False
        st.rerun()
