# Banco de dados de livros técnicos
# Nível de dificuldade: 1 = Iniciante, 2 = Básico, 3 = Intermediário, 4 = Avançado, 5 = Expert

BOOKS = [

    # ─── PYTHON ───────────────────────────────────────────────────────────────
    {
        "id": 1,
        "title": "Python para Todos: Explorando Dados com Python 3",
        "author": "Charles R. Severance",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["python", "programação", "iniciante", "dados"],
        "description": "Introdução gentil ao Python voltada para quem nunca programou. Cobre variáveis, loops, funções e manipulação de arquivos com exemplos práticos.",
        "isbn": "978-1530051120",
        "year": 2016,
        "language": "Português",
        "pages": 242,
        "buy_link": "https://www.amazon.com.br/s?k=Python+para+Todos+Severance"
    },
    {
        "id": 2,
        "title": "Automatize Tarefas Maçantes com Python",
        "author": "Al Sweigart",
        "level": 2,
        "level_label": "Básico",
        "tags": ["python", "automação", "scripts", "programação"],
        "description": "Aprenda a automatizar tarefas do dia a dia com Python: manipulação de arquivos, PDFs, planilhas, e-mails e web scraping.",
        "isbn": "978-8575226407",
        "year": 2019,
        "language": "Português",
        "pages": 504,
        "buy_link": "https://www.amazon.com.br/s?k=Automatize+Tarefas+Ma%C3%A7antes+Python"
    },
    {
        "id": 3,
        "title": "Python Fluente",
        "author": "Luciano Ramalho",
        "level": 4,
        "level_label": "Avançado",
        "tags": ["python", "programação", "avançado", "idioms", "boas práticas"],
        "description": "Escrito por um brasileiro, é considerado o livro definitivo para programadores Python que querem dominar o idioma com profundidade e elegância.",
        "isbn": "978-8575225561",
        "year": 2023,
        "language": "Português",
        "pages": 838,
        "buy_link": "https://www.amazon.com.br/s?k=Python+Fluente+Luciano+Ramalho"
    },
    {
        "id": 4,
        "title": "Use a Cabeça! Python",
        "author": "Paul Barry",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["python", "programação", "iniciante"],
        "description": "Abordagem visual e divertida para aprender Python do zero. Cheio de exercícios, puzzles e projetos práticos para fixar o conteúdo.",
        "isbn": "978-8550804606",
        "year": 2018,
        "language": "Português",
        "pages": 622,
        "buy_link": "https://www.amazon.com.br/s?k=Use+a+Cabe%C3%A7a+Python"
    },
    {
        "id": 5,
        "title": "Programação Python: Referência Completa",
        "author": "Mark Lutz",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["python", "programação", "referência", "oop"],
        "description": "Referência abrangente da linguagem Python cobrindo OOP, módulos, exceções, ferramentas avançadas e integração com outras tecnologias.",
        "isbn": "978-8577807925",
        "year": 2010,
        "language": "Português",
        "pages": 1594,
        "buy_link": "https://www.amazon.com.br/s?k=Programa%C3%A7%C3%A3o+Python+Mark+Lutz"
    },

    # ─── JAVASCRIPT ───────────────────────────────────────────────────────────
    {
        "id": 6,
        "title": "JavaScript: O Guia Definitivo",
        "author": "David Flanagan",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["javascript", "js", "web", "frontend", "programação"],
        "description": "A referência mais completa sobre JavaScript, cobrindo a linguagem a fundo: ES6+, APIs do browser, Node.js e muito mais.",
        "isbn": "978-8575227138",
        "year": 2021,
        "language": "Português",
        "pages": 706,
        "buy_link": "https://www.amazon.com.br/s?k=JavaScript+Guia+Definitivo+Flanagan"
    },
    {
        "id": 7,
        "title": "JavaScript e JQuery: Desenvolvimento de Interfaces Web Interativas",
        "author": "Jon Duckett",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["javascript", "jquery", "web", "frontend", "html", "css"],
        "description": "Livro com design visual incrível que ensina JavaScript e jQuery de forma acessível. Ótimo ponto de entrada para o desenvolvimento web.",
        "isbn": "978-8576089520",
        "year": 2016,
        "language": "Português",
        "pages": 640,
        "buy_link": "https://www.amazon.com.br/s?k=JavaScript+jQuery+Jon+Duckett"
    },
    {
        "id": 8,
        "title": "Use a Cabeça! JavaScript",
        "author": "Eric Freeman",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["javascript", "js", "web", "frontend", "iniciante"],
        "description": "Introdução prática ao JavaScript com a metodologia Head First, repleto de exercícios e desafios para aprender programando.",
        "isbn": "978-8576089247",
        "year": 2015,
        "language": "Português",
        "pages": 660,
        "buy_link": "https://www.amazon.com.br/s?k=Use+a+Cabe%C3%A7a+JavaScript"
    },
    {
        "id": 9,
        "title": "Segredos do JavaScript Ninja",
        "author": "John Resig, Bear Bibeault",
        "level": 4,
        "level_label": "Avançado",
        "tags": ["javascript", "js", "avançado", "closures", "prototype"],
        "description": "Mergulha fundo nos mecanismos internos do JavaScript: closures, protótipos, generators, promises e técnicas avançadas usadas por profissionais.",
        "isbn": "978-8575225370",
        "year": 2017,
        "language": "Português",
        "pages": 464,
        "buy_link": "https://www.amazon.com.br/s?k=Segredos+JavaScript+Ninja"
    },
    {
        "id": 10,
        "title": "Princípios de Orientação a Objetos em JavaScript",
        "author": "Nicholas C. Zakas",
        "level": 2,
        "level_label": "Básico",
        "tags": ["javascript", "oop", "orientação a objetos", "js"],
        "description": "Explica como a orientação a objetos funciona em JavaScript de forma prática e clara, cobrindo herança, protótipos e padrões de design.",
        "isbn": "978-8575224342",
        "year": 2014,
        "language": "Português",
        "pages": 120,
        "buy_link": "https://www.amazon.com.br/s?k=Princ%C3%ADpios+Orienta%C3%A7%C3%A3o+Objetos+JavaScript"
    },

    # ─── REACT ────────────────────────────────────────────────────────────────
    {
        "id": 11,
        "title": "React: Aprenda Praticando",
        "author": "Flávio Copes",
        "level": 2,
        "level_label": "Básico",
        "tags": ["react", "javascript", "frontend", "web", "spa"],
        "description": "Guia prático e objetivo para aprender React, cobrindo componentes, hooks, state management e integração com APIs.",
        "isbn": "978-8575228296",
        "year": 2020,
        "language": "Português",
        "pages": 312,
        "buy_link": "https://www.amazon.com.br/s?k=React+Aprenda+Praticando"
    },
    {
        "id": 12,
        "title": "Desenvolvimento Web com React",
        "author": "Stoyan Stefanov",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["react", "javascript", "frontend", "web", "componentes"],
        "description": "Cobre React em profundidade: ciclo de vida, hooks avançados, Redux, testes e boas práticas para aplicações de produção.",
        "isbn": "978-8575226964",
        "year": 2021,
        "language": "Português",
        "pages": 416,
        "buy_link": "https://www.amazon.com.br/s?k=Desenvolvimento+Web+React+Stefanov"
    },

    # ─── NODE.JS ───────────────────────────────────────────────────────────────
    {
        "id": 13,
        "title": "Node.js: A Bíblia",
        "author": "Adam Stefanov",
        "level": 2,
        "level_label": "Básico",
        "tags": ["node", "nodejs", "javascript", "backend", "api", "servidor"],
        "description": "Guia completo para construir aplicações backend com Node.js, cobrindo módulos, Express, bancos de dados e deploy.",
        "isbn": "978-8550805320",
        "year": 2019,
        "language": "Português",
        "pages": 598,
        "buy_link": "https://www.amazon.com.br/s?k=Node.js+B%C3%ADblia"
    },
    {
        "id": 14,
        "title": "Node.js em Ação",
        "author": "Mike Cantelon, Marc Harter",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["node", "nodejs", "javascript", "backend", "express", "servidor"],
        "description": "Ensina Node.js com foco em aplicações web reais, cobrindo Express, WebSockets, testes e performance.",
        "isbn": "978-8575225714",
        "year": 2016,
        "language": "Português",
        "pages": 456,
        "buy_link": "https://www.amazon.com.br/s?k=Node.js+em+A%C3%A7%C3%A3o"
    },

    # ─── BANCO DE DADOS / SQL ─────────────────────────────────────────────────
    {
        "id": 15,
        "title": "Use a Cabeça! SQL",
        "author": "Lynn Beighley",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["sql", "banco de dados", "mysql", "database", "dados"],
        "description": "Aprenda SQL de forma visual e envolvente com a metodologia Head First. Cobre SELECT, JOIN, subqueries e design de banco de dados.",
        "isbn": "978-8576081746",
        "year": 2008,
        "language": "Português",
        "pages": 608,
        "buy_link": "https://www.amazon.com.br/s?k=Use+a+Cabe%C3%A7a+SQL"
    },
    {
        "id": 16,
        "title": "Sistemas de Banco de Dados",
        "author": "Ramez Elmasri, Shamkant Navathe",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["banco de dados", "sql", "database", "modelagem", "er"],
        "description": "O livro texto clássico para estudar banco de dados: modelagem ER, SQL avançado, normalização, transações e bancos distribuídos.",
        "isbn": "978-8579360855",
        "year": 2019,
        "language": "Português",
        "pages": 1080,
        "buy_link": "https://www.amazon.com.br/s?k=Sistemas+Banco+Dados+Elmasri"
    },
    {
        "id": 17,
        "title": "SQL: Guia Prático",
        "author": "Robert Vieira",
        "level": 2,
        "level_label": "Básico",
        "tags": ["sql", "banco de dados", "database", "consultas"],
        "description": "Guia prático e direto ao ponto para aprender SQL com exemplos reais. Ótimo para quem quer desenvolver habilidades de consulta rapidamente.",
        "isbn": "978-8550800738",
        "year": 2016,
        "language": "Português",
        "pages": 486,
        "buy_link": "https://www.amazon.com.br/s?k=SQL+Guia+Pr%C3%A1tico+Vieira"
    },
    {
        "id": 18,
        "title": "PostgreSQL: Up and Running",
        "author": "Regina Obe, Leo Hsu",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["postgresql", "postgres", "sql", "banco de dados", "database"],
        "description": "Guia para PostgreSQL cobrindo instalação, tipos de dados, funções avançadas, PostGIS e administração do banco.",
        "isbn": "978-1491963418",
        "year": 2017,
        "language": "Português",
        "pages": 334,
        "buy_link": "https://www.amazon.com.br/s?k=PostgreSQL+Up+Running"
    },

    # ─── GIT ──────────────────────────────────────────────────────────────────
    {
        "id": 19,
        "title": "Controlando Versões com Git e GitHub",
        "author": "Alexandre Aquiles, Rodrigo Ferreira",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["git", "github", "controle de versão", "versionamento"],
        "description": "Guia em português para aprender Git e GitHub do zero: commits, branches, merges, pull requests e fluxos de trabalho em equipe.",
        "isbn": "978-8594188939",
        "year": 2015,
        "language": "Português",
        "pages": 200,
        "buy_link": "https://www.amazon.com.br/s?k=Controlando+Vers%C3%B5es+Git+GitHub"
    },
    {
        "id": 20,
        "title": "Git Profissional",
        "author": "Scott Chacon, Ben Straub",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["git", "github", "controle de versão", "devops"],
        "description": "O livro oficial do Git, disponível gratuitamente online. Cobre desde o básico até workflows avançados, internos do Git e administração.",
        "isbn": "978-1484200773",
        "year": 2014,
        "language": "Português",
        "pages": 574,
        "buy_link": "https://www.amazon.com.br/s?k=Pro+Git+Scott+Chacon"
    },

    # ─── DATA SCIENCE / MACHINE LEARNING ─────────────────────────────────────
    {
        "id": 21,
        "title": "Python para Análise de Dados",
        "author": "Wes McKinney",
        "level": 2,
        "level_label": "Básico",
        "tags": ["python", "data science", "pandas", "numpy", "análise de dados", "dados"],
        "description": "Escrito pelo criador do Pandas, ensina análise de dados com Python usando NumPy, Pandas, Matplotlib e IPython.",
        "isbn": "978-8575226476",
        "year": 2019,
        "language": "Português",
        "pages": 548,
        "buy_link": "https://www.amazon.com.br/s?k=Python+An%C3%A1lise+Dados+McKinney"
    },
    {
        "id": 22,
        "title": "Mãos à Obra: Aprendizado de Máquina com Scikit-Learn, Keras e TensorFlow",
        "author": "Aurélien Géron",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["machine learning", "ia", "inteligência artificial", "scikit-learn", "tensorflow", "keras", "deep learning"],
        "description": "O melhor livro prático sobre Machine Learning e Deep Learning. Cobre desde regressão até redes neurais convolucionais e NLP.",
        "isbn": "978-8550815435",
        "year": 2021,
        "language": "Português",
        "pages": 856,
        "buy_link": "https://www.amazon.com.br/s?k=M%C3%A3os+%C3%A0+Obra+Aprendizado+M%C3%A1quina+G%C3%A9ron"
    },
    {
        "id": 23,
        "title": "Data Science do Zero",
        "author": "Joel Grus",
        "level": 2,
        "level_label": "Básico",
        "tags": ["data science", "python", "machine learning", "estatística", "dados"],
        "description": "Introduz os fundamentos de data science implementando algoritmos do zero em Python. Ótimo para entender como as coisas funcionam por dentro.",
        "isbn": "978-8550814773",
        "year": 2021,
        "language": "Português",
        "pages": 436,
        "buy_link": "https://www.amazon.com.br/s?k=Data+Science+do+Zero+Joel+Grus"
    },
    {
        "id": 24,
        "title": "Deep Learning",
        "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
        "level": 5,
        "level_label": "Expert",
        "tags": ["deep learning", "redes neurais", "ia", "inteligência artificial", "machine learning"],
        "description": "O livro texto definitivo de Deep Learning, escrito pelos maiores pesquisadores da área. Cobertura matemática e teórica completa.",
        "isbn": "978-8575226704",
        "year": 2018,
        "language": "Português",
        "pages": 786,
        "buy_link": "https://www.amazon.com.br/s?k=Deep+Learning+Goodfellow+portugu%C3%AAs"
    },
    {
        "id": 25,
        "title": "Estatística Prática para Cientistas de Dados",
        "author": "Peter Bruce, Andrew Bruce",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["estatística", "data science", "análise de dados", "probabilidade", "dados"],
        "description": "Cobre os conceitos estatísticos essenciais para ciência de dados com foco prático: distribuições, regressão, reamostragem e classificação.",
        "isbn": "978-8550814780",
        "year": 2020,
        "language": "Português",
        "pages": 348,
        "buy_link": "https://www.amazon.com.br/s?k=Estat%C3%ADstica+Pr%C3%A1tica+Cientistas+Dados"
    },

    # ─── INTELIGÊNCIA ARTIFICIAL / LLM ────────────────────────────────────────
    {
        "id": 26,
        "title": "Inteligência Artificial: Uma Abordagem Moderna",
        "author": "Stuart Russell, Peter Norvig",
        "level": 4,
        "level_label": "Avançado",
        "tags": ["inteligência artificial", "ia", "algoritmos", "busca", "lógica", "machine learning"],
        "description": "A bíblia da Inteligência Artificial. Cobre todos os fundamentos: busca, planejamento, lógica, aprendizado de máquina e percepção.",
        "isbn": "978-8535237016",
        "year": 2013,
        "language": "Português",
        "pages": 1056,
        "buy_link": "https://www.amazon.com.br/s?k=Intelig%C3%AAncia+Artificial+Russell+Norvig"
    },

    # ─── DOCKER / KUBERNETES ──────────────────────────────────────────────────
    {
        "id": 27,
        "title": "Docker para Desenvolvedores",
        "author": "Rafael Gomes",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["docker", "containers", "devops", "infraestrutura"],
        "description": "Guia em português para aprender Docker do zero: imagens, containers, volumes, redes e Docker Compose para desenvolvimento local.",
        "isbn": "978-8594188946",
        "year": 2017,
        "language": "Português",
        "pages": 280,
        "buy_link": "https://www.amazon.com.br/s?k=Docker+para+Desenvolvedores"
    },
    {
        "id": 28,
        "title": "Docker na Prática",
        "author": "Elton Stoneman",
        "level": 2,
        "level_label": "Básico",
        "tags": ["docker", "containers", "devops", "microserviços"],
        "description": "Ensina Docker com foco em casos de uso reais: containerização de aplicações, Docker Compose, redes e volumes em profundidade.",
        "isbn": "978-8550807812",
        "year": 2020,
        "language": "Português",
        "pages": 396,
        "buy_link": "https://www.amazon.com.br/s?k=Docker+na+Pr%C3%A1tica"
    },
    {
        "id": 29,
        "title": "Kubernetes na Prática",
        "author": "John Arundel, Justin Domingus",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["kubernetes", "k8s", "containers", "devops", "cloud", "orquestração"],
        "description": "Guia prático para Kubernetes cobrindo pods, deployments, services, Helm, RBAC, monitoramento e boas práticas de produção.",
        "isbn": "978-8550816234",
        "year": 2020,
        "language": "Português",
        "pages": 326,
        "buy_link": "https://www.amazon.com.br/s?k=Kubernetes+na+Pr%C3%A1tica"
    },

    # ─── LINUX / SISTEMAS OPERACIONAIS ────────────────────────────────────────
    {
        "id": 30,
        "title": "Linux: A Bíblia",
        "author": "Christopher Negus",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["linux", "unix", "shell", "terminal", "sistemas operacionais", "administração"],
        "description": "O guia mais completo sobre Linux para iniciantes e administradores. Cobre instalação, shell, comandos, redes, segurança e servidores.",
        "isbn": "978-8576082231",
        "year": 2010,
        "language": "Português",
        "pages": 1072,
        "buy_link": "https://www.amazon.com.br/s?k=Linux+B%C3%ADblia+Negus"
    },
    {
        "id": 31,
        "title": "O Livro do Shell",
        "author": "Arnold Robbins, Nelson Beebe",
        "level": 2,
        "level_label": "Básico",
        "tags": ["shell", "bash", "linux", "unix", "scripts", "terminal", "linha de comando"],
        "description": "Referência completa sobre shell scripting, cobrindo Bash, sed, awk e ferramentas Unix para automação de tarefas.",
        "isbn": "978-8575222850",
        "year": 2006,
        "language": "Português",
        "pages": 598,
        "buy_link": "https://www.amazon.com.br/s?k=Livro+Shell+Robbins"
    },

    # ─── ENGENHARIA DE SOFTWARE / ARQUITETURA ─────────────────────────────────
    {
        "id": 32,
        "title": "Código Limpo: Habilidades Práticas do Agile Software",
        "author": "Robert C. Martin",
        "level": 2,
        "level_label": "Básico",
        "tags": ["clean code", "boas práticas", "refatoração", "engenharia de software", "código"],
        "description": "O livro fundamental sobre escrita de código de qualidade: nomenclatura, funções, comentários, testes e refatoração com exemplos em Java.",
        "isbn": "978-8576082675",
        "year": 2009,
        "language": "Português",
        "pages": 462,
        "buy_link": "https://www.amazon.com.br/s?k=C%C3%B3digo+Limpo+Robert+Martin"
    },
    {
        "id": 33,
        "title": "Refatoração: Aperfeiçoando o Design de Código Existente",
        "author": "Martin Fowler",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["refatoração", "boas práticas", "design", "engenharia de software", "padrões"],
        "description": "O clássico sobre refatoração de código: catálogo de técnicas para melhorar código legado sem alterar comportamento externo.",
        "isbn": "978-8575227916",
        "year": 2020,
        "language": "Português",
        "pages": 460,
        "buy_link": "https://www.amazon.com.br/s?k=Refatora%C3%A7%C3%A3o+Martin+Fowler"
    },
    {
        "id": 34,
        "title": "Padrões de Projetos: Soluções Reutilizáveis de Software Orientado a Objetos",
        "author": "Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        "level": 4,
        "level_label": "Avançado",
        "tags": ["design patterns", "padrões de projeto", "oop", "arquitetura", "engenharia de software"],
        "description": "O livro do 'Gang of Four', clássico absoluto que define os 23 padrões de design fundamentais usados no desenvolvimento de software.",
        "isbn": "978-8573076103",
        "year": 2000,
        "language": "Português",
        "pages": 395,
        "buy_link": "https://www.amazon.com.br/s?k=Padr%C3%B5es+de+Projetos+Gang+of+Four"
    },
    {
        "id": 35,
        "title": "Arquitetura Limpa: O Guia do Artesão para Estrutura e Design de Software",
        "author": "Robert C. Martin",
        "level": 4,
        "level_label": "Avançado",
        "tags": ["arquitetura", "clean architecture", "design", "engenharia de software", "solid"],
        "description": "Uncle Bob apresenta princípios de arquitetura de software: SOLID, componentes, limites e como criar sistemas sustentáveis a longo prazo.",
        "isbn": "978-8550804606",
        "year": 2019,
        "language": "Português",
        "pages": 432,
        "buy_link": "https://www.amazon.com.br/s?k=Arquitetura+Limpa+Robert+Martin"
    },
    {
        "id": 36,
        "title": "O Mítico Homem-Mês",
        "author": "Frederick P. Brooks Jr.",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["gerenciamento", "engenharia de software", "projetos", "times", "gestão"],
        "description": "Ensaios clássicos sobre engenharia de software e gerenciamento de projetos. Conceitos atemporais como a Lei de Brooks ainda são citados hoje.",
        "isbn": "978-8550802046",
        "year": 2018,
        "language": "Português",
        "pages": 304,
        "buy_link": "https://www.amazon.com.br/s?k=M%C3%ADtico+Homem-M%C3%AAs+Brooks"
    },

    # ─── SEGURANÇA / HACKING ÉTICO ────────────────────────────────────────────
    {
        "id": 37,
        "title": "Fundamentos de Segurança da Informação",
        "author": "Jason Andress",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["segurança", "cybersegurança", "segurança da informação", "hacking"],
        "description": "Introdução abrangente à segurança da informação: conceitos de CIA, ameaças, criptografia, controles de acesso e resposta a incidentes.",
        "isbn": "978-8575224915",
        "year": 2015,
        "language": "Português",
        "pages": 304,
        "buy_link": "https://www.amazon.com.br/s?k=Fundamentos+Seguran%C3%A7a+Informa%C3%A7%C3%A3o"
    },
    {
        "id": 38,
        "title": "Hacking: A Arte de Explorar Falhas",
        "author": "Jon Erickson",
        "level": 4,
        "level_label": "Avançado",
        "tags": ["hacking", "segurança", "exploits", "buffer overflow", "rede", "cybersegurança"],
        "description": "Mergulha fundo no hacking real: buffer overflows, shellcoding, exploração de rede e criptografia com exemplos em C e assembly.",
        "isbn": "978-8575223512",
        "year": 2012,
        "language": "Português",
        "pages": 494,
        "buy_link": "https://www.amazon.com.br/s?k=Hacking+Arte+Explorar+Falhas"
    },

    # ─── REDES ────────────────────────────────────────────────────────────────
    {
        "id": 39,
        "title": "Redes de Computadores",
        "author": "Andrew Tanenbaum, David Wetherall",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["redes", "redes de computadores", "tcp/ip", "protocolo", "infraestrutura"],
        "description": "O livro texto clássico de redes: modelo OSI, TCP/IP, Ethernet, wireless, segurança de redes e aplicações de rede em profundidade.",
        "isbn": "978-8576059240",
        "year": 2011,
        "language": "Português",
        "pages": 960,
        "buy_link": "https://www.amazon.com.br/s?k=Redes+de+Computadores+Tanenbaum"
    },

    # ─── JAVA ─────────────────────────────────────────────────────────────────
    {
        "id": 40,
        "title": "Use a Cabeça! Java",
        "author": "Kathy Sierra, Bert Bates",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["java", "programação", "oop", "orientação a objetos", "iniciante"],
        "description": "A forma mais divertida e eficaz de aprender Java. Cobre OOP, herança, polimorfismo, interfaces, exceções e muito mais.",
        "isbn": "978-8576082484",
        "year": 2007,
        "language": "Português",
        "pages": 688,
        "buy_link": "https://www.amazon.com.br/s?k=Use+a+Cabe%C3%A7a+Java"
    },
    {
        "id": 41,
        "title": "Java Efetivo",
        "author": "Joshua Bloch",
        "level": 4,
        "level_label": "Avançado",
        "tags": ["java", "programação", "boas práticas", "avançado"],
        "description": "O guia definitivo para escrever Java de qualidade. 90 itens de boas práticas cobertos com exemplos claros e explicações detalhadas.",
        "isbn": "978-8550804926",
        "year": 2019,
        "language": "Português",
        "pages": 412,
        "buy_link": "https://www.amazon.com.br/s?k=Java+Efetivo+Joshua+Bloch"
    },
    {
        "id": 42,
        "title": "Spring em Ação",
        "author": "Craig Walls",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["spring", "java", "backend", "framework", "api", "spring boot"],
        "description": "O guia prático mais popular sobre Spring Framework e Spring Boot: IoC, MVC, segurança, dados e microsserviços.",
        "isbn": "978-8550815435",
        "year": 2020,
        "language": "Português",
        "pages": 520,
        "buy_link": "https://www.amazon.com.br/s?k=Spring+em+A%C3%A7%C3%A3o+Craig+Walls"
    },

    # ─── C / C++ ──────────────────────────────────────────────────────────────
    {
        "id": 43,
        "title": "Linguagem C: Completo e Total",
        "author": "Herbert Schildt",
        "level": 2,
        "level_label": "Básico",
        "tags": ["c", "linguagem c", "programação", "sistemas"],
        "description": "Referência completa da linguagem C: tipos, ponteiros, estruturas, arquivos e programação de sistemas com exemplos práticos.",
        "isbn": "978-8534614542",
        "year": 1997,
        "language": "Português",
        "pages": 826,
        "buy_link": "https://www.amazon.com.br/s?k=Linguagem+C+Completo+Total+Schildt"
    },
    {
        "id": 44,
        "title": "C++ Primer",
        "author": "Stanley Lippman",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["c++", "cpp", "programação", "oop", "templates"],
        "description": "Introdução abrangente ao C++ moderno cobrindo a linguagem central, STL, templates e boas práticas de programação orientada a objetos.",
        "isbn": "978-0321714114",
        "year": 2012,
        "language": "Português",
        "pages": 976,
        "buy_link": "https://www.amazon.com.br/s?k=C%2B%2B+Primer+Lippman"
    },

    # ─── CLOUD / AWS ──────────────────────────────────────────────────────────
    {
        "id": 45,
        "title": "Amazon Web Services na Prática",
        "author": "Andreas Wittig, Michael Wittig",
        "level": 2,
        "level_label": "Básico",
        "tags": ["aws", "amazon", "cloud", "nuvem", "devops", "infraestrutura"],
        "description": "Guia prático para começar na AWS: EC2, S3, RDS, IAM, VPC, Lambda e arquiteturas de referência para produção.",
        "isbn": "978-8575226186",
        "year": 2018,
        "language": "Português",
        "pages": 560,
        "buy_link": "https://www.amazon.com.br/s?k=Amazon+Web+Services+na+Pr%C3%A1tica"
    },

    # ─── ALGORITMOS / ESTRUTURA DE DADOS ──────────────────────────────────────
    {
        "id": 46,
        "title": "Entendendo Algoritmos: Um Guia Ilustrado",
        "author": "Aditya Bhargava",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["algoritmos", "estrutura de dados", "programação", "lógica"],
        "description": "Introdução visual e divertida aos algoritmos mais importantes: busca binária, ordenação, grafos e programação dinâmica com ilustrações.",
        "isbn": "978-8575225028",
        "year": 2017,
        "language": "Português",
        "pages": 264,
        "buy_link": "https://www.amazon.com.br/s?k=Entendendo+Algoritmos+Aditya+Bhargava"
    },
    {
        "id": 47,
        "title": "Estruturas de Dados e Algoritmos com JavaScript",
        "author": "Loiane Groner",
        "level": 2,
        "level_label": "Básico",
        "tags": ["algoritmos", "estrutura de dados", "javascript", "programação"],
        "description": "Cobre as principais estruturas de dados (listas, pilhas, filas, árvores, grafos) e algoritmos de ordenação e busca implementados em JavaScript.",
        "isbn": "978-8575227015",
        "year": 2019,
        "language": "Português",
        "pages": 430,
        "buy_link": "https://www.amazon.com.br/s?k=Estruturas+Dados+Algoritmos+JavaScript+Loiane"
    },
    {
        "id": 48,
        "title": "Algoritmos: Teoria e Prática",
        "author": "Thomas H. Cormen, Charles E. Leiserson",
        "level": 5,
        "level_label": "Expert",
        "tags": ["algoritmos", "estrutura de dados", "teoria", "complexidade", "grafos"],
        "description": "O CLRS — a bíblia definitiva de algoritmos. Cobertura matemática rigorosa de todos os algoritmos e estruturas fundamentais da computação.",
        "isbn": "978-8535236996",
        "year": 2012,
        "language": "Português",
        "pages": 926,
        "buy_link": "https://www.amazon.com.br/s?k=Algoritmos+Cormen+Leiserson+portugu%C3%AAs"
    },

    # ─── DEVOPS / AGILE ───────────────────────────────────────────────────────
    {
        "id": 49,
        "title": "O Projeto Fênix",
        "author": "Gene Kim, Kevin Behr, George Spafford",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["devops", "agile", "gestão", "ti", "cultura", "transformação digital"],
        "description": "Romance empresarial que explica DevOps de forma envolvente. Apresenta os três caminhos do DevOps e como transformar a TI de uma empresa.",
        "isbn": "978-8550802640",
        "year": 2018,
        "language": "Português",
        "pages": 432,
        "buy_link": "https://www.amazon.com.br/s?k=O+Projeto+F%C3%AAnix+Gene+Kim"
    },
    {
        "id": 50,
        "title": "O Manual de DevOps",
        "author": "Gene Kim, Jez Humble, Patrick Debois",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["devops", "agile", "ci/cd", "integração contínua", "entrega contínua", "automação"],
        "description": "O guia prático de DevOps: princípios, práticas, ferramentas e casos de uso reais para implementar DevOps em organizações.",
        "isbn": "978-8550802657",
        "year": 2018,
        "language": "Português",
        "pages": 528,
        "buy_link": "https://www.amazon.com.br/s?k=Manual+DevOps+Gene+Kim"
    },

    # ─── HTML / CSS ───────────────────────────────────────────────────────────
    {
        "id": 51,
        "title": "HTML e CSS: Projete e Construa Websites",
        "author": "Jon Duckett",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["html", "css", "web", "frontend", "design", "desenvolvimento web"],
        "description": "Livro visual e belíssimo que ensina HTML e CSS do zero. O ponto de entrada ideal para o desenvolvimento web moderno.",
        "isbn": "978-8576089520",
        "year": 2016,
        "language": "Português",
        "pages": 490,
        "buy_link": "https://www.amazon.com.br/s?k=HTML+CSS+Jon+Duckett"
    },
    {
        "id": 52,
        "title": "CSS: The Definitive Guide",
        "author": "Eric Meyer, Estelle Weyl",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["css", "html", "web", "frontend", "design", "layout"],
        "description": "A referência mais completa sobre CSS: modelo de caixa, Flexbox, Grid, animações, pseudo-elementos e técnicas avançadas de layout.",
        "isbn": "978-1449393199",
        "year": 2018,
        "language": "Português",
        "pages": 1090,
        "buy_link": "https://www.amazon.com.br/s?k=CSS+Definitive+Guide"
    },

    # ─── PROGRAMAÇÃO GERAL / LÓGICA ───────────────────────────────────────────
    {
        "id": 53,
        "title": "Pense em Python",
        "author": "Allen B. Downey",
        "level": 1,
        "level_label": "Iniciante",
        "tags": ["python", "programação", "lógica", "iniciante", "pensamento computacional"],
        "description": "Introduz o pensamento computacional usando Python. Ideal para quem nunca programou: variáveis, funções, recursão e orientação a objetos.",
        "isbn": "978-8575228135",
        "year": 2016,
        "language": "Português",
        "pages": 352,
        "buy_link": "https://www.amazon.com.br/s?k=Pense+em+Python+Downey"
    },
    {
        "id": 54,
        "title": "O Codificador Limpo",
        "author": "Robert C. Martin",
        "level": 2,
        "level_label": "Básico",
        "tags": ["boas práticas", "profissionalismo", "engenharia de software", "carreira", "tdd", "código"],
        "description": "Uncle Bob fala sobre como ser um programador profissional: estimativas, TDD, prática deliberada e ética no desenvolvimento.",
        "isbn": "978-8576082705",
        "year": 2012,
        "language": "Português",
        "pages": 258,
        "buy_link": "https://www.amazon.com.br/s?k=O+Codificador+Limpo+Robert+Martin"
    },
    {
        "id": 55,
        "title": "O Programador Pragmático",
        "author": "David Thomas, Andrew Hunt",
        "level": 3,
        "level_label": "Intermediário",
        "tags": ["boas práticas", "programação", "engenharia de software", "carreira", "produtividade"],
        "description": "Conselhos práticos e atemporais sobre como ser um programador melhor: DRY, ortogonalidade, contratos, automação e debugging.",
        "isbn": "978-8575227244",
        "year": 2020,
        "language": "Português",
        "pages": 352,
        "buy_link": "https://www.amazon.com.br/s?k=Programador+Pragm%C3%A1tico"
    },
]


