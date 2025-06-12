import streamlit as st
import pandas as pd
import numpy as np

st.title("Étude de l'overpricing sur le délai de vente")
st.text(
    "Analyse de l’impact d’une surcote ou d’une sous-cote sur la vitesse de vente"
    "avec la moyenne du marché."
)
st.write("ici, je pense prendre une fois par jour les annonces et analyser le moment où les annonces disparaissent et essayer de dégager un lien entre l'écart du prix du bien avec des autres du même type et de le temps de mise en ligne d'une annonce")
# À implémenter...
df_time = pd.DataFrame({
    "Ecart_de_prix_avec_le_marché": list(range(-10, 10)),
    "Durée_de_mise_en_ligne": [40 + 12 * i for i in range(20)]
    })
st.scatter_chart(df_time, x='Ecart_de_prix_avec_le_marché', y='Durée_de_mise_en_ligne')