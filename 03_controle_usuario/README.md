# Controle de Usuários em Python (Mini CRUD)

Este projeto implementa um **sistema simples de controle de usuários em Python**, com foco em boas práticas de programação, organização de código, regras de negócio claras e testes automatizados.

O objetivo principal é simular um **CRUD realista**, semelhante ao que é encontrado em sistemas do dia a dia, sem depender de frameworks ou bancos de dados complexos.

---

## Funcionalidades

- Criar usuários
- Atualizar dados do usuário (nome e email)
- Ativar e desativar usuários (soft delete)
- Listar usuários
- Buscar usuário por ID
- Persistir dados em arquivo JSON
- Testes unitários e teste de integração mínima

---

## Regras de Negócio

- O ID do usuário é criado automaticamente e **não pode ser alterado**
- Não é permitido criar usuários com email duplicado
- Atualizações ignoram strings vazias (`""`)
- Usuários desativados permanecem no sistema (delete lógico)
- Não é possível desativar um usuário já desativado

---

## Estrutura do Projeto



03_controle_usuario/
├── main.py
├── user_utils.py
├── json_utils.py
├── menu.py
└── tests/
├── test_user_utils.py
└── test_user_flow.py


---

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd 03_controle_usuario


Execute o programa:

python main.py

Como Executar os Testes

O projeto utiliza pytest.

Instale o pytest (se necessário):

pip install pytest


Execute os testes:

pytest -v

Tecnologias Utilizadas

Python 3

Pytest

Persistência em JSON

Programação funcional e orientada a dados

Observações Finais

Este projeto foi desenvolvido com foco em:

clareza de código

separação de responsabilidades

testes como ferramenta de validação e segurança

raciocínio de engenharia de software, não apenas sintaxe

Ele serve tanto como exercício de aprendizado quanto como projeto de portfólio inicial.


---

## Próximo passo recomendado (fora do código)

Suba isso no GitHub e use este projeto como:
- base para outros domínios (produtos, pedidos, estoque)
- material para explicar em entrevistas
- referência de padrão para projetos futuros

Quando quiser evoluir para o próximo nível, você já tem a base certa.