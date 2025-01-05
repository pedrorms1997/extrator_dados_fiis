### README.md

```markdown
# Extrator de Dados de FIIs

Este projeto é uma aplicação web desenvolvida para extrair, exibir e filtrar dados de FIIs diretamente do site [Funds Explorer](https://www.fundsexplorer.com.br/ranking). Ele oferece funcionalidades como filtros dinâmicos, exportação de dados para CSV e XLSX, além de uma interface elegante e responsiva.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do backend.
  - Framework **Flask** para criação de rotas e renderização da aplicação.
  - **Playwright** para automação do navegador e extração de dados.
  - **Pandas** para manipulação e exportação de dados.

- **HTML/CSS/JavaScript**: Interface do usuário.
  - Design responsivo e moderno.
  - Funcionalidades como geração de filtros dinâmicos e exportação de dados com JavaScript.

---

## 📋 Habilidades Trabalhadas no Projeto

- Automação de tarefas web com **Playwright**.
- Desenvolvimento de APIs e aplicações web com **Flask**.
- Manipulação e exportação de dados com **Pandas**.
- Criação de interfaces responsivas com HTML, CSS e JavaScript.
- Uso de conceitos de usabilidade e design para melhorar a experiência do usuário.

---

## 🚀 Configuração do Projeto

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local.

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Navegador Google Chrome ou Chromium instalado (necessário para o Playwright).

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/extrator-fiis.git
cd extrator-fiis
```

### Passo 2: Criar um Ambiente Virtual

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No Windows:
  ```bash
  venv\Scripts\activate
  ```

- No Linux/MacOS:
  ```bash
  source venv/bin/activate
  ```

### Passo 3: Instalar as Dependências

Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar o Playwright

Instale os navegadores necessários para o Playwright:

```bash
playwright install
```

### Passo 5: Rodar o Projeto

Inicie o servidor Flask:

```bash
python app.py
```

Acesse o projeto no navegador:

```
http://127.0.0.1:5000
```

---

## 🗃️ Funcionalidades

- **Atualizar Dados:** Botão para buscar os dados mais recentes dos FIIs.
- **Filtragem Dinâmica:** Filtros para todas as colunas, incluindo intervalos para valores numéricos.
- **Exportação de Dados:** Botões para exportar os dados para formatos CSV e XLSX.
- **Interface Personalizada:** Design responsivo, com foco em usabilidade.

---

## 📧 Contato

Desenvolvido por **Pedro Moraes**. Caso tenha dúvidas ou sugestões, entre em contato:

- **E-mail:** [pedrorms.contato@gmail.com](mailto:pedrorms.contato@gmail.com)
- **Dados extraídos de:** [Funds Explorer](https://www.fundsexplorer.com.br/ranking)

---

## 📝 Licença

Este projeto é de uso livre para estudos e experimentação. Os dados apresentados são propriedade do site [Funds Explorer](https://www.fundsexplorer.com.br/ranking). Respeite os termos de uso do site ao utilizá-los.
```

---

### O que inclui no README:

1. **Objetivo do projeto:** Descrição geral sobre o que a aplicação faz.
2. **Tecnologias utilizadas:** Linguagens, bibliotecas e frameworks mencionados.
3. **Skills desenvolvidas:** Explicação sobre as habilidades trabalhadas.
4. **Passo a passo de instalação:** Instruções detalhadas para configurar o ambiente, instalar dependências e rodar o projeto.
5. **Funcionalidades principais:** Lista com as principais capacidades da aplicação.
6. **Informações de contato:** Seu e-mail e a origem dos dados.