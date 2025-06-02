# app.py
import streamlit as st
import whisper
import requests
import tempfile
import time
import os
from config import add_footer
from doc import display_documentation # Importa a nova função de documentação

# --- Streamlit App UI ---
# THIS MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="Transcrição & Pontos-Chave", layout="wide")

# --- Google Material Icons Stylesheet ---
st.markdown("""
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <style>
        /* Optional: Adjust icon alignment and size */
        .material-symbols-outlined {
            vertical-align: middle;
            font-size: 1.3em; /* Adjust as needed */
        }
        /* Styles for colored text in markdown headings */
        .text-blue { color: #007bff; } /* Standard blue */
        .text-green { color: #28a745; } /* Standard green */
    </style>
""", unsafe_allow_html=True)

# --- Configuration ---
OLLAMA_API_URL = "http://localhost:11434/api/generate"
DEFAULT_OLLAMA_MODEL = "llama3"
DEFAULT_WHISPER_MODEL = "small" # "tiny", "base", "small", "medium", "large"

# --- Helper Functions ---

@st.cache_resource(show_spinner=False) # Cache o modelo Whisper para eficiência - Spinner do cache desabilitado
def load_whisper_model(model_name=DEFAULT_WHISPER_MODEL):
    """Carrega o modelo Whisper especificado."""
    try:
        model = whisper.load_model(model_name)
        return model
    except Exception as e:
        st.error(f"Erro ao carregar o modelo Whisper '{model_name}': {e}")
        st.info("Certifique-se de que os arquivos do modelo Whisper estão disponíveis ou tente um tamanho de modelo diferente.")
        return None

@st.cache_data(show_spinner=False) # Cache the transcription result - Spinner do cache desabilitado
def transcribe_audio_cached(whisper_model_name_for_cache, audio_bytes, original_filename="audio.wav"):
    """
    Transcreve os audio_bytes usando o modelo Whisper especificado (nome).
    Retorna o texto transcrito ou um string de erro específica.
    """
    model = None
    # Envolve a chamada a load_whisper_model com um spinner dedicado
    with st.spinner(f"Carregando modelo Whisper ({whisper_model_name_for_cache})...", show_time=True):
        model = load_whisper_model(whisper_model_name_for_cache)
    
    if model is None:
        return "ERRO_MODELO_NAO_CARREGADO"

    temp_file_suffix = os.path.splitext(original_filename)[1] if '.' in original_filename else ".tmp"
    with tempfile.NamedTemporaryFile(delete=False, suffix=temp_file_suffix) as tmp_audio_file:
        tmp_audio_file.write(audio_bytes)
        temp_audio_path = tmp_audio_file.name
    
    try:
        result = model.transcribe(temp_audio_path, fp16=False, language='pt') 
        return result["text"]
    except Exception: # pylint: disable=broad-except
        return "ERRO_TRANSCRICAO"
    finally:
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)

@st.cache_data(show_spinner=False) # Cache the key points extraction - Spinner do cache desabilitado
def get_key_points_from_ollama_cached(text_to_summarize, ollama_model_name):
    """
    Envia o texto para o Ollama para extrair pontos-chave.
    Retorna os pontos-chave ou um string de erro específica.
    """
    if not text_to_summarize or text_to_summarize in ["ERRO_MODELO_NAO_CARREGADO", "ERRO_TRANSCRICAO", "TEXTO_VAZIO_TRANSCRICAO"]:
        return "NENHUM_TEXTO_VALIDO_PARA_SUMARIZACAO"

    prompt = f"""
    Você é um especialista em sumarização. Dado o seguinte transcrito, por favor, extraia os principais pontos-chave.
    Apresente esses pontos-chave de forma clara e concisa, preferencialmente como uma lista com marcadores.

    Transcrito:
    "{text_to_summarize}"

    Pontos-chave:
    """
    payload = {
        "model": ollama_model_name,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=300) 
        response.raise_for_status()
        data = response.json()
        return data.get("response", "Nenhum ponto-chave extraído pelo Ollama.")
    except requests.exceptions.RequestException:
        return "ERRO_OLLAMA_COMUNICACAO"
    except Exception: # pylint: disable=broad-except
        return "ERRO_OLLAMA_INESPERADO"

