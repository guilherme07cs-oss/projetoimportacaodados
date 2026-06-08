# Projeto Importação de Dados com Python

## Sobre o Projeto

Este projeto foi desenvolvido em Python com o objetivo de simular um cenário real de migração de dados entre sistemas.

A aplicação realiza a leitura de um arquivo CSV contendo informações de produtos e importa esses dados para um banco de dados SQLite de forma automatizada.

Além da importação, o sistema possui uma interface gráfica desenvolvida com Tkinter, permitindo que o usuário visualize os dados importados e realize pesquisas diretamente na aplicação.

---

## Funcionalidades

- Importação de dados a partir de arquivos CSV
- Armazenamento automático em banco SQLite
- Interface gráfica desenvolvida com Tkinter
- Exibição dos registros em tabela
- Pesquisa de produtos
- Registro de auditoria:
  - Data da importação
  - Usuário responsável
  - Arquivo de origem
  - Status da operação

---

## Tecnologias Utilizadas

- Python 3.13.7
- Pandas
- SQLite
- Tkinter

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/guilherme07cs-oss/projetoimportacaodados.git
```

Acesse a pasta:

```bash
cd projetoimportacaodados
```

Instale as dependências:

```bash
pip install pandas
```

---

## Como Executar

Execute o sistema:

```bash
python app.py
```

---

## Exemplo de Arquivo CSV

```csv
produto;quantidade;preco
i5-10400;5;100
RTX 5060;6;200
Ryzen 7 7700X;12;400
```

---

## Exemplo de Dados Importados

| Produto | Quantidade | Preço |
|----------|------------|--------|
| i5-10400 | 5 | 100 |
| RTX 5060 | 6 | 200 |
| Ryzen 7 7700X | 12 | 400 |

---

## Objetivo Acadêmico

Este projeto foi desenvolvido como parte do Projeto Integrador, com foco em:

- Integração de Sistemas
- Migração de Dados
- Bancos de Dados
- Automação de Processos
- Uso de Inteligência Artificial no Desenvolvimento de Software

---

## Autor

**Guilherme Costa da Silva**

GitHub:
https://github.com/guilherme07cs-oss