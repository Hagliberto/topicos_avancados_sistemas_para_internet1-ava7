# 🎙️ Transcrição de Áudio com Whisper e Extração de Pontos-Chave com Ollama 🧠

---

## 📖 Visão Geral Detalhada do Projeto

Bem-vindo! Este projeto é uma solução robusta e intuitiva, nascida na disciplina de **Tópicos Avançados em Sistemas para Internet I** do curso de **Tecnologia em Sistemas para Internet**. Nossa missão? Transformar áudio bruto em texto preciso e, em seguida, extrair os **pontos-chave** mais importantes de forma automatizada. 🎯

Queremos oferecer uma ferramenta **open-source** que demonstre o poder da **Inteligência Artificial (IA)** no processamento de linguagem natural e áudio. Tudo isso através de uma interface web interativa (criada com Streamlit ✨) que roda **localmente** na sua máquina, garantindo **privacidade total** e controle sobre seus dados. 🔒

### 🎯 Propósito e Objetivos

Vivemos em um mundo com muito conteúdo falado! O objetivo central é fornecer uma forma **acessível e poderosa** de analisar esse conteúdo. Automatizamos a transcrição e a sumarização para otimizar seu tempo e facilitar o acesso à informação presa em gravações. Não é só converter fala em texto, é **agregar valor** extraindo a essência do conteúdo. A escolha por modelos locais (Whisper + Ollama) reforça nosso compromisso com a sua privacidade.

### 👥 Público-Alvo Principal

Esta ferramenta foi pensada para você, seja qual for sua área:

*   **🎓 Estudantes e Pesquisadores:** Transcreva aulas, palestras, entrevistas. Facilita a revisão, busca e análise de dados de áudio.
*   **💼 Profissionais:** Registre e resuma reuniões, workshops, depoimentos. Otimize seu tempo e retenha informações cruciais.
*   **📢 Criadores de Conteúdo e Jornalistas:** Gere legendas, transcreva entrevistas, crie resumos de podcasts/vídeos. Agilize seu fluxo de trabalho.
*   **💻 Desenvolvedores e Entusiastas de IA:** Use como exemplo prático para explorar Whisper e LLMs (via Ollama) em seus próprios projetos.

### ✨ Principais Benefícios

Usar esta ferramenta traz muitas vantagens:

*   **⏱️ Economia de Tempo:** Chega de transcrição manual demorada! Libere tempo para o que realmente importa.
*   **♿ Acessibilidade:** Torne o conteúdo de áudio acessível a todos, incluindo pessoas com deficiência auditiva, e facilite a pesquisa textual.
*   **📊 Eficiência na Análise:** Identifique rapidamente informações cruciais e temas centrais com a extração de pontos-chave.
*   **🔒 Privacidade e Controle:** Seus dados ficam na sua máquina. Sem envios para nuvens externas.
*   **⚙️ Customização:** Escolha o tamanho do modelo Whisper e o LLM no Ollama que melhor se adaptam às suas necessidades e hardware.
*   **💰 Baixo Custo/Gratuito:** Totalmente baseado em ferramentas open-source. Sem custos de API.

---

## ✅ Funcionalidades Detalhadas

Combinamos várias capacidades para uma experiência completa:

*   **🎙️ Transcrição Precisa:** Faça upload fácil de arquivos `.wav` e `.mp3`. Usamos o poderoso **OpenAI Whisper** para alta acurácia, otimizado para Português (`pt`).
*   **🧠 Extração Inteligente de Pontos-Chave:** O texto transcrito é analisado por um **LLM via Ollama** para identificar e apresentar os tópicos principais de forma concisa. Você escolhe o modelo Ollama local (`llama3`, `mistral`, etc.).
*   **🔧 Configuração Flexível:** Selecione o tamanho do modelo **Whisper** (`tiny` a `large`) para balancear velocidade e precisão. Especifique qual **modelo Ollama** usar.
*   **👀 Interface Clara e Feedback:** Interaja através de uma interface **Streamlit** amigável. Veja indicadores de progresso (spinners ⏳), ouça o áudio carregado (▶️) e receba notificações ( Tostas 🍞) ao concluir.

---

## 🏗️ Arquitetura Simplificada

Entenda como tudo funciona:

1.  **🖥️ Frontend (Interface Streamlit):** Coleta o áudio e configurações, exibe os resultados.
2.  **🔊 Motor de Transcrição (Whisper Local):** Converte fala em texto na sua máquina.
3.  **📝 Motor de Pontos-Chave (Ollama + LLM Local):** Processa o texto para extrair insights.

