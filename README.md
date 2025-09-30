# 🤖 Bot de Controle de Finanças | Bot_Financas
<p align="center">
Um assistente financeiro pessoal construído com Flask e Twilio para registro rápido e monitoramento inteligente de despesas via WhatsApp.
</p>

# ✨ Status e Tecnologias
Status	Framework Web	API de Mensageria	Linguagem
Em Desenvolvimento	Flask	Twilio API for WhatsApp	Python

# Exportar para as Planilhas
🛠 Tecnologias Principais
<p align="left">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge">
<img src="https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=twilio&logoColor=white" alt="Twilio Badge">
<img src="https://img.shields.io/badge/Sql-000000?style=for-the-badge&logo=sqlite&logoColor=white" alt="Banco de Dados Badge">
</p>

# 💡 Sobre o Projeto
O Bot_Financas transforma a gestão financeira em uma conversa simples. Desenvolvido com Flask para gerenciar as rotas do webhook e Twilio para a comunicação via WhatsApp, o bot resolve o problema de esquecermos de registrar despesas, permitindo o monitoramento em tempo real.

# 🔑 Principais Funcionalidades (MVP)
Registro Instantâneo: Adiciona despesas e receitas enviando comandos simples.

Sistema de Webhooks: Utiliza o Flask para receber mensagens do Twilio e processá-las.

Categorização Inteligente: Reconhece ou permite definir categorias para cada transação (ex: alimentação, transporte).

Consultas em Tempo Real: Responde a consultas de saldo e extrato na hora.

Persistência de Dados: Armazenamento seguro de todas as transações em SQL.

# 🏗 Arquitetura do Sistema
O projeto adota a arquitetura Model-Service-Controller (MSC). O Flask atua no ponto de entrada (app.py), gerenciando o webhook do Twilio e direcionando o fluxo para os Controllers.

Componente	Pasta	Responsabilidade
Ponto de Entrada	app.py	Inicializa o Flask, carrega variáveis de ambiente e configura a rota de webhook (/whatsapp).
Controller	controllers/	Trata as requisições (mensagens do Twilio/WhatsApp), valida o comando e chama os serviços.
Service	services/	Contém a lógica de negócio, como cálculo de saldo, geração de relatórios e validação de transações.
Model	models/	Define a estrutura dos dados (como Transacao, Usuario) e a interação direta com o Banco de Dados (ORM).

# Exportar para as Planilhas
⚙️ Configuração e Execução (Passo a Passo)
📋 Pré-requisitos
Python 3.10+ | Git

Conta Twilio (com o Sandbox do WhatsApp configurado) | ngrok (ou outro túnel)

# 1. Clonagem e Instalação
Bash

# Clone e entre no diretório
git clone https://github.com/Muhhzx/Bot_Financas.git
cd Bot_Financas

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt
2. Variáveis de Ambiente
Crie o arquivo .env na raiz do projeto.

Ini, TOML

# Conteúdo do arquivo .env
# Credenciais do Twilio
TWILIO_ACCOUNT_SID=[SEU SID DA CONTA TWILIO]
TWILIO_AUTH_TOKEN=[SEU TOKEN DE AUTENTICACAO TWILIO]

# Banco de Dados
DB_CONNECTION_STRING=[SUA STRING DE CONEXAO DO BD]

# Chave secreta do Flask para segurança
FLASK_SECRET_KEY='[UMA CHAVE SECRETA ALEATORIA E COMPLEXA]'
3. Execução Local e Configuração do Webhook
Inicie o Servidor Flask: python app.py

Exponha o Flask com ngrok: ngrok http 5000

Configure o Twilio: Defina o webhook na Twilio para [URL_DO_NGROK]/whatsapp.

💬 Guia Rápido de Comandos
Comando	Formato	Descrição	Exemplo de Envio
Despesa	gastei <valor> <categoria>	Registra um gasto.	gastei 125.50 Mercado
Receita	ganhei <valor> <origem>	Registra uma entrada de dinheiro.	ganhei 4000 Salário
Saldo	meu saldo	Retorna o valor atual do seu saldo.	meu saldo
Extrato	extrato <período>	Gera um resumo de gastos e receitas.	extrato semanal

📧 Contato.  
Nome: Murilo Gomes Sardinha

GitHub: @Muhhzx

Email: murilogomes.dev@gmail.com
