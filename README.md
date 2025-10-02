# 🎾 Prediction Tennis Live

Dashboard multipagina per analisi live di match di tennis: inserimento manuale/da testo, OCR da screenshot, verdetto combinato.

## Avvio locale
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy su Streamlit Cloud
- Usa **requirements.txt** (versioni pin-nate)
- Aggiungi **packages.txt** (Tesseract + libGL)
- Configura **.streamlit/config.toml**
- Nessuna credenziale hardcoded → usa `.streamlit/secrets.toml`

## Funzionalità
- Inserimento manuale delle 8 key stats
- Parser da testo incollato (EN/IT)
- OCR (Tesseract) per BY-COURT
- Contesto live (BO3/BO5, set focus, score, server)
- Analisi media dei blocchi e verdetto con confidenza
