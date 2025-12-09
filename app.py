import streamlit as st
import time
from streamlit_extras.let_it_rain import rain  # <--- JANGAN LUPA BARIS INI

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Pesan Untukmu",
    page_icon="🍂",
    layout="centered"
)

# --- CSS untuk Tampilan Estetik (Dark Mode & Clean) ---
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1 {
        text-align: center;
        font-weight: 300;
        margin-bottom: 20px;
        color: #FF4B4B;
    }
    p {
        text-align: justify;
        line-height: 1.6;
        font-size: 18px;
    }
    /* Tombol Style */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 1px solid #FF4B4B;
        color: #FF4B4B;
        background-color: transparent;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #FF4B4B;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- Fungsi Utama ---
def main():
    # 1. JUDUL / NAMA DIA
    st.title("FATHUL INGRID SUJAWATI") 
    st.markdown("---")

    # 2. LAGU (Opsional) - Bisa dihapus jika error
    # Ganti src di bawah dengan link embed lagu spotify pilihanmu
   # Bagian Lagu
    st.write("Play lagu nyaa...")
    
    # LINK RESMI SPOTIFY (Masing Masing - Ernie Zakri & Ade Govinda)
    st.components.v1.iframe(
        src="https://open.spotify.com/embed/track/7BgFlmOxrL7M1jVGoxqy37?utm_source=generator",
        width=700,
        height=80,
        scrolling=False
    )
    
    # 4. TOMBOL RAHASIA
    if st.button("for u"):
        with st.spinner("wait yaa......"):
            time.sleep(2.5)
            
        # 5. ISI PESAN JUJUR KAMU
        st.success("baca ya")
        
        st.markdown("""
        > *"Jujur, gua masi sering keinget lu, 
        di jalan yang biasa kita lewatin, tempat tempat yang pernah kita datengin.*
        
        > *gua ga minta kita balik seperti dulu. 
        kenapa?banyak alesannya, pasti lu tau. Dan gua mau ngasi tau lu kalo sekarang
        gua ngerasa balik lagi jadi willi pas belum kenal lu tapi dengan bayang bayang lu di hari hari"*
        
         > *Intinya semangat trus dan selamat untuk apa apa yang udah lu dapet setelah ga sama gua"*
        
        """)
        
        rain(
            emoji="🍂", # Ganti dengan emoji pilihanmu: 💔
            font_size=54,
            falling_speed=5,
            animation_length="infinite",
        )

if __name__ == "__main__":

    main()


