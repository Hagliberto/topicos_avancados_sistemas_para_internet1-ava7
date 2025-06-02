# Transcrição de Áudio com Whisper e Extração de Pontos-Chave com Ollama

Este projeto implementa um pipeline que:
1. Recebe um arquivo de áudio.
2. Realiza a transcrição do áudio utilizando o modelo Whisper da OpenAI.
3. Utiliza uma instância local do Ollama para gerar um resumo destacando os pontos-chave do texto transcrito.

A interface do usuário é construída com Streamlit, facilitando o upload do áudio e a visualização dos resultados.

## Funcionalidades Principais

* Upload de arquivos de áudio nos formatos `.wav` ou `.mp3`.
* Transcrição de áudio para texto utilizando diferentes tamanhos do modelo Whisper (selecionável pelo usuário).
* Extração de pontos-chave do texto transcrito através de um modelo de linguagem grande (LLM) configurado no Ollama (selecionável pelo usuário).
* Interface web amigável e intuitiva.

## Pré-requisitos Essenciais

Antes de começar, garanta que você tem os seguintes softwares instalados e configurados no seu sistema:

1.  **Python:** Versão 3.8 ou superior. Você pode baixar o Python em [python.org](https://www.python.org/).
    * Durante a instalação do Python no Windows, marque a opção "Add Python to PATH".
2.  **Ollama:** É necessário ter o Ollama instalado e em execução.
    * **Instalação do Ollama:** Siga as instruções em [ollama.com](https://ollama.com/). O Ollama permite rodar modelos de linguagem grandes localmente.
    * **Download de um Modelo LLM para o Ollama:** Você precisará de um modelo para que o Ollama realize a extração dos pontos-chave. `llama3` é uma boa opção. Abra seu terminal (Prompt de Comando, PowerShell, ou Terminal do Linux/macOS) e execute:
        ```bash
        ollama pull llama3
        ```
        Você pode substituir `llama3` por outro modelo de sua preferência (ex: `mistral`, `phi3`), mas lembre-se de ajustar o nome do modelo na interface da aplicação se usar um diferente do padrão (`llama3`).
    * **Verifique se o Ollama está rodando:** Após a instalação, o Ollama geralmente roda como um serviço em segundo plano. Você pode testar se ele está respondendo abrindo `http://localhost:11434` no seu navegador (deve aparecer "Ollama is running") ou rodando `ollama list` no terminal.
3.  **ffmpeg (para Whisper):** O Whisper utiliza o `ffmpeg` para processar diversos formatos de áudio.
    * **Verificação:** Abra um novo terminal e digite `ffmpeg -version`. Se informações da versão aparecerem, ele está instalado e no PATH.
    * **Instalação (Windows):**
        1.  Baixe o `ffmpeg` em [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) (pegue uma "release build").
        2.  Extraia o arquivo para uma pasta, por exemplo, `C:\ffmpeg`.
        3.  Adicione o caminho da subpasta `bin` (ex: `C:\ffmpeg\bin`) à variável de ambiente `PATH` do seu sistema.
        4.  Reinicie o terminal/IDE para que a alteração no `PATH` tenha efeito.
    * **Instalação (Linux - ex: Ubuntu/Debian):**
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
    * **Instalação (macOS com Homebrew):**
        ```bash
        brew install ffmpeg
        ```

## Configuração e Instalação do Projeto

Siga os passos abaixo para configurar o ambiente e instalar as dependências do projeto:

1.  **Clone o Repositório (Opcional):**
    Se você recebeu o projeto como um arquivo ZIP, extraia-o. Se for de um repositório Git:
    ```bash
    git clone <link-do-seu-repositório>
    cd <nome-da-pasta-do-repositório>
    ```

2.  **Crie e Ative um Ambiente Virtual (Altamente Recomendado):**
    Ambientes virtuais isolam as dependências do projeto, evitando conflitos com outros projetos Python.
    * No terminal, navegue até a pasta raiz do projeto e execute:
        ```bash
        python -m venv venv
        ```
    * Ative o ambiente virtual:
        * **Windows (Prompt de Comando/PowerShell):**
            ```bash
            .\venv\Scripts\activate
            ```
        * **Linux/macOS (bash/zsh):**
            ```bash
            source venv/bin/activate
            ```
        Após a ativação, você verá `(venv)` no início do prompt do seu terminal.

3.  **Instale as Dependências Python:**
    Com o ambiente virtual ativado, instale as bibliotecas listadas no arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    O arquivo `requirements.txt` deve conter[cite: 1]:
    ```
    streamlit
    openai-whisper
    requests
    ```

## Como Executar a Aplicação

Com tudo configurado e as dependências instaladas, siga os passos:

1.  **Garanta que o Ollama está em Execução:**
    * Verifique se o serviço Ollama foi iniciado.
    * Confirme que o modelo que você pretende usar (ex: `llama3`) foi baixado (`ollama list`).

2.  **Execute o Script Streamlit:**
    * Certifique-se de que seu ambiente virtual `(venv)` está ativado.
    * Navegue pelo terminal até a pasta raiz do projeto (onde o arquivo `app.py` está localizado).
    * Execute o comando:
        ```bash
        streamlit run app.py
        ```

3.  **Acesse a Aplicação:**
    * Após executar o comando acima, o Streamlit geralmente abrirá a aplicação automaticamente no seu navegador web padrão.
    * Se não abrir, o terminal mostrará um endereço local (URL), tipicamente `http://localhost:8501`. Copie e cole este endereço no seu navegador.

## Utilizando a Aplicação

1.  **Configurações (Barra Lateral):**
    * **Selecione o Modelo Whisper:** Escolha o tamanho do modelo Whisper. Modelos menores (`tiny`, `base`) são mais rápidos, mas menos precisos. Modelos maiores (`small`, `medium`, `large`) são mais precisos, mas exigem mais processamento e tempo. O padrão é `base`.
    * **Nome do Modelo Ollama:** Insira o nome do modelo Ollama que você baixou e deseja usar para a extração de pontos-chave. O padrão é `llama3`.

2.  **Upload do Áudio:**
    * Clique em "Browse files" ou arraste e solte um arquivo de áudio (`.wav` ou `.mp3`) na área indicada.

3.  **Processamento:**
    * Clique no botão "Processar Áudio".
    * Aguarde o processo de transcrição e extração de pontos-chave. O tempo pode variar dependendo do tamanho do áudio e dos modelos selecionados.

4.  **Resultados:**
    * A transcrição completa do áudio será exibida.
    * Os pontos-chave extraídos pelo Ollama serão mostrados logo abaixo ou ao lado.

## Visão Geral do Código (`app.py`)

* **Importações:** Bibliotecas necessárias como `streamlit`, `whisper`, `requests`, etc.
* **Configuração:** Constantes para a URL da API do Ollama e modelos padrão.
* **Funções Auxiliares:**
    * `load_whisper_model()`: Carrega o modelo Whisper selecionado e o armazena em cache para melhor desempenho.
    * `transcribe_audio()`: Responsável pela transcrição do arquivo de áudio.
    * `get_key_points_from_ollama()`: Envia o texto transcrito para a API do Ollama e obtém os pontos-chave.
* **Interface do Usuário (Streamlit):** Define o layout da página, os seletores de modelo, o uploader de arquivos e as áreas de exibição dos resultados.
* **Fluxo Principal:** Gerencia o upload do arquivo, o acionamento do processamento e a orquestração das chamadas às funções auxiliares.
* O script utiliza `tempfile` para manipular o arquivo de áudio enviado de forma segura e temporária.

## Melhorias Futuras (Não Implementadas)

* Opção para receber arquivos de imagem e gerar descrições.
* Funcionalidade para retornar o conteúdo transcrito ou resumido em formato de áudio (Text-to-Speech).

Se encontrar problemas, verifique se todos os pré-requisitos foram atendidos e se os serviços (como o Ollama) estão realmente em execução.