import streamlit as st
import pandas as pd
# Hier kommen später die Bibliotheken für LEA/AI hinzu

# 1. VALEO BRANDING (Header & Design)
st.set_page_config(page_title="Valeo Scanner", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .valeo-header {
        background-color: #000000;
        padding: 20px;
        color: #99cf16; /* Valeo Grün */
        font-size: 30px;
        font-weight: bold;
        border-bottom: 5px solid #99cf16;
        margin-bottom: 20px;
    }
    </style>
    <div class="valeo-header">VALEO - Digital Scan Assistant (LEA)</div>
    """, unsafe_allow_html=True)

# 2. SEITEN-LAYOUT
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Scan")
    uploaded_file = st.file_uploader("Datei hochladen (JPG/PDF)", type=["jpg", "png", "pdf"])
    
    if uploaded_file:
        st.success("Datei empfangen! LEA verarbeitet die Daten...")
        # Hier wird dein Sequential Prompt im Hintergrund ausgeführt
        # Beispiel-Ergebnis:
        new_data = {"Datum": "2023-10-27", "Info": "Beispiel Scan", "Status": "Erfolgreich"}
        st.write("Ergebnis von LEA:", new_data)

with col2:
    st.header("Datenbank / Suche")
    # Beispiel-Tabelle (Später Verknüpfung mit Google Sheets)
    df = pd.DataFrame([
        {"Datum": "2023-10-25", "Info": "Rechnung 123", "Status": "Geprüft"},
        {"Datum": "2023-10-26", "Info": "Lieferschein 456", "Status": "Offen"}
    ])
    
    search = st.text_input("Schnellsuche in der Tabelle")
    if search:
        df = df[df['Info'].str.contains(search)]
    
    st.dataframe(df, use_container_width=True)

# 3. VALEO FOOTER
st.markdown("""
    <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; font-size: 12px; color: gray;'>
    © 2023 Valeo - Internal Scanning Tool
    </div>
    """, unsafe_allow_html=True)

content_copy
