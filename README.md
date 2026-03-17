# Descrição do Projeto

Este projeto tem como objetivo criar um sistema que ajude a coordenação do SENAI a acompanhar o desempenho dos alunos de forma mais rápida e organizada.

Atualmente, as notas chegam de diferentes formas e com quantidades variadas de atividades, o que torna o processo de análise mais demorado e sujeito a erros. Além disso, em alguns casos os dados podem estar incompletos ou incorretos.

Para resolver esse problema, o sistema foi desenvolvido para:

Processar as notas dos alunos

Calcular automaticamente a média de cada estudante

Identificar alunos em recuperação

Destacar alunos com melhor desempenho

Tratar possíveis erros nos dados

Gerar um relatório final em arquivo .txt

O sistema também foi pensado para ter um código organizado e modular, facilitando a manutenção e futuras melhorias.

# Objetivo do Sistema

O objetivo principal é facilitar o trabalho da coordenação acadêmica, permitindo que a análise do desempenho dos alunos seja feita de forma mais rápida, segura e confiável.

Com isso, o sistema ajuda a:

Reduzir erros no cálculo de médias

Identificar rapidamente alunos que precisam de recuperação

Destacar alunos com bom desempenho

Gerar relatórios claros para consulta e acompanhamento

# Requisitos do Sistema  Requisitos Funcionais (RF)

São as funções que o sistema precisa realizar:

Receber as notas dos alunos

Processar os dados de cada estudante

Verificar se existem erros ou dados incompletos

Calcular a média das notas

Classificar os alunos de acordo com o desempenho

Identificar alunos em recuperação

Destacar alunos com melhores resultados

Gerar um relatório final em arquivo .txt

# Requisitos Não Funcionais (RNF)

São características de qualidade do sistema:

O código deve ser organizado e modular

O sistema deve tratar erros nos dados recebidos


# Regras de Negócio

A média do aluno será calculada com base nas notas disponíveis.

Se a lista de notas estiver vazia ou inválida, o sistema deve tratar o erro.

Alunos com média abaixo de 6.0 ficam em recuperação.

Alunos com média igual ou maior que 6.0 são considerados aprovados.

Os alunos com maiores médias devem ser destacados no relatório.

Todas as informações devem ser registradas no relatório final.
-------------------