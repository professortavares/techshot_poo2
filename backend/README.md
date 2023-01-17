# DEV.: 

1. Crie o ambiente virtual do projeto:
> python3 -m venv venv

2. Ative o ambiente virtual:
> . venv/bin/activate

Se você estiver usando o Windows, use:
> venv\Scripts\activate

Para desativar o ambiente virtual, use:
> deactivate

4. Instale as dependências do projeto:
> pip install -r requirements.txt

E então instale o projeto:
> pip install -e .

Para atualizar as dependências do projeto, use:
> pip install --upgrade --force-reinstall -r requirements.txt

5. Para executar os testes de unidade, use:
> pytest

Para cobertura de código, use:
> pytest --cov=techshot_poo --cov-report html:cov_html
