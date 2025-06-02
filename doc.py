# doc.py
import streamlit as st

def display_documentation():
    """Exibe a documentação completa e formatada do projeto usando abas e colunas."""

    st.markdown("## <span class='material-symbols-outlined'>menu_book</span> Documentação Detalhada do Projeto", unsafe_allow_html=True)
    st.caption("Navegue pelas abas abaixo para explorar todos os aspectos do projeto, desde a configuração até o uso e solução de problemas.")
    st.subheader(" ", divider="rainbow")

    tab_labels = [ # Emojis diretamente nos nomes das abas para melhor apelo visual
        "🌟 Visão Geral",
        "🛠️ Tecnologias",
        "🖥️ Config. Ambiente",
        "🧠 Config. Modelos IA",
        "🚀 Executando o App",
        "🧭 Guia de Uso",
        "❓ FAQ/Problemas"
    ]
    tab_overview, tab_tech, tab_env_setup, tab_ia_setup, tab_running_app, tab_usage_guide, tab_faq = st.tabs(tab_labels)


    # --- Aba: Visão Geral ---
    with tab_overview:
        col_ov1, col_ov2 = st.columns(2)

        with col_ov1:
            st.success("### **Propósito e Objetivos**", icon="🎯")            
            st.markdown("""
            Este projeto foi concebido como resposta à atividade da disciplina :blue[**Tópicos Avançados em Sistemas para Internet I**] do curso :blue[**Tecnologia em Sistemas para Internet**]. Fundamentalmente, é uma ferramenta robusta e intuitiva para **transformar conteúdo de áudio em texto transcrito e, subsequentemente, em insights concisos através da extração de pontos-chave**.
            
            O objetivo principal é oferecer uma solução de código aberto que demonstre a integração eficaz de tecnologias de ponta em Inteligência Artificial (IA) para processamento de linguagem natural e áudio. A aplicação é acessível por meio de uma interface web interativa, priorizando a facilidade de uso e a execução local dos modelos para maior privacidade e controle do usuário.

            **Público-Alvo Principal:**
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>school</span> Estudantes e Pesquisadores:** Para transcrever aulas, palestras, entrevistas e facilitar a análise qualitativa e quantitativa de material de áudio.
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>business_center</span> Profissionais de Diversas Áreas:** Para registrar e sumarizar reuniões, workshops, depoimentos ou qualquer conteúdo falado relevante para suas atividades, otimizando o tempo e a retenção de informação.
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>campaign</span> Criadores de Conteúdo e Jornalistas:** Para gerar legendas, transcrever entrevistas ou resumos de podcasts, vídeos e outros materiais de áudio, agilizando o fluxo de trabalho.
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>developer_mode_tv</span> Desenvolvedores e Entusiastas de IA:** Como um exemplo prático e um ponto de partida para explorar a aplicação e integração de modelos como Whisper e LLMs via Ollama em projetos próprios.
            """, unsafe_allow_html=True)

        with col_ov2:
            st.success("### **Principais Benefícios**", icon="✨")
            st.markdown("""
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>schedule</span> Economia de Tempo:** Automatiza o processo manual e frequentemente demorado de transcrição, liberando tempo para tarefas mais estratégicas.
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>accessibility_new</span> Acessibilidade Aprimorada:** Torna o conteúdo de áudio mais acessível para pessoas com deficiência auditiva e facilita a pesquisa textual dentro do material falado.
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>analytics</span> Eficiência na Análise de Dados:** A extração de pontos-chave permite identificar rapidamente as informações cruciais e os temas centrais do áudio.
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>security</span> Privacidade e Controle Local:** Ao utilizar modelos que rodam localmente (especialmente com Ollama), os dados do usuário permanecem em sua máquina, garantindo maior privacidade e controle.
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>tune</span> Customização e Flexibilidade:** Oferece opções para selecionar diferentes modelos (tamanhos do Whisper, escolha do LLM no Ollama) de acordo com a necessidade específica de precisão, velocidade e recursos disponíveis.
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>code_off</span> Baixo Custo/Gratuito:** Utiliza ferramentas e modelos open-source, eliminando custos de APIs pagas para transcrição e processamento de linguagem.
            """, unsafe_allow_html=True)
        
        st.subheader(" ", divider="rainbow")
        st.subheader("🔑 Funcionalidades Detalhadas")
        
        # Funcionalidades em colunas, com cada feature em um container destacado
        cols_features_1, cols_features_2 = st.columns(2)
        
        with cols_features_1:
            with st.container(border=True):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>record_voice_over</span> Transcrição de Áudio Precisa", unsafe_allow_html=True)
                st.markdown("""
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>file_upload</span> Upload facilitado de arquivos de áudio nos formatos `.wav` e `.mp3`.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>hearing_disabled</span> Utilização do robusto modelo OpenAI Whisper para reconhecimento de fala.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>translate</span> Priorização para o idioma Português (`language='pt'`) para maior acurácia em conteúdos locais.
                """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True) 
            with st.container(border=True):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>psychology</span> Extração Inteligente de Pontos-Chave", unsafe_allow_html=True)
                st.markdown("""
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>hub</span> Integração com Modelos de Linguagem Grandes (LLMs) através do Ollama para análise semântica.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>edit_note</span> Identificação e apresentação concisa dos principais tópicos e informações da transcrição.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>dynamic_feed</span> Flexibilidade para o usuário definir qual modelo LLM (ex: `llama3`, `mistral`) localmente disponível no Ollama será utilizado.
                """, unsafe_allow_html=True)

        with cols_features_2:
            with st.container(border=True):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>tune</span> Configuração Flexível de Modelos", unsafe_allow_html=True)
                st.markdown("""
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>model_training</span> Seleção do tamanho do modelo Whisper (`tiny`, `base`, `small`, `medium`, `large`) para balancear velocidade e precisão.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>settings_ethernet</span> Campo para especificar o nome do modelo Ollama a ser utilizado, conforme configurado localmente pelo usuário.
                """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True) 
            with st.container(border=True):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>preview</span> Interface Clara e Feedback ao Usuário", unsafe_allow_html=True)
                st.markdown("""
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>smart_display</span> Interface web interativa e amigável construída com Streamlit.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>hourglass_top</span> Indicadores de progresso (spinners) com exibição de tempo decorrido durante as operações.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>play_circle</span> Player de áudio integrado para verificação do arquivo carregado.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>notifications_active</span> Notificações (toasts) para informar sobre a conclusão de etapas.
                """, unsafe_allow_html=True)
        
        st.subheader(" ", divider="rainbow")
        st.subheader("🏗️ Arquitetura Simplificada do Sistema")
        st.markdown("""
        O funcionamento da aplicação pode ser entendido através de suas principais camadas e o fluxo de dados entre elas:
        """)

        arch_col1, arch_col2, arch_col3 = st.columns(3)
        with arch_col1:
            st.markdown("<div align='center'><strong><span class='material-symbols-outlined' style='font-size:1.5em; vertical-align:middle;'>wysiwyg</span><br>1. Frontend<br>(Interface do Usuário)</strong></div>", unsafe_allow_html=True)
            st.caption("Desenvolvida com **Streamlit**. Coleta o áudio e as configurações do usuário, e exibe os resultados finais.")
        with arch_col2:
            st.markdown("<div align='center'><strong><span class='material-symbols-outlined' style='font-size:1.5em; vertical-align:middle;'>graphic_eq</span><br>2. Transcrição<br>(Processamento Local)</strong></div>", unsafe_allow_html=True)
            st.caption("Utiliza a biblioteca **OpenAI Whisper**. Converte o arquivo de áudio em texto bruto diretamente na máquina do usuário.")
        with arch_col3:
            st.markdown("<div align='center'><strong><span class='material-symbols-outlined' style='font-size:1.5em; vertical-align:middle;'>summarize</span><br>3. Pontos-Chave<br>(Processamento Local)</strong></div>", unsafe_allow_html=True)
            st.caption("Emprega **Ollama + LLM**. Recebe o texto transcrito e o processa para extrair os principais insights e pontos.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        # O título do fluxograma centralizado pelo HTML
        st.markdown("<p style='text-align:center; font-weight:bold;'><span class='material-symbols-outlined' style='vertical-align:middle; font-size:1.2em;'>flowsheet</span> Fluxo de Dados da Aplicação:</p>", unsafe_allow_html=True)
        
        # Usando colunas para centralizar o gráfico Graphviz e sua legenda
        # Ajuste as proporções [0.5, 3, 0.5] conforme necessário.
        # Isso significa que a coluna do meio (col_chart) ocupará 3 partes da largura,
        # enquanto as colunas laterais (espaçadores) ocuparão 0.5 parte cada.
        col_spacer1, col_chart, col_spacer2 = st.columns([0.5, 3, 0.5])

        with col_chart:
            st.graphviz_chart("""
                digraph {
                    rankdir="LR"; // Da esquerda para a direita

                    node [shape=box, style="rounded,filled", fillcolor="#E6F2FF", fontname="Arial", fontsize="10"];
                    edge [fontname="Arial", fontsize="9"];

                    // Nós representando os componentes
                    usuario [label="👤 Usuário", shape=circle, fillcolor="#FFEBE6"];
                    streamlit_app [label="🖥️ Interface Streamlit", fillcolor="#D1FFD1"];
                    whisper_engine [label="🎙️ Motor Whisper (Local)", fillcolor="#FFF0E6"];
                    ollama_llm [label="🧠 Ollama + LLM (Local)", fillcolor="#E6E6FF"];

                    // Arestas representando o fluxo de dados e interações
                    usuario -> streamlit_app [label=" Upload de Áudio\\n+ Configurações"];
                    streamlit_app -> whisper_engine [label="  Arquivo de Áudio  "];
                    whisper_engine -> streamlit_app [label="  Texto Transcrito  "];
                    streamlit_app -> ollama_llm [label="  Texto Transcrito  "];
                    ollama_llm -> streamlit_app [label="  Pontos-Chave  "];
                }
            """)
            
            st.caption("Diagrama do fluxo de dados principal da aplicação, da entrada do usuário até a exibição dos resultados.")
            
             
    # --- Aba: Tecnologias ---
    with tab_tech:
        st.subheader("🛠️ Stack Tecnológico Utilizado")
        st.markdown("""
        Este projeto é o resultado da sinergia entre diversas ferramentas e bibliotecas de ponta,
        cada uma desempenhando um papel crucial na funcionalidade e experiência do usuário.
        """)
        st.subheader(" ", divider="rainbow")

        col_tech1, col_tech2 = st.columns(2)
        with col_tech1:
            with st.expander("Python (Linguagem Principal)", expanded=False):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>code</span> Python", unsafe_allow_html=True)
                st.markdown("""
                Linguagem de programação versátil, poderosa e de alto nível, amplamente adotada em desenvolvimento web,
                ciência de dados, inteligência artificial e automação. Sua sintaxe clara e a vasta gama de bibliotecas
                (como PyTorch/TensorFlow, sobre os quais modelos como o Whisper são construídos) o tornam ideal para este tipo de aplicação.
                Neste projeto, Python é a espinha dorsal que interconecta todos os componentes.
                """)

            with st.expander("OpenAI Whisper (Transcrição de Áudio)", expanded=False):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>mic_external_on</span> OpenAI Whisper", unsafe_allow_html=True)
                st.markdown("""
                Um modelo de Reconhecimento Automático de Fala (ASR) de última geração, desenvolvido e treinado pela OpenAI.
                É capaz de transcrever áudio em múltiplos idiomas com notável precisão, mesmo em condições de áudio
                desafiadoras (ruído, sotaques diversos). Sua arquitetura robusta e a disponibilidade de modelos de
                diferentes tamanhos permitem um equilíbrio entre velocidade de processamento e acurácia da transcrição.
                [Saiba mais sobre Whisper](https://openai.com/research/whisper).
                """)

            with st.expander("Requests (Comunicação HTTP)", expanded=False):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>http</span> Requests", unsafe_allow_html=True)
                st.markdown("""
                Uma biblioteca Python elegante e simples para fazer requisições HTTP. Considerada o padrão de fato para
                interações HTTP em Python devido à sua API amigável. Neste projeto, é essencial para permitir que
                a aplicação Streamlit envie o texto transcrito para o servidor local do Ollama (que expõe uma API REST)
                e receba os pontos-chave gerados pelo LLM.
                """)

        with col_tech2:
            with st.expander("Streamlit (Interface Web)", expanded=False):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>dashboard_customize</span> Streamlit", unsafe_allow_html=True)
                st.markdown("""
                Um framework open-source em Python que permite transformar scripts de análise de dados e modelos de IA
                em aplicações web interativas e compartilháveis com um esforço mínimo de codificação frontend.
                Sua facilidade de uso, vasta gama de widgets interativos (botões, seletores, upload de arquivos, etc.)
                e capacidade de recarregamento rápido tornam o desenvolvimento e a prototipagem ágeis.
                [Visite Streamlit](https://streamlit.io).
                """)

            with st.expander("Ollama (LLMs Locais)", expanded=False):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>hub</span> Ollama", unsafe_allow_html=True)
                st.markdown("""
                Uma plataforma poderosa que simplifica drasticamente o processo de download, configuração e execução
                de Modelos de Linguagem Grandes (LLMs) populares, como Llama, Mistral, Gemma, entre outros, diretamente
                na sua máquina local. Ollama promove a experimentação e o uso de IA generativa com maior privacidade,
                controle e sem a necessidade de depender de APIs externas ou custos associados. Suporta uma crescente
                biblioteca de modelos abertos. [Conheça o Ollama](https://ollama.com).
                """)
        
        st.subheader(" ", divider="rainbow")
        st.warning(
            """**Dependência Externa Essencial: FFmpeg**
            
            ⚠️ O `ffmpeg` é uma suíte de software crucial para manipulação de multimídia. No contexto deste projeto,
            o Whisper depende do `ffmpeg` para decodificar e processar uma ampla variedade de formatos de arquivo de áudio
            antes da transcrição. Sua ausência ou configuração incorreta no sistema resultará em falhas na
            transcrição. As instruções detalhadas de instalação do `ffmpeg` podem ser encontradas na aba "Config. Ambiente".
            """, 
            icon="🚨"
        )

    # --- Aba: Configuração do Ambiente ---
    with tab_env_setup:
        st.subheader("🖥️ Configuração do Ambiente de Desenvolvimento/Execução")
        st.markdown("Siga estes passos detalhados para preparar seu ambiente local e executar a aplicação. Uma configuração correta é essencial para que todas as funcionalidades operem como esperado.")
        st.subheader(" ", divider="rainbow")

        # Primeiros 4 passos em duas colunas
        col_env1, col_env2 = st.columns(2)

        with col_env1:
            with st.expander("Passo 1: Instalação do Python", expanded=False): # Manter o primeiro expandido
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>code</span> 1. Python", unsafe_allow_html=True)
                st.info("➡️ Certifique-se de ter Python instalado. Versões **3.8 a 3.11** são recomendadas. Você pode baixar Python em [python.org](https://www.python.org/downloads/).", icon="🐍")
                st.markdown("""
                - Após a instalação, é crucial verificar se o Python e o `pip` (o gerenciador de pacotes do Python) estão corretamente configurados nas variáveis de ambiente do seu sistema (PATH). Abra um novo terminal ou prompt de comando e execute:
                  ```bash
                  python --version
                  pip --version
                  ```
                - Se os comandos não forem reconhecidos, você precisará adicionar manualmente os diretórios de instalação do Python e da sua subpasta `Scripts` (onde o `pip` geralmente reside no Windows) à variável de ambiente PATH do seu sistema.
                """)

            with st.expander("Passo 2: Criação de Ambiente Virtual (Recomendado)", expanded=False):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>eco</span> 2. Ambiente Virtual", unsafe_allow_html=True)
                st.success("💡 Para evitar conflitos de dependência entre diferentes projetos Python e manter seu ambiente global limpo, é uma **excelente prática de desenvolvimento** usar um ambiente virtual dedicado para este projeto.", icon="🛡️")
                st.markdown("""
                **Benefícios:**
                - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>shield</span> Isolamento:** As bibliotecas e suas versões específicas instaladas para este projeto não interferirão com outros projetos Python ou com a instalação global do Python no seu sistema.
                - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>repeat</span> Reprodutibilidade:** Facilita a recriação do mesmo ambiente de desenvolvimento em outras máquinas ou por outros colaboradores, usando um arquivo `requirements.txt`.

                **Como criar e ativar (exemplo usando `venv`):**
                No seu terminal, navegue até a pasta onde você deseja criar o projeto (ou onde você já extraiu os arquivos) e execute:
                ```bash
                # 1. Criar o ambiente virtual (será criada uma pasta chamada '.venv')
                python -m venv .venv

                # 2. Ativar o ambiente virtual:
                #    No Linux/macOS:
                source .venv/bin/activate
                #    No Windows (Prompt de Comando):
                #    .venv\\Scripts\\activate.bat
                #    No Windows (PowerShell):
                #    .venv\\Scripts\\Activate.ps1
                ```
                - <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>terminal</span> *Você normalmente verá o nome do ambiente (ex: `(.venv)`) no início do prompt do seu terminal, indicando que ele está ativo.*
                - <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>playlist_add_check</span> *Todos os comandos `pip install` para este projeto devem ser executados com o ambiente virtual ativado.*
                - <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>toggle_off</span> Para desativar o ambiente virtual quando terminar de trabalhar no projeto, simplesmente digite `deactivate` no terminal.
                """, unsafe_allow_html=True)

        with col_env2:
            with st.expander("Passo 3: Obtenção do Código Fonte do Projeto", expanded=False):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>folder_zip</span> 3. Código Fonte do Projeto", unsafe_allow_html=True)
                st.markdown("""
                Você precisará dos arquivos da aplicação (`app.py`, `doc.py`, etc.) para executá-la.
                - **<span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>archive</span> Se você recebeu os arquivos como um `.zip`:** Extraia o conteúdo para uma pasta de sua preferência no seu computador.
                - **<span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>hub</span> Se for um repositório Git (exemplo):** Use o Git para clonar o repositório (substitua a URL pelo link correto, se aplicável).
                  ```bash
                  git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
                  cd NOME_DO_REPOSITORIO_CLONADO
                  ```
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>snippet_folder</span> A estrutura básica de arquivos que você deve ter na pasta do projeto inclui, no mínimo:
                    - `app.py` (o script principal da aplicação Streamlit)
                    - `doc.py` (este arquivo de documentação)
                    - `requirements.txt` (arquivo de dependências Python, veja o próximo passo)
                    - Opcionalmente, `config.py` (se usado para configurações como o rodapé).
                """, unsafe_allow_html=True)

            with st.expander("Passo 4: Instalação das Dependências Python", expanded=False):
                st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>list_alt</span> 4. Instalação das Dependências Python", unsafe_allow_html=True)
                st.markdown("""
                As bibliotecas Python externas necessárias para o funcionamento do projeto estão listadas em um arquivo `requirements.txt`.
                
                1.  **<span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>description</span> Crie o arquivo `requirements.txt`** na raiz do seu projeto com o seguinte conteúdo:
                    ```text
streamlit
openai-whisper
requests
                    ```
                2.  **<span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>download</span> Instale as dependências:** Com o ambiente virtual (se você criou um) **ativado**, execute o seguinte comando no terminal:
                    ```bash
                    pip install -r requirements.txt
                    ```
                Isso instalará as seguintes bibliotecas e suas respectivas dependências:
                - **<span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>rocket_launch</span> Streamlit:** Framework utilizado para construir e servir a interface web interativa da aplicação.
                - **<span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>mic</span> OpenAI Whisper:** Biblioteca da OpenAI para realizar a transcrição de áudio para texto de alta precisão.
                - **<span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>http</span> Requests:** Biblioteca para realizar chamadas HTTP, usada  para comunicar com a API local do servidor Ollama.
                """, unsafe_allow_html=True)
                st.caption("Nota: A dependência `ffmpeg`, que é crucial para o Whisper, é uma instalação a nível de sistema e é tratada no próximo passo.")
        
        st.subheader(" ", divider="rainbow")

        with st.expander("Passo 5: Instalação do FFmpeg (Dependência Crítica para Whisper)", expanded=False):
            st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>movie_filter</span> 5. FFmpeg", unsafe_allow_html=True)
            st.error("🛑 **FFmpeg é absolutamente essencial** para que a biblioteca Whisper possa processar arquivos de áudio corretamente. \n\nSem o FFmpeg instalado e devidamente configurado no PATH do seu sistema, a funcionalidade de transcrição provavelmente falhará ou não suportará todos os formatos de áudio.", icon="⚠️")
            
            st.markdown("Instale o FFmpeg no seu sistema operacional:")
            
            # Instruções do FFmpeg em três colunas
            col_ffmpeg_linux, col_ffmpeg_mac, col_ffmpeg_win = st.columns(3)

            with col_ffmpeg_linux:
                st.markdown("##### <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>terminal</span> Linux (Debian/Ubuntu)", unsafe_allow_html=True)
                st.markdown("""
                Execute no terminal:
                ```bash
                sudo apt update && sudo apt install ffmpeg
                ```
                """, unsafe_allow_html=True)
            
            with col_ffmpeg_mac:
                st.markdown("##### <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>desktop_mac</span> macOS (Homebrew)", unsafe_allow_html=True)
                st.markdown("""
                Se você usa o [Homebrew](https://brew.sh/index_pt-br):
                ```bash
                brew install ffmpeg
                ```
                """, unsafe_allow_html=True)

            with col_ffmpeg_win:
                st.markdown("##### <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>desktop_windows</span> Windows", unsafe_allow_html=True)
                st.markdown("""
                1.  <span class='material-symbols-outlined' style='font-size:0.9em; vertical-align:middle;'>download_for_offline</span> Baixe os binários (ex: de [Gyan.dev](https://www.gyan.dev/ffmpeg/builds/)).
                2.  <span class='material-symbols-outlined' style='font-size:0.9em; vertical-align:middle;'>folder_open</span> Extraia para uma pasta (ex: `C:\\ffmpeg`).
                3.  <span class='material-symbols-outlined' style='font-size:0.9em; vertical-align:middle;'>rule_folder</span> Adicione a pasta `bin` (ex: `C:\\ffmpeg\\bin`) ao PATH do sistema.
                4.  <span class='material-symbols-outlined' style='font-size:0.9em; vertical-align:middle;'>restart_alt</span> **Reinicie** terminais abertos ou o sistema.
                """, unsafe_allow_html=True)
            
            st.subheader(" ", divider="rainbow")
            st.markdown("""
            **<span class='material-symbols-outlined' style='vertical-align:middle;'>task_alt</span> Verificando a Instalação do FFmpeg:**
            Para confirmar, abra um **novo** terminal e digite:
            ```bash
            ffmpeg -version
            ```
            Você deverá ver informações sobre a versão do FFmpeg. Se ocorrer um erro de "comando não encontrado", revise a instalação e a configuração do PATH.
            """, unsafe_allow_html=True)

    # --- Aba: Configuração dos Modelos IA ---
    with tab_ia_setup:
        st.subheader("🧠 Configuração dos Modelos de Inteligência Artificial")
        st.markdown("""
        Esta seção detalha como configurar os modelos de IA necessários para as funcionalidades de transcrição (Whisper)
        e extração de pontos-chave (Ollama com LLMs). Uma configuração correta é crucial para o funcionamento do aplicativo.
        """)
        st.subheader(" ", divider="rainbow")

        col_whisper, col_ollama = st.columns(2)

        with col_whisper:
            st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>hearing</span> 1. Modelos Whisper (Transcrição)", unsafe_allow_html=True)
            
            with st.expander("Detalhes e Considerações sobre os Modelos Whisper", expanded=False):
                st.markdown("""
                Os modelos de transcrição do OpenAI Whisper são o coração da funcionalidade de conversão de áudio para texto.
                Eles são gerenciados pela própria biblioteca `openai-whisper`.
                
                - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>file_download</span> Download Automático:** Ao selecionar um tamanho de modelo na interface do aplicativo (`tiny`, `base`, `small`, `medium`, `large`) pela primeira vez, o modelo correspondente será baixado automaticamente.
                - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>wifi</span> Requisito de Internet:** É necessária uma conexão com a internet para este download inicial de cada modelo.
                - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>folder_managed</span> Local de Cache:** Os modelos baixados são armazenados localmente para uso futuro, geralmente na pasta `~/.cache/whisper` (no diretório home do seu usuário, dentro da pasta `.cache`).
                - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>tune</span> Considerações sobre os Modelos:**
                    - Modelos menores (ex: `tiny`, `base`, `small`) são **mais rápidos** e exigem **menos recursos** computacionais (RAM/VRAM), mas podem ser **menos precisos** na transcrição.
                    - Modelos maiores (ex: `medium`, `large`) oferecem **maior precisão**, mas são **significativamente mais lentos** e consomem **mais recursos**. O modelo `large` pode ser particularmente pesado para CPUs e se beneficia enormemente de uma GPU NVIDIA com suporte a CUDA.
                    - **Desempenho:** Os modelos são otimizados para rodar em CPU, mas o desempenho, especialmente dos modelos `medium` e `large`, é substancialmente melhor com uma GPU NVIDIA compatível.
                """, unsafe_allow_html=True)
                st.caption("O aplicativo está configurado para priorizar transcrições em Português (`language='pt'`).")

        with col_ollama:
            st.markdown("#### <span class='material-symbols-outlined' style='vertical-align:middle;'>hub</span> 2. Ollama e LLMs (Pontos-Chave)", unsafe_allow_html=True)
            st.markdown("""
            Ollama é a plataforma utilizada para executar Modelos de Linguagem Grandes (LLMs) localmente em sua máquina.
            Estes LLMs analisam o texto transcrito para extrair os pontos-chave. <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>psychology</span>
            """, unsafe_allow_html=True)
            
            with st.expander("Etapa 2.1: Instalação do Ollama", expanded=False):
                st.markdown("##### <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>system_update_alt</span> Guia de Instalação", unsafe_allow_html=True)
                st.markdown("""
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>link</span> Visite o [site oficial do Ollama](https://ollama.com/download) e baixe o instalador para seu sistema operacional (Windows, macOS, Linux).
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>desktop_windows</span> Siga as instruções de instalação fornecidas.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>terminal</span> Após a instalação, abra um **novo terminal** e execute `ollama --version` para confirmar.
                """, unsafe_allow_html=True)

            with st.expander("Etapa 2.2: Download de Modelos LLM via Ollama", expanded=False):
                st.markdown("##### <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>model_training</span> Baixando os Modelos Necessários", unsafe_allow_html=True)
                st.markdown("""
                Antes de usar um LLM com o aplicativo, você precisa baixá-lo usando o Ollama. O aplicativo sugere `llama3` por padrão.
                <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>terminal</span> Abra seu terminal e execute:
                ```bash
                # Para baixar o Llama 3 (modelo 8B, ~4.7GB, bom equilíbrio)
                ollama pull llama3

                # Para baixar o Mistral (outro modelo popular, ~4.1GB)
                ollama pull mistral

                # Para um modelo menor e mais rápido (ex: Qwen2 0.5B, ~0.4GB)
                ollama pull qwen2:0.5b
                ```
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>pageview</span> Explore mais modelos na [biblioteca Ollama](https://ollama.com/library).
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>badge</span> O nome usado no comando `pull` (ex: `llama3`) é o que você deve inserir na interface do app.
                - **Tamanhos dos Modelos:** LLMs vêm em diversos tamanhos (ex: 0.5B, 7B, 13B, 70B parâmetros). Modelos maiores são geralmente mais capazes, mas exigem mais RAM e poder de processamento. Verifique os requisitos.
                - **Atualizar um Modelo:** Para obter a versão mais recente de um modelo: `ollama pull nome_do_modelo` (ou `nome_do_modelo:latest`).
                """, unsafe_allow_html=True)

            with st.expander("Etapa 2.3: Executando o Servidor Ollama", expanded=False):
                st.markdown("##### <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>dns</span> Execução e Verificação do Servidor", unsafe_allow_html=True)
                st.markdown("""
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>power</span> **Serviço em Background (Padrão):** Em muitas instalações, o Ollama inicia automaticamente.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>play_circle</span> **Início Manual / Ver Logs:** Se precisar iniciar manualmente ou quiser ver os logs em tempo real (útil para depuração), abra um terminal e execute:
                  ```bash
                  ollama serve
                  ```
                  Se executar `ollama serve` em primeiro plano no terminal, você verá os logs de atividade do servidor diretamente.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>lan</span> **Verificação da Porta:** O servidor opera por padrão em `http://localhost:11434`.
                - <span class='material-symbols-outlined' style='font-size:1em; vertical-align:middle;'>list_alt</span> **Listar Modelos Baixados:** Para ver os modelos que você tem localmente:
                  ```bash
                  ollama list
                  ```
                """, unsafe_allow_html=True)
        
        st.subheader(" ", divider="rainbow") 
        st.warning(
            """
            **Crítico: Ollama e Modelos LLM**

            O servidor Ollama deve estar em execução, e o modelo LLM que você especificar na interface do aplicativo precisa ter sido previamente baixado com `ollama pull` e estar listado em `ollama list` para que a funcionalidade de extração de pontos-chave funcione corretamente. 
            - :red[‼️ **Caso contrário, você encontrará erros de comunicação ou o campo de pontos-chave ficará vazio.**]
            """, 
            icon="🚨"
        )

    # --- Aba: Executando a Aplicação ---
    with tab_running_app: #
        st.subheader("🚀 Executando a Aplicação Streamlit") 
        st.markdown("""
        Com todos os pré-requisitos e configurações do ambiente e dos modelos de IA concluídos (detalhados nas abas anteriores), você está pronto para iniciar o aplicativo.
        """) 
        st.subheader(" ", divider="rainbow")

        col_checklist, col_steps = st.columns([0.8, 1.2]) # Ajuste a proporção se desejar

        with col_checklist:
            # Título corrigido usando st.markdown para renderizar o ícone HTML e adicionando o emoji ✅ manualmente
            st.markdown("#### <span class='material-symbols-outlined'>checklist</span> Checklist Rápido Antes de Executar:", unsafe_allow_html=True)
            
            # A lista de marcadores abaixo já estava correta com unsafe_allow_html=True no seu st.markdown
            st.markdown("""
            - <span class='material-symbols-outlined' style='vertical-align:middle; font-size:1.1em;'>toggle_on</span> Ambiente virtual **ativado**?
            - <span class='material-symbols-outlined' style='vertical-align:middle; font-size:1.1em;'>dns</span> Servidor Ollama **rodando**?
            - <span class='material-symbols-outlined' style='vertical-align:middle; font-size:1.1em;'>download_done</span> Modelo LLM desejado **baixado** via Ollama (ver aba "Config. Modelos IA")?
            - <span class='material-symbols-outlined' style='vertical-align:middle; font-size:1.1em;'>folder_zip</span> Você está no **diretório correto** do projeto no terminal?
            - <span class='material-symbols-outlined' style='vertical-align:middle; font-size:1.1em;'>movie_filter</span> `ffmpeg` **instalado** e no PATH (ver aba "Config. Ambiente")?
            """, unsafe_allow_html=True)
            st.subheader(" ", divider="rainbow")
            st.markdown("##### <span class='material-symbols-outlined'>system_update_alt</span> Download de Modelos Whisper", unsafe_allow_html=True)
            st.caption("Lembre-se: os modelos Whisper são baixados automaticamente no primeiro uso. Uma conexão com a internet será necessária nesse momento.")
            

        with col_steps:
            st.markdown(r"""
            1.  **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>power_settings_new</span> Ative o Ambiente Virtual:**
                Se você criou um (ex: `.venv`), certifique-se de que ele está ativo no seu terminal atual.
                ```bash
                # Exemplo para Linux/macOS:
                source .venv/bin/activate
                # Exemplo para Windows (PowerShell):
                # .\.venv\Scripts\Activate.ps1 
                ```
                
            2.  **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>fact_check</span> Verifique o Servidor Ollama:**
                Confirme que o servidor Ollama está em execução (conforme detalhado na aba "Config. Modelos IA").
            3.  **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>folder_open</span> Navegue até a Pasta do Projeto:**
                No seu terminal, use o comando `cd` para ir até o diretório onde o arquivo `app.py` está localizado.
                ```bash
                cd caminho/para/seu/projeto
                ```
            4.  **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>terminal</span> Execute o Comando Streamlit:**
                Digite o seguinte comando e pressione Enter:
                ```bash
                streamlit run app.py
                ```
                ou
                ```bash
                streamlit run app.py --server.fileWatcherType none
                ```
                 
                
                
                Este comando inicia o servidor web do Streamlit e, na maioria das vezes, abre a aplicação automaticamente no seu navegador padrão.
            """, unsafe_allow_html=True)
        
        st.subheader(" ", divider="rainbow")

        st.success("🎉 **Aplicação Iniciada! O que esperar:** 🎉", icon="✅") 
        st.markdown("""
        - Seu navegador web padrão deverá abrir uma nova aba com a interface do aplicativo.
        - Se não abrir automaticamente, o terminal (onde você executou `streamlit run app.py`) mostrará as URLs para acesso:
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>computer</span> Local URL:** Geralmente `http://localhost:8501`
            - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>wifi</span> Network URL:** Algo como `http://SEU_ENDERECO_IP_LOCAL:8501` (útil para acessar de outros dispositivos na mesma rede).
        - <span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>hourglass_empty</span> **Primeiro Carregamento:** Aguarde alguns instantes para a interface carregar completamente. O primeiro uso de um modelo Whisper ou o carregamento inicial de um modelo Ollama podem levar um pouco mais de tempo.
        """, unsafe_allow_html=True) 
        st.subheader(" ", divider="rainbow")

        st.markdown("#### <span class='material-symbols-outlined'>stop_circle</span> Parando a Aplicação", unsafe_allow_html=True)
        st.markdown("""
        Para interromper o servidor Streamlit e fechar a aplicação:
        - Volte para a janela do terminal onde você executou o comando `streamlit run app.py`.
        - Pressione as teclas `Ctrl` + `C`.
        - O terminal pode pedir uma confirmação para encerrar o job; se sim, confirme (geralmente digitando `y` ou `s`).
        """)
        st.subheader(" ", divider="rainbow")

        st.markdown("#### <span class='material-symbols-outlined'>tips_and_updates</span> Dicas Adicionais ao Executar", unsafe_allow_html=True)
        st.markdown("""
        - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>refresh</span> Recarregar Alterações no Código:** Se você editar os arquivos Python (`app.py`, `doc.py`, etc.) enquanto o Streamlit está rodando, a interface do Streamlit no navegador geralmente mostrará uma opção "Rerun" no canto superior direito, ou pode tentar recarregar automaticamente. Se preferir, salvar o arquivo modificado e atualizar a página do navegador (F5 ou Cmd+R) também funciona.
        - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>important_devices</span> Acesso em Outros Dispositivos:** A "Network URL" exibida no terminal é útil se você quiser testar ou usar a aplicação em um tablet, smartphone ou outro computador que esteja conectado à mesma rede Wi-Fi/LAN.
        - **<span class='material-symbols-outlined' style='font-size:1.1em; vertical-align:middle;'>troubleshoot</span> Observando o Terminal:** Mantenha o terminal onde o Streamlit está rodando visível. Ele exibirá informações úteis, logs de acesso e, mais importante, mensagens de erro detalhadas caso algo não funcione como esperado na aplicação.
        """, unsafe_allow_html=True)

    # --- Aba: Guia de Uso ---
    with tab_usage_guide:
        st.subheader("🧭 Guia de Uso da Interface do Aplicativo") 
        st.markdown("A interface foi projetada para ser intuitiva.  está um detalhamento das principais seções e funcionalidades:") 

        col_usage1, col_usage2 = st.columns(2)

        with col_usage1:
            st.markdown("#### <span class='material-symbols-outlined'>view_sidebar</span> 1. Barra Lateral de Configurações (Sidebar)", unsafe_allow_html=True) 
            with st.expander("Detalhes da Barra Lateral", expanded=False): 
                st.markdown("""
                Localizada à esquerda da tela, a barra lateral contém todas as opções de configuração antes do processamento:
                - **<span class='material-symbols-outlined'>mic</span> Selecione o Modelo Whisper:**
                    - Um menu suspenso permite escolher o tamanho do modelo Whisper a ser usado para a transcrição (ex: `tiny`, `small`, `medium`).
                    - **Impacto:** Modelos menores são mais rápidos mas menos precisos. Modelos maiores são mais precisos mas mais lentos e exigem mais recursos computacionais.
                - **<span class='material-symbols-outlined'>hub</span> Nome do Modelo Ollama:**
                    - Um campo de texto onde você deve inserir o nome exato do modelo LLM que você baixou via Ollama e deseja usar para extrair os pontos-chave (ex: `llama3`, `mistral`, `qwen2:0.5b`).
                    - Este nome deve corresponder a um modelo listado por `ollama list`.
                - **<span class='material-symbols-outlined'>upload_file</span> Escolha um arquivo de áudio:**
                    - Botão para fazer upload de um arquivo de áudio do seu computador.
                    - **Formatos Suportados:** `.wav` e `.mp3`.
                """, unsafe_allow_html=True) # Este já estava correto

        with col_usage2:
            st.markdown("#### <span class='material-symbols-outlined'>web_asset</span> 2. Área Principal de Interação", unsafe_allow_html=True) 
            with st.expander("Detalhes da Área Principal (Após Upload e Processamento)", expanded=False): 
                st.markdown("""
                - **<span class='material-symbols-outlined'>play_circle</span> Player de Áudio:**
                    - Após o upload, um player de áudio aparecerá, permitindo que você ouça o áudio carregado antes ou depois do processamento.
                - **<span class='material-symbols-outlined'>rocket_launch</span> Botão "Processar Áudio":**
                    - Este é o gatilho principal (indicado pelo emoji 🚀 no botão real). Ao clicar nele, o processo de transcrição e extração de pontos-chave é iniciado.
                - **<span class='material-symbols-outlined'>hourglass_top</span> Indicadores de Progresso (Spinners):**
                    - Durante o processamento, spinners aparecerão indicando as etapas em execução.
                    - Estes spinners incluem a funcionalidade `show_time=True`, exibindo o tempo decorrido.
                - **<span class='material-symbols-outlined'>view_column</span> Resultados Exibidos em Colunas:**
                    - **Coluna da Transcrição:** À esquerda, o texto completo transcrito.
                    - **Coluna de Pontos-Chave:** À direita, os pontos-chave identificados.
                - **<span class='material-symbols-outlined'>notifications</span> Notificações (Toasts):**
                    - Mensagens curtas e temporárias para indicar a conclusão de etapas.
                """, unsafe_allow_html=True)  
        
        # Seção "Acesso à Documentação" abaixo das colunas, ocupando a largura total
        st.subheader(" ", divider="rainbow") 
        st.markdown("#### <span class='material-symbols-outlined'>menu_book</span> 3. Acesso à Documentação", unsafe_allow_html=True) 
        st.markdown("""
        - No topo da página principal ou da página de documentação, você encontrará o botão **"<span class='material-symbols-outlined'>visibility</span> Ver Documentação Interativa"** (ou similar, o texto do botão é definido em `app.py`).
        - Clicar neste botão alterna a visualização entre a interface principal do aplicativo e esta página de documentação detalhada.
        """, unsafe_allow_html=True)  
        
        
    # --- Aba: FAQ/Solução de Problemas ---
    with tab_faq:
        st.subheader("❓ Perguntas Frequentes e Solução de Problemas") #
        st.error("#### Encontrou um problema? Veja se estas dicas ajudam!", icon="🛠️") #

        col_faq1, col_faq2 = st.columns(2)

        with col_faq1:
            with st.expander("Problema: A aplicação não inicia ou mostra erro ao executar `streamlit run app.py`"): #
                st.markdown("""
                - **Verifique a instalação do Streamlit:** `pip show streamlit`.
                - **Nome do arquivo:** Confirme que está no diretório correto e que o nome é `app.py`.
                - **Ambiente Virtual:** Garanta que está ativado.
                - **Conflitos de Porta:** Verifique as mensagens no terminal.
                - **Logs do Terminal:** Observe para mensagens de erro detalhadas.
                """) #

            with st.expander("Problema: Transcrição com Whisper está muito lenta"): #
                st.markdown("""
                - **Modelo Grande:** Modelos maiores são inerentemente mais lentos.
                - **Recursos da Máquina:** Máquinas com poucos recursos serão mais lentas.
                - **Primeira Execução:** Download do modelo adiciona tempo.
                - **Solução:** Tente um modelo Whisper menor.
                """) #
            
            with st.expander("Problema: Ollama não responde, erro de comunicação, ou nenhum ponto-chave é extraído"): #
                st.markdown("""
                - **Servidor Ollama Inativo:** Verifique com `ollama list`. Tente `ollama serve`.
                - **Modelo LLM não Baixado:** Use `ollama pull NOME_DO_MODELO`.
                - **Nome do Modelo Incorreto:** Certifique-se de que o nome na interface é exato.
                - **URL/Porta do Ollama:** Padrão é `http://localhost:11434`.
                - **Recursos Insuficientes para o LLM:** Verifique os logs do `ollama serve`.
                """) #

        with col_faq2:
            with st.expander("Problema: FFmpeg não encontrado / Erro na transcrição relacionado a formato de áudio"): #
                st.markdown("""
                - **Causa Principal:** FFmpeg não instalado ou não está no PATH.
                - **Solução:** Siga as instruções de instalação na aba "Config. Ambiente". Reinicie o terminal/PC. Verifique com `ffmpeg -version`.
                """) #

            with st.expander("Problema: Erro ao carregar modelo Whisper / Download falha"): #
                st.markdown("""
                - **Conexão com a Internet:** Necessária para o download inicial.
                - **Espaço em Disco:** Verifique `~/.cache/whisper`.
                - **Firewall/Proxy:** Podem estar bloqueando o download.
                - **Cache Corrompido:** Tente limpar `~/.cache/whisper`.
                """) #
            
            with st.expander("Problema: Qualidade da transcrição não é ideal ou o idioma está incorreto"): #
                st.markdown("""
                - **Qualidade do Áudio:** Ruído, volume baixo, múltiplos falantes afetam a precisão.
                - **Tamanho do Modelo Whisper:** Modelos menores são menos precisos.
                - **Idioma:** App configurado para **language='pt'**. Outros idiomas podem não funcionar bem.
                """) #

        st.info("ℹ️ **Dica Geral:** Sempre verifique os logs (mensagens de texto) no terminal onde você executou `streamlit run app.py` e, se aplicável, no terminal onde `ollama serve` está rodando. Eles frequentemente contêm mensagens de erro detalhadas que podem ajudar a diagnosticar o problema.", icon="🔍") #