# ─── Tags por categoria para sugestões de busca ───────────────────────────────
SEARCH_SUGGESTIONS = [
    "Python", "JavaScript", "React", "Node.js", "Java", "C++", "SQL",
    "Git", "Docker", "Kubernetes", "Linux", "AWS", "Machine Learning",
    "Data Science", "Deep Learning", "Inteligência Artificial", "Segurança",
    "Algoritmos", "Estrutura de Dados", "Clean Code", "Arquitetura",
    "DevOps", "HTML", "CSS", "Spring", "Pandas", "TensorFlow", "Flask",
    "Backend", "Frontend", "Redes", "Shell", "Bash"
]


def _tokenize(text: str) -> set:
    """Quebra o texto em tokens de palavras inteiras (minúsculas, sem pontuação)."""
    import re
    return set(re.findall(r"[a-záàãâéêíóôõúüçñ0-9]+", text.lower()))


def search_books(query: str) -> list:
    """
    Busca livros por query (tag, título, autor ou descrição).
    Retorna lista ordenada por nível de dificuldade (mais fácil ao mais difícil).

    Scoring (por palavra da query encontrada):
      - tag exata ou tag contém a palavra: +4
      - palavra contém tag completa:       +3
      - título:                            +2
      - descrição:                         +1
      - autor:                             +1

    Para queries de múltiplas palavras (ex: "machine learning"),
    também testa a query completa como unidade nas tags e no título.
    """
    if not query or not query.strip():
        return []

    import re

    query_clean = query.strip().lower()
    query_tokens = set(re.findall(r"[a-záàãâéêíóôõúüçñ0-9]+", query_clean))

    scored_books = []

    for book in BOOKS:
        score = 0

        title_lower = book["title"].lower()
        desc_lower  = book["description"].lower()
        auth_lower  = book["author"].lower()
        tags_lower  = [t.lower() for t in book["tags"]]

        # ── Bônus por query completa (ex: "machine learning") ──────────────
        if len(query_tokens) > 1:
            # Tag contém a query completa
            if any(query_clean in tag for tag in tags_lower):
                score += 6
            # Título contém a query completa
            if query_clean in title_lower:
                score += 4

        # ── Score por token individual ──────────────────────────────────────
        for word in query_tokens:
            if len(word) < 2:
                continue  # ignora palavras muito curtas

            for tag in tags_lower:
                tag_tokens = _tokenize(tag)
                if word in tag_tokens:
                    score += 4          # palavra exata numa tag
                elif len(word) >= 3 and word in tag:
                    score += 3          # palavra é substring de tag (mín 3 chars)
                elif len(tag) >= 3 and tag in word:
                    score += 3          # tag é substring da palavra (ex: "sql" em "mysql")

            if re.search(r"\b" + re.escape(word) + r"\b", title_lower):
                score += 2

            if re.search(r"\b" + re.escape(word) + r"\b", desc_lower):
                score += 1

            if re.search(r"\b" + re.escape(word) + r"\b", auth_lower):
                score += 1

        if score > 0:
            scored_books.append((score, book))

    # Ordena: primeiro por relevância (desc), depois por nível (asc)
    scored_books.sort(key=lambda x: (-x[0], x[1]["level"]))

    # Descarta livros com score muito baixo (prováveis falsos positivos)
    if scored_books:
        max_score = scored_books[0][0]
        threshold = max(2, max_score * 0.20)
        scored_books = [(s, b) for s, b in scored_books if s >= threshold]

    # Remove duplicatas e retorna apenas os livros
    seen = set()
    results = []
    for _, book in scored_books:
        if book["id"] not in seen:
            seen.add(book["id"])
            results.append(book)

    # Reordena os resultados finais por nível de dificuldade (1 → 5)
    results.sort(key=lambda b: b["level"])

    return results
