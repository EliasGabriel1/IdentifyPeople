from io import BytesIO
import requests
from PIL import Image
from clarifai.rest import ClarifaiApp

# Chave de acesso da API do Clarifai
CLARIFAI_KEY = "sua-chave-de-acesso-aqui"

def baixar_e_redimensionar_imagem(url):
    """Baixa e redimensiona a imagem da URL."""
    response = requests.get(url)
    imagem = Image.open(BytesIO(response.content))
    imagem_redimensionada = imagem.resize((224, 224))
    return imagem_redimensionada

def identificar_pessoa_na_imagem(url_imagem):
    """Identifica se a imagem contém uma pessoa usando a API do Clarifai."""
    imagem = baixar_e_redimensionar_imagem(url_imagem)

    # Prepara a imagem para ser enviada para a API do Clarifai
    buffer = BytesIO()
    imagem.save(buffer, format="JPEG")
    byte_imagem = buffer.getvalue()

    # Inicializa a aplicação do Clarifai com a chave de acesso
    app = ClarifaiApp(api_key=CLARIFAI_KEY)

    # Envia a imagem para a API do Clarifai para reconhecimento de objetos
    response = app.models.predict(
        model_id="aaa03c23b3724a16a56b629203edc62c",
        inputs=[{"data": {"image": {"base64": byte_imagem.decode("utf-8")}}}]
    )

    # Verifica se a imagem contém a tag "person" retornada pela API do Clarifai
    return any(concept["name"] == "person" and concept["value"] > 0.5
               for concept in response["outputs"][0]["data"]["concepts"])

# Exemplo de uso da função
url = "https://i.imgur.com/9jg9TGO.jpg"
if identificar_pessoa_na_imagem(url):
    print("A imagem contém uma pessoa.")
else:
    print("A imagem não contém uma pessoa.")