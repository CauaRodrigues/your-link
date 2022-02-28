# Your Link

Encurtador de url CLI com python. Encurta urls através de APIs da Bitly e Cuttly.

![Apresentação Your Link](/.github/your-link.png)

---
## ⚠️ Pré-requisitos

Para usar este encurtador de urls, você precisa ter instalado em sua máquina o [Git](https://git-scm.com/) (para clonar o projeto em sua máquina) e o [Python](https://www.python.org/) (para rodar o projeto e fazer a instalação dos módulos usados). Além disso, você precisa de uma conta na [Bitly](https://bitly.com/) e na [Cuttly](https://cutt.ly/) para ter acesso aos tokens.

<br />

---
## 🎲 Rodando o Projeto

```bash
# Clone este repositório
$ git clone https://github.com/CauaRodrigues/your-link.git

# Acesse a pasta do projeto
$ cd your-link

# Crie um ambiente virtual e ative ele
$ python -m venv env
$ source ./env/bin/activate

# Agora instale os módulos usados
$ pip install -r requirements.txt

# Resgate o seu token no site da Cuttly e da Bitly e execute esse script python.
# Informe as APIs Keys da Cuttly e Bitly corretamente.
$ python3 tokens.py

# Depois desses dois dados informados, um arquivo .env será criado com essas mesmas informações, criando duas variáveis de ambiente e os outros arquivos dentro do diretório terá acesso a elas.
```


