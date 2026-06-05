# Database

## Visão Geral

A pasta `database` contém scripts, configurações e documentação relacionados ao banco de dados da aplicação. Este diretório gerencia a estrutura de dados, migrações e inicialização do banco de dados.

## Objetivo

Gerenciar e manter a integridade do banco de dados através de:

- Definição de schemas e estruturas de tabelas
- Controle de versão das migrações
- Scripts de inicialização e seeding
- Documentação da estrutura de dados
- Backup e restauração de dados
- Otimização de queries

## Estrutura de Arquivos

Exemplos de arquivos e pastas que podem estar neste diretório:

## Exemplos de Arquivos

```
database/
├── schema.sql            # Definição do schema principal
├── init.sql              # Script de inicialização
├── seed_data.sql         # Dados iniciais/fixtures
├── migrations/
│   ├── 001_create_users.sql
│   ├── 002_create_products.sql
│   └── 003_add_user_roles.sql
├── procedures/           # Stored procedures
│   └── get_user_stats.sql
├── triggers/             # Triggers de banco de dados
│   └── audit_log_trigger.sql
├── backups/              # Backups do banco
│   └── backup_2024.sql
├── config/
│   ├── connection.json   # Configurações de conexão
│   └── database.yml      # Arquivo de configuração
└── README.md             # Documentação do banco de dados
```
