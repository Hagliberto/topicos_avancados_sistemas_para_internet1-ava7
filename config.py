import streamlit as st

def add_footer():
    # Definindo o estilo CSS para o rodapé, menu e animações
    st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #FFFFFF;
            color: #000000;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            transition: background-color 0.3s ease;
        }
        .footer:hover {
            background-color: #00FF7F;
        }
        .stButton button {
            width: 100%;
            background-color: white;
            color: #ff0000;
            border-radius: 10px;
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #ff0019;
            color: white;
        }
        .main-content {
            margin-top: 3rem;
            color: #e0e0e0;
        }
        /* Estilo do input de PIN */
        .pin-input {
            text-align: center;
            font-size: 20px;
            padding: 10px;
            margin: 20px auto;
            width: 150px;
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            transition: border-color 0.3s ease;
        }
        .pin-input:focus {
            border-color: #ff0000;
            outline: none;
        }
        /* Animação para o menu */
        .menu-item {
            transition: transform 0.3s ease, background-color 0.3s ease;
        }
        .menu-item:hover {
            transform: scale(1.05);
            background-color: #333333;
        }
        
    </style>
    """, unsafe_allow_html=True)
    
    # Adicionando o rodapé
    st.markdown('<div class="footer">👨🏻‍💻 Hagliberto Alves de Oliveira®️</div>', unsafe_allow_html=True)
    
        