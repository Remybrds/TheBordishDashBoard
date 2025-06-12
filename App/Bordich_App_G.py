

# Chargement des données !!!!


# Fonction d'affichage du NeighborFinder
d

# Fonction du tableau de résultats



# Fonction d'étude de l'overpricing


if st.session_state["authentication_status"]:
    # Barre de navigation
    PAGES = ["Acceuil", "NeighborFinder", "Résultats", "Overpricing"]
    with st.sidebar:
        selection = option_menu(menu_title=None, options=PAGES)
        authenticator.logout("Déconnexion")
        
    # Routing
    
    elif selection == "NeighborFinder":
        neighbor_finder_page()
    elif selection == "Résultats":
        results_page()
    elif selection == "Overpricing":
        overpricing_page()
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.error("Les champs username et mot de passe doivent être remplie")

