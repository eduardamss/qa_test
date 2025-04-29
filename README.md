#QA-Challenge: Testando a API de Piadas

## Sobre o projeto

Este desafio realiza testes funcionas e de carga na API de piadas apresentadas na url https://official-joke-api.appspot.com/random_joke

URL: https://official-joke-api.appspot.com/random_joke

## Passos do projeto
  ## Como rodar
  1. criar ambiente virtual: 
      python -m venv venv

  2. Ativar o Ambiente: 
     venv\Scripts\activate

  3.Instalar dependências:
     pip install requests pytest locust

  4. Execute testes funcionais (Pytest):
     pytest tests/test_piada.py --maxfail=1 --disable-warnings -v

  5. Executar Teste de Carga (Locust)
    locust -f locustfile.py
    http://localhost:8089
        Prencha: 
           .Number: 10
           . Spawn rate: 2
           .Host: https://official-joke-api.appspot.com
        
## Dependências
- Python 3.8+
- pytest
- requests
- locust

## Premissas
- A API deve retornar JSON válido.
- Todos os campos obrigatórios devem estar preenchidos.
- Tempo de resposta deve ser inferior a 2s para 95% dos casos.

## Contribuidora
   . Maria Eduarda Silva
