# 🤖 Automação de Processos com Python | Data-Driven Process Automation

## 📌 Visão Geral
Este projeto apresenta uma **automação completa de processos operacionais utilizando Python**, com foco em **ganho de eficiência, redução de erros manuais e integração entre dados e sistemas**.

A solução automatiza o **cadastro de produtos em um sistema web**, simulando a interação humana com o navegador (abertura, navegação e preenchimento de formulários), a partir de uma **base de dados estruturada em CSV**.

O projeto conecta **automação de tarefas + manipulação de dados**, evidenciando como Python pode ser utilizado para **escalar processos repetitivos orientados a dados**, um cenário recorrente em ambientes corporativos e altamente valorizado em áreas de **Dados, BI e Engenharia de Dados**.

---

## 🎯 Objetivo do Projeto
- Automatizar o preenchimento de formulários web de forma confiável
- Eliminar tarefas manuais repetitivas
- Integrar dados estruturados com sistemas operacionais
- Demonstrar uso prático de Python para automação de processos
- Evidenciar competências aplicáveis a Análise de Dados, BI e Engenharia de Dados

---

## ▶ Demonstração do Processo
1. O script `codigo.py` é iniciado  
2. O navegador é aberto automaticamente  
3. Os dados do arquivo `produtos.csv` são lidos  
4. Cada linha da base de dados é processada  
5. O formulário é preenchido e enviado automaticamente  

---

## 🧠 Descrição do Processo Automatizado
O fluxo da automação segue as seguintes etapas técnicas:

- Inicialização do script principal
- Controle de tempo para sincronização entre ações
- Leitura da base de dados com Pandas
- Iteração linha a linha da base de produtos
- Mapeamento de colunas para campos do formulário
- Preenchimento automático e envio dos dados
- Repetição do processo até o cadastro completo

Todo o processo é executado **sem intervenção humana**, após a inicialização do script.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas
- **Python**
- **PyAutoGUI** – automação de interface gráfica
- **Pandas** – leitura e manipulação de dados
- **Time** – controle de tempo e sincronização
- **CSV** como fonte de dados estruturados

---

## 📂 Estrutura do Repositório
```
│
├── README.md # Documentação do projeto
├── codigo.py # Script principal de automação
├── auxiliar.py # Script auxiliar para captura de coordenadas
├── produtos.csv # Base de dados com os produtos
├── automation_form.png# Print do formulário automatizado
```

---


---

## 📊 Base de Dados Utilizada
A base de dados `produtos.csv` contém informações estruturadas utilizadas como entrada do processo automatizado, incluindo:

- Código do produto
- Marca
- Tipo
- Categoria
- Preço unitário
- Custo
- Observações (OBS)

Os dados são lidos com **Pandas** e utilizados diretamente no preenchimento do formulário.

---

## 🔁 Lógica da Automação
- O script percorre cada linha da base de dados utilizando um loop
- Cada coluna é mapeada para um campo específico do formulário
- Os dados são convertidos para texto quando necessário
- Campos opcionais são tratados para evitar falhas no processo
- O ciclo se repete até o cadastro completo de todos os registros

---

## 🧩 Destaques Técnicos
- Integração entre **dados estruturados e automação de processos**
- Uso de loops (`for`) para escalabilidade
- Tratamento de valores nulos
- Separação de responsabilidades entre scripts
- Simulação realista de interação humana com sistemas web

---

## 🚀 Aplicações Práticas
Este tipo de automação pode ser aplicado em:
- Cadastro de produtos, clientes ou fornecedores
- Migração de dados entre sistemas
- Processos administrativos e operacionais
- Apoio a áreas de Dados, BI, Operações e Backoffice
- Redução de custos operacionais e erros humanos

---

## 📬 Contato
Fico à disposição para conversar sobre este projeto, trocar ideias sobre **Análise de Dados, Business Intelligence, Engenharia ou Ciência de Dados**, além de discutir soluções de **automação orientadas a dados** e novos desafios em tecnologia.

- 💼 LinkedIn: [Jéssica Fuentes](https://www.linkedin.com/in/j%C3%A9ssica-fuentes/)
