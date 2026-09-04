# 📚 TechBooks

> Site de recomendações de livros técnicos em português, com foco em tecnologia. Digite uma ferramenta, linguagem ou assunto e receba recomendações ordenadas do **mais fácil ao mais difícil**.

🌐 **[tech-books-00jn.onrender.com](https://tech-books-00jn.onrender.com)**

---

## ✨ Funcionalidades

- 🔍 **Busca inteligente** por ferramenta, linguagem, assunto ou autor
- 📊 **Ordenação por nível** — do Iniciante ao Expert (5 níveis)
- ⚡ **Autocomplete** com sugestões enquanto você digita, navegável pelo teclado
- 🏷️ **Quick tags** para buscas populares com um clique
- 🔗 **Deep link** — compartilhe buscas via URL (`?q=python`)
- 📱 **Responsivo** — funciona bem em celular e desktop
- 🌙 **Dark theme** com design moderno

---

## 📖 Acervo

**55 livros** cobrindo as principais áreas da tecnologia:

| Área | Exemplos de busca |
|------|------------------|
| Linguagens | `Python`, `JavaScript`, `Java`, `C++` |
| Web & Frontend | `React`, `HTML`, `CSS`, `Node.js` |
| Banco de Dados | `SQL`, `PostgreSQL` |
| DevOps & Cloud | `Docker`, `Kubernetes`, `AWS`, `Git` |
| Data Science & IA | `Machine Learning`, `Deep Learning`, `Pandas`, `TensorFlow` |
| Segurança | `Segurança`, `Hacking` |
| Fundamentos | `Algoritmos`, `Estrutura de Dados`, `Redes` |
| Boas Práticas | `Clean Code`, `Arquitetura`, `Design Patterns`, `DevOps` |
| Sistemas | `Linux`, `Shell`, `Bash` |

### Níveis de dificuldade

| Nível | Label | Cor |
|-------|-------|-----|
| 1 | 🟢 Iniciante | Verde |
| 2 | 🔵 Básico | Azul |
| 3 | 🟡 Intermediário | Amarelo |
| 4 | 🟠 Avançado | Laranja |
| 5 | 🔴 Expert | Vermelho |

---

## 🛠️ Tecnologias

- **Backend:** Python 3 · Flask 3.0
- **Frontend:** HTML5 · CSS3 · JavaScript (Vanilla)
- **Deploy:** Render (Free Tier)
- **Servidor:** Gunicorn

---

## 🚀 Rodando localmente

**Pré-requisitos:** Python 3.8+

```bash
# 1. Clone o repositório
git clone https://github.com/monica1602/tech_books.git
cd tech_books

# 2. (Opcional) Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor
python app.py
```

Acesse **http://localhost:5000** no navegador.

---

## 📡 API

A aplicação expõe uma API REST simples:

### `GET /api/search?q={termo}`

Busca livros por termo. Retorna resultados ordenados por nível de dificuldade.

```bash
curl "http://localhost:5000/api/search?q=python"
```

```json
{
  "success": true,
  "query": "python",
  "total": 8,
  "results": [
    {
      "id": 1,
      "title": "Python para Todos: Explorando Dados com Python 3",
      "author": "Charles R. Severance",
      "level": 1,
      "level_label": "Iniciante",
      "description": "...",
      "year": 2016,
      "pages": 242,
      "language": "Português",
      "tags": ["python", "programação", "iniciante", "dados"],
      "buy_link": "https://www.amazon.com.br/..."
    }
  ]
}
```

### `GET /api/suggestions`

Retorna a lista de sugestões para o autocomplete.

### `GET /api/books?level={1-5}`

Lista todos os livros, com filtro opcional por nível.

### `GET /api/stats`

Retorna estatísticas do acervo (total de livros, distribuição por nível, total de tags).

---

## 📁 Estrutura do projeto

```
tech_books/
├── app.py              # Backend Flask — rotas da API e servidor
├── books_data.py       # Banco de dados dos livros + algoritmo de busca
├── requirements.txt    # Dependências Python
├── Procfile            # Comando de inicialização para o Render/Heroku
├── render.yaml         # Configuração de deploy no Render
├── .gitignore
└── static/
    ├── index.html      # Frontend — estrutura e estados de UI
    ├── styles.css      # Estilos — dark theme, responsivo
    └── app.js          # Lógica do frontend — busca, autocomplete, renderização
```

---

## ☁️ Deploy no Render

O projeto já está configurado para deploy automático no Render via `render.yaml`.

Para fazer o seu próprio deploy:

1. Faça fork deste repositório
2. Acesse [render.com](https://render.com) e crie uma conta
3. **New +** → **Web Service** → conecte seu repositório
4. O Render detecta o `render.yaml` automaticamente
5. Clique em **"Create Web Service"**

> **Nota:** no plano gratuito o serviço entra em modo de espera após 15 minutos sem acesso, o que causa um delay de ~50 segundos na primeira requisição.

---

## 🤝 Contribuindo

Quer adicionar um livro ou uma nova categoria? Contribuições são bem-vindas!

1. Faça um fork do projeto
2. Adicione o livro em `books_data.py` seguindo o formato existente
3. Abra um Pull Request

**Formato para adicionar um livro:**

```python
{
    "id": 56,                          # próximo ID disponível
    "title": "Título do Livro",
    "author": "Nome do Autor",
    "level": 2,                        # 1=Iniciante, 2=Básico, 3=Intermediário, 4=Avançado, 5=Expert
    "level_label": "Básico",
    "tags": ["tag1", "tag2", "tag3"],  # palavras-chave para a busca
    "description": "Descrição breve do livro.",
    "isbn": "978-0000000000",
    "year": 2024,
    "language": "Português",
    "pages": 300,
    "buy_link": "https://www.amazon.com.br/s?k=..."
}
```

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
