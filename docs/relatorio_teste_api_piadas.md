Relatório de Teste - QA Challenge: Testando a API de Piadas

## Introdução
Este relatório descreve os testes feio na API de piadas aleatórias. Foram realizados testes funcionais, de carga, análise das repostas e validações para garantir a integridade dos dados. 

## Estrutura do Projeto

teste_api/
├── tests/
│   └── test_piada.py    
├── reports/
│   ├── evidencias/       
│   └── relatorio_testes.md 
├── locustfile.py    
├── README.md      

## Objetivos 
. Verificar se a API retorna piadas com campos corretos
. Garantir que os tipos de dados sejam válidos e consistentes. 
. Avaliar o desempenho sob carga simulada
. Identificar possíveis erros, como IDS duplicados 

## Ambiente de Teste
. Windows 11 Pro
. Python: 3.13
   Ferramentas: 
     .Pytest 
     . Locust
     .Requests

## Plano de teste
   ## Funcionalidades
     . Validação das respostas JSON. 
     .Verificação dos campos obrigatórios: type, setup, punchline, id. 
     . Verificação dos tipos corretos:  string para type, setup, punchline e inteiro para id
     . Verificação de unicidade dos IDs em 100 repetições
   ## Teste de Carga
      . Simulação de 10 usuários simultâneos realizando requisições. 
      . Análise do tempo médio de respostas. 

## Execução dos Testes  
   ## Resultados Funcionais
      Durante a execução foi possível verificar um erro de ID duplicado pelo Pytest. 
        Evidências: reports/teste_funcional_id_duplicado.png
   ## Resultados de Carga
      Durante a simulação de 10 usuários simultâneos usando Locust, a API respondeu bem, mas foram observados variação de tempo
        Tempo médio de resposta: 641,99 ms
        Evidências: reports/teste_carga_tempo_medio.png

## Bugs Encontrados
  ID: 1

 Descrição: Retorno de ID duplicado após múltiplas requisições

 Severidade: Alta

 Passos para reprodução: 
     1. Realizar 100 requisições ao endpoint /random_joke  
     2. Observar a repetição de IDs

 Evidências: reports/teste_carga_tempo_medio.png

## Métricas Coletadas 
   Métrica: Valor
   N° de requisições testadas: 100
   N° de falhas encontradas 1 (ID duplicado)
   Taxa de sucesso: 99%
   Tempo médio de resposta: 641,99 ms

## Análise dos Resultados
A API retorna as informações com a estrutura e os tipos de dados corretos. No entanto, foi identificado um problema de duplicação de IDs em diferentes requisições, o que pode afetar usuários ou sistemas que precisam de IDs únicos. Em relação ao desempenho, o tempo médio de resposta ficou dentro do esperado para aplicações em produção, sem grandes variações mesmo com uma carga moderada.

## Ricos Identificados
. Riscos de inconsistência nos dados a IDs duplicados. 
. Potencial problema em sistemas que dependam de chave única. 

## Recomendação
. Revisar o mecanismo de geração de IDS únicos na API
. Implementar controle para garantir unicidade de retornar os dados. 
. Realizar testes com cargas maiores para validar escalabilidade.

     

