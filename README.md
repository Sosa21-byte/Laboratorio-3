# Laboratorio-3
![OIP](https://github.com/user-attachments/assets/58a82ea3-b2bc-4969-a4c1-b645101e4712)

\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{tcolorbox}
\tcbuselibrary{skins, breakable}

% Estilo para cajas de comandos
\newtcolorbox{commandbox}[1]{
    colback=black!5,
    colframe=black!75,
    fonttitle=\bfseries,
    title=#1,
    breakable,
    enhanced
}

\title{Práctica de Laboratorio 3: Chatbot con DeepSeek y Streamlit}
\author{Tu Nombre}
\date{\today}

\begin{document}

\maketitle

\section{Objetivo}
Desarrollar un chatbot interactivo sobre sistemas digitales usando la API de DeepSeek y desplegarlo en Streamlit.

\section{Requisitos Previos}
\begin{itemize}
    \item Python 3.7+ instalado
    \item Cuenta en GitHub
    \item Cuenta en Streamlit
\end{itemize}

\section{Desarrolla tu propio chatbot con DeepSeek}

\begin{commandbox}{1. Configuración inicial de la API}
\begin{lstlisting}[language=Python]
import requests

# Configuración de la API 
API_KEY = 'sk-53751d5c6f344a5dbc0571de9f51313e'
API_URL = 'https://api.deepseek.com/v1/chat/completions'
\end{lstlisting}
\end{commandbox}

\begin{commandbox}{2. Función para enviar mensajes a la API}
\begin{lstlisting}[language=Python]
def enviar_mensaje(mensaje, modelo='deepseek-chat'):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    \end{lstlisting}
\end{commandbox}

\begin{commandbox}{2. Función para enviar mensajes a la API}
\begin{lstlisting}
    
    data = {
        'model': modelo,
        'messages': 
        [{'role': 'user', 'content': mensaje}]
    }
    
    try:
        response = requests.post
        (API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json
        ()['choices'][0]['message']['content']
    except Exception as e:
        return f'Error: {str(e)}'
\end{lstlisting}
\end{commandbox}

\begin{commandbox}{3. Lógica principal del chatbot}
\begin{lstlisting}[language=Python]
def main():
    print
    ("BienvenidoalchatbotdeDeepSeek
    Escribe'salir'paraterminar.")
    
    while True:
        mensaje_usuario = input("Tu: ")
        
        if mensaje_usuario.lower() == 'salir':
            print("Chatbot: ¡Hasta luego!")
            break
            
        respuesta = enviar_mensaje(mensaje_usuario)
        print(f"Chatbot: {respuesta}")

if __name__ == '__main__':
    main()
\end{lstlisting}
\end{commandbox}



\begin{commandbox}{4. Ejecución del chatbot básico}
\begin{lstlisting}[language=bash]
# Ejecutar el script
python chatbot_basico.py

# Ejemplo de interacción:
# Tu: Hola, ¿qué es un sistema digital?
# Chatbot: Un sistema digital es...
\end{lstlisting}
\end{commandbox}

\begin{commandbox}{5. Comandos para instalar dependencias}
\begin{lstlisting}[language=bash]
# Instalar solo requests para el chatbot básico
pip install requests

# Para congelar dependencias
pip freeze > requirements.txt
\end{lstlisting}
\end{commandbox}

\begin{commandbox}{6. Desplegar en Streamlit}
\begin{enumerate}
    \item Ingresar a \url{https://streamlit.io/}
    \item Conectar cuenta de GitHub
    \item Seleccionar repositorio y archivo \texttt{app.py}
    \item Click en \textbf{Deploy}
\end{enumerate}
\end{commandbox}

\section{Resultados Esperados}
\begin{itemize}
    \item Chatbot funcional sobre sistemas digitales
    \item Código disponible en repositorio público GitHub
    \item Aplicación web desplegada en Streamlit
\end{itemize}

\end{document}
