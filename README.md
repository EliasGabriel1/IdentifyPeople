# IdentifyPeople
<div class="markdown prose w-full break-words dark:prose-invert dark">
    <h1>Identificador de pessoas em imagens com Clarifai</h1>
    <p>Este é um pequeno script Python que usa a API do Clarifai para identificar se uma imagem contém uma pessoa ou
        não. Ele redimensiona a imagem para 224x224 pixels e envia para a API do Clarifai para reconhecimento de
        objetos.</p>
    <h2>Requisitos</h2>
    <ul>
        <li>Python 3.6 ou superior</li>
        <li>Pacotes Python: <code>requests</code>, <code>Pillow</code>, <code>clarifai</code></li>
    </ul>
    <h2>Configuração</h2>
    <p>Antes de executar o script, você precisa ter uma chave de acesso para a API do Clarifai. Você pode obter uma
        chave de acesso gratuita em <a href="https://www.clarifai.com/" target="_new">clarifai.com</a>.</p>
    <p>Substitua "sua-chave-de-acesso-aqui" pela sua chave de acesso na linha
        <code>CLARIFAI_KEY = "sua-chave-de-acesso-aqui"</code></p>
    <h2>Uso</h2>
    <p>Para usar a função <code>identificar_pessoa_na_imagem()</code>, basta fornecer a URL da imagem como entrada. A
        função retorna True se a imagem contém uma pessoa e False caso contrário.</p>
</div>

<img src="https://i.ibb.co/DL0z4q2/Captura-de-tela-2023-03-29-133247.png" alt="Captura-de-tela-2023-03-29-133247"
    border="0">
