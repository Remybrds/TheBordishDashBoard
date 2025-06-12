#---------- init ----------


import streamlit as st
import pandas as pd


lien = "data/dataset_annonce_train.xlsx"
df = pd.read_excel(lien)

accueil = st.Page(page="../App/views/Acceuil.py", title="Accueil", default=True)

NeighboorFinder = st.Page(page="../App/views/NeighboorFinder.py", title="NeighboorFinder")

Overprincing = st.Page(page="../App/views/Overprincing.py", title="AccuOverprincingeil")

Resultats = st.Page(page="../App/views/Resultats.py", title="Resultats")

pg = st.navigation(pages = [accueil, NeighboorFinder, Overprincing, Resultats])

pg.run()