**Fluxo:** Usuário ➡️ Interface ➡️ Whisper ➡️ Interface ➡️ Ollama ➡️ Interface ➡️ Usuário

---

## 🛠️ Stack Tecnológico Utilizado

Construído com ferramentas open-source incríveis:

*   **🐍 Python:** A linguagem que une tudo.
*   **🖼️ Streamlit:** Para a interface web interativa.
*   **🎤 OpenAI Whisper:** Para transcrição de áudio state-of-the-art (local).
*   **🧠 Ollama:** Para rodar LLMs localmente com facilidade.
*   **🌐 Requests:** Para comunicação entre Streamlit e Ollama.
*   **FFmpeg:** Essencial para processamento de áudio pelo Whisper.

---

## 🧱 Pré-requisitos Essenciais

Antes de começar, garanta que você tem:

1.  **Python (>= 3.8):** Baixe em [python.org](https://www.python.org/). (Marque "Add Python to PATH" no Windows).
2.  **Ollama:** Instalado e rodando. Siga as instruções em [ollama.com](https://ollama.com/).
    *   **Baixe um Modelo LLM:** Ex: `ollama pull llama3` (ou `mistral`, `phi3`, etc.).
    *   **Verifique:** Acesse `http://localhost:11434` ou rode `ollama list`.
3.  **FFmpeg:** Necessário para o Whisper.
    *   **Verifique:** `ffmpeg -version` no terminal.
    *   **Instale:**
        *   **Windows:** Baixe em [gyan.dev](https://www.gyan.dev/ffmpeg/builds/), extraia e adicione a pasta `bin` ao `PATH` do sistema.
        *   **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install ffmpeg`
        *   **macOS (Homebrew):** `brew install ffmpeg`

---

## 🚀 Configuração e Instalação

Vamos preparar o ambiente:

1.  **Obtenha o Código:** Clone o repositório Git ou extraia o arquivo ZIP.
    ```bash
    # Exemplo com Git
    git clone <URL_DO_REPOSITÓRIO>
    cd <NOME_DA_PASTA>
    ```
2.  **Crie e Ative um Ambiente Virtual:** (Altamente recomendado!)
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    ```
    *(Você verá `(venv)` no seu terminal)*
3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Como Executar a Aplicação

Com tudo pronto:

1.  **Verifique o Ollama:** Garanta que o serviço está rodando e o modelo LLM desejado foi baixado (`ollama list`).
2.  **Execute o Script Streamlit:** (Com o ambiente `venv` ativado)
    ```bash
    streamlit run app.py
    ```
3.  **Acesse a Interface:** O Streamlit deve abrir a aplicação no seu navegador. Se não, acesse o endereço fornecido no terminal (geralmente `http://localhost:8501`).

---

## 🖱️ Utilizando a Aplicação

É super simples:

1.  **Configure (Barra Lateral):**
    *   Escolha o **Modelo Whisper** (tamanho).
    *   Digite o **Nome do Modelo Ollama** que você baixou.
2.  **Faça Upload do Áudio:** Clique em "Browse files" ou arraste e solte um arquivo `.wav` ou `.mp3`.
3.  **Processe:** Clique no botão "Processar Áudio".
4.  **Aguarde e Veja os Resultados:** Acompanhe o progresso. A transcrição e os pontos-chave aparecerão na tela!

---

## 👨‍💻 Visão Geral do Código (`app.py`)

O coração da aplicação:

*   **Importações:** `streamlit`, `whisper`, `requests`, `tempfile`, etc.
*   **Configurações:** Constantes (URL Ollama, modelos padrão).
*   **Funções Auxiliares:** `load_whisper_model`, `transcribe_audio`, `get_key_points_from_ollama` (com cache `@st.cache_resource` para otimizar!).
*   **Interface (Streamlit):** Define o layout, widgets e áreas de exibição.
*   **Fluxo Principal:** Gerencia o upload, processamento e exibição dos resultados.

---

## 🚧 Melhorias Futuras (Ideias)

*   Adicionar suporte a processamento de **imagens** (descrições).
*   Implementar **Text-to-Speech** para ouvir os resultados.

---

*Se encontrar problemas, revise os **Pré-requisitos Essenciais** e garanta que tudo está instalado e rodando corretamente! Bom uso!* 👍

