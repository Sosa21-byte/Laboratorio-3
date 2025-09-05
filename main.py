import requests

API_KEY = 'sk-53751d5c6f344a5dbc0571de9f51313e'
API_URL = 'https://api.deepseek.com/v1/chat/completions'

def enviar_mensaje(mensaje, modelo='deepseek-chat'):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': modelo,
        'messages': [{'role': 'user', 'content': mensaje}]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as err:
        return f"Error de la API: {err}"
    except Exception as e:
        return f"Error inesperado: {e}"

def main():
    print("Hola, estaré respondiendo tus dudas sobre materiales programables, robots biohibridos y metaversos programables. Escribe 'salir' para terminar.")
    parametro= enviar_mensaje("Eres un divulgador cientifico y en los proximos prompts deberás responder preguntas sobre materiales programables, robots biohibridos y metaversos programables; de ser posible tus respuestas no deben ser mayores a 150 palabras")
    
    while True:
        mensaje_usuario = input("Tú: ")

        if mensaje_usuario.lower() == 'salir':
            print("Chatbot: ¡Hasta luego!")
            break

        respuesta = enviar_mensaje(mensaje_usuario)
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    main()
