import streamlit as st


# Configuration du header
st.set_page_config(layout="wide")

# Définition des couleurs
background_color = "#000000"
main_content_color = "#FFFFFF"

# Création du header
header = st.empty()
header.markdown(
    f"""
    <div style="background-color: {background_color}; height: 100px; display: flex; align-items: center; 
    justify-content: space-between; padding: 20px;"> 
        <img src="https://via.placeholder.com/70" alt="Logo" style="height: 70px; width: 70px;">  <div style="color: {main_content_color};"> </div> </div> """,
    unsafe_allow_html=True,
)


# Création du contenu principal
main_content = st.empty()
main_content.markdown(
    """
    # Contenu principal de votre application Streamlit

    ## Description de votre application

    """,
    unsafe_allow_html=True,
)
