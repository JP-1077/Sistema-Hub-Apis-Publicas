# Sistema Hub APIs Públicas

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript)

[Visão Geral](#visão-geral-do-projeto) • [Objetivos](#objetivo-do-projeto) • [Estrutura](#estrutura-de-pastas-do-projeto) • [Tecnologias](#ferramentas-utilizadas) • [Benefícios](#benefícios-do-projeto)

</div>

---

## 📋 Visão Geral do Projeto

**Sistema Hub APIs Públicas** é uma aplicação Full-Stack que centraliza e organiza dados de três APIs públicas populares: **Rick & Morty**, **Disney** e **Star Wars**. O projeto funciona como um agregador de dados que consome informações dessas franquias, armazena localmente em um banco de dados SQLite e apresenta em uma interface web responsiva e intuitiva.

### Escopo Técnico

A arquitetura segue o padrão **Cliente-Servidor**, onde:

- **Backend** (Flask + SQLite): Responsável por consumir as APIs externas, processar dados, gerenciar cache e fornecer endpoints REST estruturados
- **Frontend** (HTML/CSS/JavaScript): Interface responsiva que comunica com o backend via requisições assíncronas, exibindo dados de forma organizada e interativa
- **Camada de Dados**: Banco SQLite para persistência local, eliminando chamadas repetidas às APIs externas



---

## 🎯 Objetivo do Projeto

### Objetivos Primários

1. **Criar um agregador de dados unificado** que consolida informações de três APIs públicas distintas em uma única interface, eliminando a necessidade de consultar múltiplos endpoints

2. **Aprimorar competências Full-Stack** de forma prática, desenvolvendo tanto a camada de backend (consumo de APIs, processamento de dados, design de endpoints) quanto de frontend (DOM manipulation, comunicação assíncrona, UX responsiva)

3. **Implementar boas práticas de engenharia de software** desde o início do projeto, incluindo:
   - Versionamento com Git
   - Documentação técnica clara
   - Arquitetura modular e escalável
   - Separação de responsabilidades

### Objetivos Secundários

- Demonstrar proficiência em integração de APIs REST externas
- Explorar padrões de cache para otimização de performance
- Implementar filtros e busca eficientes em grandes datasets
- Documentar o processo de desenvolvimento para portfólio profissional

---

## ✍🏽 System Design

### Design da Aplicação

```

**APIs Públicas** 
|
Backend (Flask) 
|
SQLite 
|
Frontend (JavaScript) 
| 
Usuário**

```
### 📁 Estrutura de Pastas do Projeto

```
Sistema Hub APIs Públicas/
│
├── 📄 README.md                      # Documentação principal
├── 📄 CONTRIBUTING.md                # Guia de contribuição
├── 📄 .gitignore                     # Arquivos ignorados pelo Git
├── 📄 requirements.txt               # Dependências Python
├── 📄 .env.example                   # Variáveis de ambiente (template)
│
│
├── 📁 backend/                       # ⚙️ NÚCLEO DA APLICAÇÃO
│   ├── 📄 app.py                     # Factory function e inicialização Flask
│   ├── 📄 config.py                  # Configurações (dev, test, prod)
│   ├── 📄 run.py                     # Entry point para rodar servidor
│   │
│   ├── 📁 models/                    # 🗄️ Definições de tabelas SQLAlchemy
│   │   ├── 📄 __init__.py
│   │   ├── 📄 character.py           # Modelo para personagens genéricos
│   │   ├── 📄 movie.py               # Modelo para filmes
│   │   └── 📄 planet.py              # Modelo para planetas
│   │
│   ├── 📁 routes/                    # 🛣️ Endpoints REST da API
│   │   ├── 📄 __init__.py
│   │   ├── 📄 rickmorty.py           # Rotas: /api/rickmorty/*
│   │   ├── 📄 disney.py              # Rotas: /api/disney/*
│   │   └── 📄 starwars.py            # Rotas: /api/starwars/*
│   │
│   ├── 📁 services/                  # 🔧 Lógica de negócio e integrações
│   │   ├── 📄 __init__.py
│   │   ├── 📄 api_consumer.py        # Consumo das APIs externas
│   │   ├── 📄 cache_manager.py       # Estratégia de cache em memória
│   │   ├── 📄 data_processor.py      # Transformação e validação de dados
│   │   └── 📄 sync_manager.py        # Sincronização de dados
│   │
│   ├── 📁 database/                  # 💾 Gerenciamento do banco de dados
│   │   ├── 📄 __init__.py
│   │   ├── 📄 db.py                  # Inicialização SQLAlchemy + context
│   │   └── 📁 migrations/            # Migrações futuras (Alembic)
│   │
│   └── 📁 utils/                     # 🛠️ Utilitários e helpers
│       ├── 📄 __init__.py
│       ├── 📄 logger.py              # Configuração de logging
│       ├── 📄 decorators.py          # Decoradores reutilizáveis
│       └── 📄 constants.py           # Constantes da aplicação
│
│
├── 📁 frontend/                      # 🎨 INTERFACE DO USUÁRIO
│   ├── 📄 index.html                 # Página principal (dashboard)
│   ├── 📄 about.html                 # Página sobre o projeto
│   ├── 📄 404.html                   # Página de erro
│   │
│   ├── 📁 css/
│   │   ├── 📄 style.css              # Estilos principais (grid, cores, tipografia)
│   │   ├── 📄 responsive.css         # Media queries (mobile-first)
│   │   └── 📄 animations.css         # Transições e animações
│   │
│   ├── 📁 js/
│   │   ├── 📄 main.js                # Lógica principal e inicialização DOM
│   │   ├── 📄 api-client.js          # Classe para comunicação com backend
│   │   ├── 📄 dom-utils.js           # Funções para manipulação do DOM
│   │   ├── 📄 constants.js           # URLs, configurações, enums
│   │   └── 📄 utils.js               # Helpers gerais (formatação, etc)
│   │
│   └── 📁 assets/                    # 📦 Recursos estáticos
│       ├── 📁 images/                # Imagens (personagens, backdrops)
│       ├── 📁 icons/                 # Ícones (SVG, favicons)
│       └── 📁 fonts/                 # Web fonts customizadas
│
│
├── 📁 tests/                         # 🧪 Suite de testes (futuro)
│   ├── 📄 __init__.py
│   ├── 📁 backend/
│   │   ├── 📄 test_routes.py         # Testes de endpoints
│   │   └── 📄 test_services.py       # Testes de lógica
│   └── 📁 frontend/
│       └── 📄 test_api_client.js     # Testes de API client
│
│
└── 📁 docs/                          # 📚 Documentação técnica
    ├── 📄 API_REFERENCE.md           # Referência completa de endpoints
    ├── 📄 SETUP.md                   # Guia de instalação e configuração
    ├── 📄 ARCHITECTURE.md            # Diagrama e decisões arquiteturais
    └── 📄 DATABASE_SCHEMA.md         # Estrutura do banco de dados
```

### Explicação da Estrutura

#### **Backend**
- Separação clara entre rotas, lógica de negócio e acesso a dados
- Services encapsulam a complexidade de consumir APIs externas
- Models definem o contrato de dados com o banco

#### **Frontend**
- Estrutura simples e escalável
- CSS organizado por responsabilidade
- JavaScript modular com separação de conceitos
- Assets centralizados para fácil manutenção

#### **Raiz do Projeto**
- Configurações globais (.env, requirements.txt)
- Documentação acessível (README, CONTRIBUTING)
- Git versionado desde o início

---

## 🔧 Ferramentas Utilizadas

### Backend

| Ferramenta | Versão | Propósito | Justificativa |
|-----------|--------|----------|--------------|
| **Python** | 3.9+ | Linguagem | Ecosistema rich, comunidade ativa |
| **Flask** | 3.0 | Framework Web | Leve, flexível, ideal para APIs REST |
| **SQLAlchemy** | 2.0 | ORM | Abstração de banco, queries type-safe |
| **SQLite** | 3 | Banco de Dados | Zero-config, perfeito para dev/prototipo |
| **Requests** | 2.31 | HTTP Client | Consumir APIs externas com simplicidade |
| **Flask-CORS** | 4.0 | Middleware | Permitir requisições cross-origin |
| **python-dotenv** | 1.0 | Env Config | Variáveis de ambiente seguras |

### Frontend

| Ferramenta | Tipo | Justificativa |
|-----------|------|--------------|
| **HTML5** | Markup | Semântico, moderno, nativo |
| **CSS3** | Estilo | Flexbox/Grid para layouts responsivos |
| **JavaScript (ES6+)** | Lógica | Fetch API nativa, sem dependências pesadas |
| **Responsive Design** | Padrão | Mobile-first, acessível em todos os devices |

### DevOps & Versionamento

| Ferramenta | Propósito |
|-----------|-----------|
| **Git** | Controle de versão distribuído |
| **GitHub** | Hospedagem e colaboração |
| **pip** | Gerenciador de pacotes Python |
| **Virtual Environment** | Isolamento de dependências |

### APIs Consumidas

```
Rick & Morty:  https://rickandmortyapi.com/api
Disney:        https://api.disneyapi.dev
Star Wars:     https://swapi.dev/api/
```

Todas são **públicas e gratuitas**, sem autenticação necessária.

---

## 💡 Benefícios do Projeto

#### 1. **Experiência Unificada**
- Explora dados de 3 universos em um só lugar
- Não precisa navegar múltiplos sites/APIs
- Interface intuitiva e responsiva
- Busca e filtros eficientes

#### 2. **Performance Otimizada**
- Cache local reduz chamadas às APIs
- Carregamento rápido após primeira sincronização
- Menos latência comparado a APIs diretas
- Escalabilidade horizontal possível

#### 3. **Confiabilidade**
- Fallback se APIs externas caírem (dados em cache)
- Validação de dados antes de exibir
- Tratamento de erros gracioso
- Sincronização automática


---

## 🎓 Conclusão do Projeto

### Propósito Alcançado

**Sistema Hub APIs Públicas** é mais que um agregador de dados—é um **laboratório prático de engenharia de software**. Ao desenvolvê-lo, você não apenas cria uma aplicação funcional, mas também:

✨ **Consolida conhecimentos** em padrões arquiteturais reais  
✨ **Pratica disciplina técnica** desde o design até deployment  
✨ **Constrói portfólio robusto** demonstrando profissionalismo  
✨ **Cria fundação** para evolução futura com tecnologias avançadas  

