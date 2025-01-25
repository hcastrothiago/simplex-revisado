## Pré-requisitos

Certifique-se de que os seguintes softwares estão instalados no seu sistema:

1. **Node.js** (versão 16 ou superior)
2. **Python** (versão 3.10 ou superior)
3. Gerenciador de pacotes para Python (pip)
4. Gerenciador de pacotes para Node.js (npm ou yarn)

---

## Passos de Configuração

### 1. Instalar Node.js

Faça o download e instale o Node.js na [página oficial](https://nodejs.org/):

- Escolha a versão LTS (Long Term Support) para maior estabilidade.

Após a instalação, verifique se o Node.js foi instalado corretamente executando:

```bash
node -v
npm -v
```

### 2. Instalar Python

Faça o download e instale o Python na [página oficial](https://www.python.org/downloads/):

- Certifique-se de adicionar o Python ao PATH durante a instalação.

Após a instalação, verifique se o Python foi instalado corretamente executando:

```bash
python --version
pip --version
```

### 3. Clonar o Repositório do Projeto

Clone este repositório em sua máquina local usando:

```bash
git clone https://github.com/hcastrothiago/simplex-revisado.git
cd ./simplex-revisado
```

### 4. Instalar Dependências do Node.js

Na raiz do projeto, instale as dependências do Node.js:

```bash
npm install
```

Ou, se estiver utilizando o Yarn:

```bash
yarn install
```

### 5. Instalar Dependências do Python

Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### 6. Executar o Projeto

Para iniciar o projeto, siga os passos abaixo:

#### Iniciar o servidor Node.js

```bash
npm start
```

Ou, se estiver utilizando o Yarn:

```bash
yarn start
```

#### Executar o script Python

Certifique-se de estar no ambiente virtual e execute:

```bash
py .\api\api.py
```

---

## Utilize o Insominia

Importe a arquivo de configuração em `./docs/Insomnia_2025-01-25.json`

---
## Utilize uma visão intuitiva com front em html

Inicie o servidor web
```
npm run server
```

Acesse o endereço `localhost:3000`

---

**Thiago Castro**