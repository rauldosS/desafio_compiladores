1) (Extrator de caracteres de um arquivo) - Desenvolva um programa que leia um arquivo de texto e o decomponha na sequência de caracteres ASCII individuais nele contidos;

2) (Inclusão de um filtro para eliminar os caracteres não desejados) - Acrescente ao programa construído uma seção que receba como entrada uma lista de caracteres indesejados e, com eles, inclua no programa um filtro que remova da sequência originalmente encontrada de caracteres ASCII todas as ocorrências dos caracteres que constam dessa lista. Em particular, use esse programa para fazer a eliminação de brancos, espaçadores, tabulações, marcas de final de linha, final de arquivo, formatação, etc.

3) (listagem numerada) - O programa deve ler o arquivo gerado e criar a partir dele uma listagem do texto, acrescido do número sequencial de suas linhas.

5) (Conversão numérica) - Desenvolva programas de conversão numérica de entrada e de saída de dados que efetuem a leitura dos dados escritos em diversas bases numéricas e armazenem na memória os valores convertidos, denotados em uma notação padrão. Faça o mesmo para a saída de dados, escolhendo a base e o formato de saída (número de dígitos a imprimir, posição do sinal, etc.)

6) (Tabelas de símbolos e atributos) - Desenvolva um programa que monte uma tabela de símbolos, em que cada símbolo possa se apresentar com um comprimento arbitrário. Construa também procedimentos para ordená-los alfabeticamente, para pesquisar um símbolo específico na tabela, para incluir um elemento adicional, para associar atributos a um dado símbolo etc.

7) (Tabelas de palavras reservadas) - Desenvolva um procedimento de pesquisa em tabelas de conteúdo fixo, tais como as de palavras reservadas e similares.

A atividade pode ser desenvolvida individual ou no máximo em grupos de 3 pessoas.

Pode ser utilizada a linguagem de programação de sua preferência.

Deve ser apresentado em 21/10/20

# Desenvolvido com Django framework

Ao adicionar (enviar) um novo arquivo para o banco de dados, será possível realizar a decomposição do conteúdo do mesmo para recuperar a sequência de caracteres ASCII individuais.
Cada um destes caracteres são um novo registro em uma tabela, sendo associados pelo identificador do arquivo correspondente, estes caracteres terão um campo para identificação de "atividade", ou seja, ao adicionar um novo arquivo todos os caracteres originais serão cadastrados na tabela "secundária", com sua respectiva sequência, neste caso será possível"desabilitar" ou "filtrar" um caractere e atualizar/reconstruir o arquivo apenas com os ativos, e caso seja necessário, será fácil reconstruir o mesmo com sua estrutura original.
