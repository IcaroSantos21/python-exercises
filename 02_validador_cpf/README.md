# Validador de CPF em Python

Este projeto implementa a validação de CPF em Python utilizando **boas práticas de engenharia de software**, com foco em organização, testabilidade e uso correto de bibliotecas externas.

O sistema possui:
* **Validação manual:** Implementação própria baseada no algoritmo oficial.
* **Validação via biblioteca:** Uso da biblioteca externa `validate-docbr`.
* **Testes automatizados:** Suite de testes com `pytest`.
* **Arquitetura limpa:** Separação clara entre lógica de negócio, interface e execução.


## 📂 Estrutura do Projeto

```text
.
├── cpf_utils.py           # Implementação manual da lógica de validação
├── cpf_lib_validator.py   # Wrapper para a biblioteca validate-docbr
├── main.py                # Ponto de entrada principal
├── menu.py                # Interface de interação com o usuário
├── tests/                 # Testes automatizados
│   ├── __init__.py
│   └── test_cpf_utils.py  
├── README.md
├── .tool-versions         # Versões de ferramentas (ex: Python)
└── .gitignore             # Configurado para ignorar venv, caches e temporários

```

> **Nota:** Diretórios como `venv/`, `__pycache__/` e `.pytest_cache/` não são versionados para manter o repositório limpo.

---

## 🛠️ Componentes do Sistema

### 1. Validação Manual (`cpf_utils.py`)

Contém a lógica desenvolvida do zero para validar a regra de negócio dos dígitos verificadores. As etapas incluem:

* **Sanitização:** Remoção de caracteres não numéricos.
* **Check de Integridade:** Verifica tamanho (11 dígitos) e impede sequências repetidas (ex: `111.111.111-11`).
* **Cálculo Algorítmico:** Orquestração do cálculo dos dois dígitos verificadores.

### 2. Validação com Biblioteca (`cpf_lib_validator.py`)

Encapsula a biblioteca `validate-docbr`. Esta abordagem garante:

* **Baixo acoplamento:** Se a biblioteca mudar, alteramos apenas este arquivo.
* **Confiabilidade:** Uso de código testado pela comunidade em ambiente de produção.

### 3. Interface e Execução

* **`main.py`:** Ponto de entrada que inicia a aplicação.
* **`menu.py`:** Gerencia a entrada de dados e exibição de resultados, mantendo a regra de negócio isolada da interface.

---

## 🧪 Testes Automatizados

Os testes garantem que qualquer refatoração futura não quebre as regras existentes.

**Cenários testados:**

* CPFs válidos (com e sem formatação).
* CPFs inválidos (dígitos incorretos).
* Entradas com letras ou caracteres especiais.
* CPFs com todos os números iguais.

Para rodar os testes:

```bash
pytest -v

```

---

## 🚀 Como Executar

### Pré-requisitos

* Python 3.x
* Ambiente virtual (recomendado)

### Instalação

1. **Clone o repositório** e acesse a pasta.
2. **Crie e ative o ambiente virtual:**
```bash
python -m venv venv
# No Linux/macOS:
source venv/bin/activate
# No Windows:
.\venv\Scripts\activate

```


3. **Instale as dependências:**
```bash
pip install validate-docbr pytest

```


4. **Execute a aplicação:**
```bash
python main.py

```



---

## 🧠 Boas Práticas Adotadas

* **Separação de Preocupações (SoC):** Lógica, interface e testes não se misturam.
* **DRY (Don't Repeat Yourself):** Reuso de funções de sanitização.
* **Single Responsibility Principle:** Cada função possui apenas uma responsabilidade clara.
* **Encapsulamento:** Dependências externas são isoladas em módulos específicos.

---

## 👤 Autor: Icaro Santos

Projeto desenvolvido para fins de estudo e prática de engenharia de software em Python.

```