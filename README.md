# VerdeVias - Transporte Sustentavel

## Solução Sustentável para a Mobilidade Urbana da Região Metropolitana de São Paulo



## Descrição do Projeto

VerdeVias é uma iniciativa que visa transformar a mobilidade urbana na Região Metropolitana de São Paulo, promovendo um sistema de transporte público mais sustentável e eficiente. Este projeto propõe a transição para fontes de energia renovável, como solar e elétrica, e o uso de inteligência artificial para otimizar o planejamento de rotas e o consumo energético. Nosso objetivo é reduzir a pegada de carbono do transporte público e melhorar a qualidade de vida urbana.

O sistema utiliza um banco de dados Oracle com quatro tabelas principais: **TIPO_FONTES**, **EMISSOES_CARBONO**, **PROJETOS_SUSTENTAVEIS** e **REGIOES_SUSTENTAVEIS**. Estas tabelas armazenam informações essenciais sobre fontes de emissão, projetos de sustentabilidade, emissões de carbono e regiões atendidas, formando a base para a análise e o monitoramento de indicadores de sustentabilidade.

## Objetivos do Projeto

- Implementar um sistema de CRUD (Inserir, Excluir, Alterar, Consultar) para gerenciar as informações do banco de dados de forma eficiente.
  
- Oferecer funcionalidades de consulta ao banco de dados com opções de filtro e exportação dos resultados.
  
- Integrar o sistema com um banco de dados Oracle para armazenamento e manipulação de dados relacionados a projetos sustentáveis e emissões de carbono.

## Funcionalidades

- **Menu de Opções**: Interface interativa para navegação e acesso às funcionalidades do sistema.
  
- **CRUD Completo**: Operações de criação, leitura, atualização e exclusão de registros no banco de dados.
  
- **Consultas Filtradas**: Possibilidade de realizar consultas com filtros específicos aplicados na cláusula `WHERE`.
  
- **Exportação de Dados**: Opção para exportar os resultados das consultas em formatos como JSON ou Excel.
  
- **Validação de Entradas**: Garantia de integridade dos dados por meio de validações das entradas do usuário.
  
- **Tratamento de Exceções**: Manejo de erros de forma a assegurar a estabilidade e segurança do sistema.

## Requisitos do Sistema

1. **Banco de Dados**: Oracle, com as tabelas e relacionamento conforme o modelo apresentado.
   
2. **Interface de Usuário**: Menu de opções para navegação das funcionalidades.
   
3. **Estrutura do Código**:
   - Estruturas de decisão e repetição.
   - Subalgoritmos (Funções e Procedimentos) com passagem de parâmetros e retorno, onde aplicável.
   - Manipulação de arquivos texto ou JSON para exportação de dados.
     
4. **Consultas e Exportação**:
   - Implementar pelo menos três consultas diferentes com filtros na cláusula `WHERE`.
   - Disponibilizar exportação para arquivos de dados nos formatos JSON ou Excel.

## Modelo de Dados

As principais tabelas no banco de dados são:

1. **TIPO_FONTES**
   - `ID_TIPO_FONTE` (chave primária): Identificador do tipo de fonte de emissão.
   - `NOME`: Nome do tipo de fonte (ex.: solar, elétrica).

2. **EMISSOES_CARBONO**
   - `ID_EMISSAO` (chave primária): Identificador da emissão de carbono.
   - `ID_TIPO_FONTE` (chave estrangeira): Referência ao tipo de fonte.
   - `EMISSAO`: Quantidade de emissão em unidades específicas.

3. **PROJETOS_SUSTENTAVEIS**
   - `ID_PROJETO` (chave primária): Identificador do projeto sustentável.
   - `DESCRICAO`: Descrição detalhada do projeto.
   - `CUSTO`: Custo estimado para implementação do projeto.
   - `STATUS`: Status do projeto.
   - `ID_TIPO_FONTE` (chave estrangeira): Tipo de fonte de energia do projeto.
   - `ID_REGIAO` (chave estrangeira): Região onde o projeto está localizado.

4. **REGIOES_SUSTENTAVEIS**
   - `ID_REGIAO` (chave primária): Identificador da região.
   - `NOME`: Nome da região.

## Estrutura do Projeto

O código segue uma abordagem modular, com funções separadas para cada operação CRUD e para as funcionalidades de consulta e exportação de dados. As principais funcionalidades estão organizadas em um menu, facilitando a navegação e o uso do sistema. 

As operações de manipulação de dados são integradas com o banco de dados Oracle, e o código inclui validações de entrada e tratamento de exceções para garantir a integridade dos dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para a implementação do sistema.
- 
- **Oracle**: Banco de dados relacional para armazenamento e manipulação de dados.
- 
- **JSON e Excel**: Formatos de exportação de dados.
- 
- **Inteligência Artificial e Análise de Dados**: Para otimização de rotas e eficiência no transporte público.

## Como Executar

1. Configure o banco de dados Oracle com as tabelas e relacionamentos descritos.
   
2. Execute o script principal do sistema em Python.
   
3. Navegue pelas opções do menu para realizar operações de inserção, consulta, atualização, exclusão, e exportação de dados.

## Contribuição 🧑‍💻

⮕ Jennifer Eduarda Vieira Daleffi - RM557137 - Gestao e Back-end Python

⮕ Leonardo Cadena de Sousa - RM557528 - Fullstack: Java Back-end e Front-end

⮕ Julia Vasconselos Oliveira - RM558785 - Analista de Dados: SQL e IA

TODOS OS MEMBROS SAO DA TURMA 1TDSPF - FIAP - ANALISE E DESENVOLVIMENTO DE SISTEMAS: SEGUNDO SEMESTRE DE 2024