# --- Lógica de exibição da Documentação ou App Principal ---
# Toggle for README page / Documentação
show_readme = st.toggle("📖 Ver Documentação Interativa", help="Clique para ver a documentação detalhada do projeto.")

if show_readme:
    # Não é mais necessário o spinner aqui, pois a função display_documentation não carrega arquivos externos.
    display_documentation() # Chama a função de documentação do doc.py
else:
    # --- Main Application Interface ---
    st.markdown(
        """# 🎙️ <span class="material-symbols-outlined">graphic_eq</span> <span class="text-blue">**Transcrição de Áudio com Whisper**</span> & <span class="material-symbols-outlined">psychology</span> <span class="text-green">**Extração de Pontos-Chave com Ollama**</span>""",
        unsafe_allow_html=True
    )
    st.caption("Faça o upload de um arquivo de áudio (.wav ou .mp3), e este aplicativo irá transcrevê-lo e extrair os pontos-chave.") 
    st.subheader(" ", divider="rainbow")

    st.sidebar.info("## Avaliação Online 7", icon="🎵") 

    whisper_model_options = ("tiny", "base", "small", "medium", "large") 
    try:
        default_whisper_index = whisper_model_options.index(DEFAULT_WHISPER_MODEL)
    except ValueError:
        default_whisper_index = 2 # Fallback para 'small'

    st.sidebar.caption("Escolha o modelo e realize o upload do arquivo de áudio")
    with st.sidebar.expander(":green[**CONFIGURAÇÕES**]", expanded=True, icon="⚙️"): 
        whisper_model_name = st.selectbox(
            ":blue[**Selecione o Modelo Whisper** ⤵️]", 
            whisper_model_options, 
            index=default_whisper_index, 
            help=":red[**- Modelos maiores são mais precisos**]\n\n :red[**Porém mais lentos e requerem mais recursos.**]" 
        )
    
        ollama_model_name = st.text_input(
            ":blue[**Nome do Modelo Ollama** ⤵️]", 
            DEFAULT_OLLAMA_MODEL, 
            help=":red[**Insira o nome do modelo Ollama que você baixou**]\n\n :green[**(ex: llama3, mistral).**]" 
        )
        
        st.subheader(" ", divider="rainbow")
        
        uploaded_file = st.file_uploader(
            ":blue[**Escolha um arquivo de áudio**] :green[**(.wav, .mp3)** ⤵️]", 
            type=["wav", "mp3", "ogg"], 
            help=":red[**Formatos suportados:**] :green[**WAV, MP3 e OGG**]"
        )
    
    if uploaded_file is not None:
        audio_bytes = uploaded_file.getvalue() 

        col_audio_player, col_process_button_placeholder = st.columns([0.7, 0.3]) 

        with col_audio_player:
            st.audio(audio_bytes, format=uploaded_file.type) 

        with col_process_button_placeholder:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True) 
            process_button_clicked = st.button("🚀 Processar Áudio", type="primary", use_container_width=True, key="process_audio_main")

        if process_button_clicked:
            # Spinner principal com show_time=True
            with st.spinner(f":blue[**Processando**] :gray[{uploaded_file.name}...] :orange[**Isso pode levar alguns minutos (ou carregar da cache).**]", show_time=True):
                
                transcription_status_placeholder = st.empty()
                transcription_status_placeholder.info(f"Iniciando transcrição com Whisper ({whisper_model_name})...")
                
                transcribed_text_result = None
                # Envolve a chamada a transcribe_audio_cached com um spinner dedicado
                with st.spinner(f"Transcrevendo áudio com Whisper ({whisper_model_name})...", show_time=True):
                    transcribed_text_result = transcribe_audio_cached(whisper_model_name, audio_bytes, uploaded_file.name)
                
                transcription_status_placeholder.empty() 
                
                transcription_col, key_points_col = st.columns(2)
                
                with transcription_col:
                    st.markdown("## <span class='material-symbols-outlined'>article</span> Transcrição", unsafe_allow_html=True)
                    if transcribed_text_result == "ERRO_MODELO_NAO_CARREGADO":
                        st.error(f"Modelo Whisper '{whisper_model_name}' não pôde ser carregado. Verifique a configuração.")
                        transcribed_text_for_ollama = None
                    elif transcribed_text_result == "ERRO_TRANSCRICAO":
                        st.error("Ocorreu um erro durante a transcrição do áudio.")
                        transcribed_text_for_ollama = None
                    elif not transcribed_text_result: 
                        st.warning("A transcrição resultou em texto vazio.")
                        st.text_area(":violet[**Transcrição Completa**]", "", height=350, key="transcription_area_empty")
                        transcribed_text_for_ollama = "TEXTO_VAZIO_TRANSCRICAO"
                    else:
                        st.toast("Transcrição concluída!", icon="🎉")
                        st.text_area("Transcrição Completa", transcribed_text_result, height=350, key="transcription_area_ok")
                        transcribed_text_for_ollama = transcribed_text_result

                with key_points_col:
                    st.markdown("## <span class='material-symbols-outlined'>vpn_key</span> Pontos-Chave", unsafe_allow_html=True)
                    if transcribed_text_for_ollama and transcribed_text_for_ollama not in ["ERRO_MODELO_NAO_CARREGADO", "ERRO_TRANSCRICAO", "TEXTO_VAZIO_TRANSCRICAO"]:
                        key_points_status_placeholder = st.empty()
                        key_points_status_placeholder.info(f"Extraindo pontos-chave com Ollama ({ollama_model_name})...")
                        
                        key_points_result = None
                        # Envolve a chamada a get_key_points_from_ollama_cached com um spinner dedicado
                        with st.spinner(f"Gerando pontos-chave com Ollama ({ollama_model_name})...", show_time=True):
                            key_points_result = get_key_points_from_ollama_cached(transcribed_text_for_ollama, ollama_model_name)
                        
                        key_points_status_placeholder.empty() 

                        if key_points_result == "ERRO_OLLAMA_COMUNICACAO":
                            st.error(f"Erro ao comunicar com o Ollama. Verifique se está rodando em {OLLAMA_API_URL} e o modelo '{ollama_model_name}' existe.")
                        elif key_points_result == "ERRO_OLLAMA_INESPERADO":
                            st.error("Ocorreu um erro inesperado ao tentar obter pontos-chave do Ollama.")
                        elif key_points_result == "NENHUM_TEXTO_VALIDO_PARA_SUMARIZACAO": 
                             st.warning("Não há texto válido da transcrição para extrair pontos-chave.")
                        elif key_points_result == "Nenhum ponto-chave extraído pelo Ollama.":
                            st.warning("O Ollama não retornou pontos-chave específicos.")
                            st.markdown(key_points_result, unsafe_allow_html=True)
                        else:
                            st.toast("Pontos-chave extraídos!", icon="🎉")
                            time.sleep(3) 
                            st.markdown(key_points_result, unsafe_allow_html=True)
                    elif transcribed_text_for_ollama == "TEXTO_VAZIO_TRANSCRICAO":
                        st.warning("Não é possível extrair pontos-chave pois a transcrição está vazia.")
                    else: 
                        st.warning("Não é possível extrair pontos-chave porque a transcrição falhou ou o modelo Whisper não foi carregado.")
            st.toast(f"Processamento de '{uploaded_file.name}' concluído!", icon="🎉")
            time.sleep(5) 
    else:
        st.markdown("<span class='material-symbols-outlined'>cloud_upload</span> Por favor, faça o upload de um arquivo de áudio para começar.", unsafe_allow_html=True) 
        st.sidebar.subheader(" ", divider="rainbow")

    st.sidebar.markdown(
        """<div style='text-align: center; font-size: 0.9em;'>
        Desenvolvido com: <br>
        <span class='material-symbols-outlined' style='font-size: 1em; vertical-align:sub;'>code</span> Python, 
        <span class='material-symbols-outlined' style='font-size: 1em; vertical-align:sub;'>rocket_launch</span> Streamlit, <br>
        <span class='material-symbols-outlined' style='font-size: 1em; vertical-align:sub;'>mic</span> Whisper, 
        <span class='material-symbols-outlined' style='font-size: 1em; vertical-align:sub;'>hub</span> Ollama
        </div>
        """, unsafe_allow_html=True
    )
    
    add_footer()