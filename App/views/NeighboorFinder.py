import streamlit as st

st.title("Modèle trouvant les annonces les plus proches du bien à vendre")
st.text(
    "Ici, après avoir inséré les caractéristiques du bien à vendre, le modèle donnera une liste d'annonces actives proposant des caractéristiques "
    "proches du bien du client : nb pièces, proximité plage, parking, classe énergétique, "
    "surface, type de bien, etc., sans prendre en compte le prix de vente."
)

# Formulaire de critères
with st.form(key="property_form"):
    st.subheader("Entrez les caractéristiques du bien à vendre")

    # Localisation
    address = st.text_input("Adresse complète du bien", help="Permet de calculer les coordonnées géographiques")

    # Type et année de construction
    property_type = st.selectbox(
        "Type de bien", options=["Appartement", "Maison", "Studio", "Villa"]
    )
    construction_year = st.number_input(
        "Année de construction", min_value=1800, max_value=2025, value=2000, step=1
    )

    # Surface et pièces
    surface = st.number_input(
        "Surface habitable (m²)", min_value=10, max_value=500, value=80, step=1
    )
    land_surface = st.number_input(
        "Surface terrain (m²)", min_value=0, max_value=5000, value=0, step=10
    )
    nb_pieces = st.number_input(
        "Nombre de pièces", min_value=1, max_value=10, value=3, step=1
    )
    bedroom_count = st.number_input(
        "Nombre de chambres", min_value=0, max_value=10, value=2, step=1
    )

    # Étage
    floor = st.number_input(
        "Étage (numéro)", min_value=0, max_value=50, value=0, step=1,
        help="0 = rez-de-chaussée"
    )
    floor_count = st.number_input(
        "Nombre total d'étages", min_value=1, max_value=50, value=1, step=1
    )

    # Énergie et chauffage
    energy_class = st.selectbox(
        "Classe énergétique (DPE)", options=["A", "B", "C", "D", "E", "F", "G"]
    )
    heating_type = st.selectbox(
        "Type de chauffage", options=[
            "Balcon", "Terrasse", "Jardin", "Piscine", "Garage", "Parking extérieur", 
            "Parking couvert", "Cave", "Buanderie", "Cheminée", "Climatisation", 
            "Ascenseur", "Interphone", "Digicode", "Alarme", "Domotique", 
            "Accès PMR", "Vidéosurveillance", "Fibre optique"
        ]
    )
    heating_mode = st.selectbox(
        "Mode de chauffage", options=["Individuel", "Collectif"]
    )

    # Équipements / options
    options = st.multiselect(
        "Équipements (options)",
        options=["Balcon", "Ascenseur", "Parking extérieur", "Piscine", "Jardin", "Cave", "Terrasse"]
    )
    parking = st.checkbox("Parking disponible")

    submitted = st.form_submit_button("Trouver les annonces similaires")

if submitted:
    # Géocodage de l'adresse
    latitude, longitude = geocode_address(address) if address else (None, None)

    criteria = {
        "address": address,
        "latitude": latitude,
        "longitude": longitude,
        "property_type": property_type,
        "construction_year": construction_year,
        "surface": surface,
        "land_surface": land_surface,
        "nb_pieces": nb_pieces,
        "bedroom_count": bedroom_count,
        "floor": floor,
        "floor_count": floor_count,
        "energy_class": energy_class,
        "heating_type": heating_type,
        "heating_mode": heating_mode,
        "options": options,
        "parking": parking,
    }

    st.write("La suite à la prochaine page...")