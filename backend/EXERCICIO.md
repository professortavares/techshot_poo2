# Lista de exercícios de backend

## Exercício 1: 

1. Crie uma conta no github (caso não tenha)
2. Faça o fork do repositório https://github.com/professortavares/techshot_poo2
3. Crie uma branch de desenvolvimento para o exercício (ex. de nome: branch_exercicio_1)
4. Transforme o arquivo techshot/api/usuario.py em uma classe
5. Crie um arquivo test/api/test_usuario.py e crie os testes de unidade para os métodos da classe Usuario (que você criou no passo 4)
6. Faça o commit e o push da sua branch de desenvolvimento
7. Crie um pull request para a branch main do repositório

## Exercício 2:

1. Com base do código que você criou no exercício 1, crie uma nova branch de desenvolvimento (ex. de nome: branch_exercicio_2)
2. Crie um serviço para a classe InformacaoPessoal
3. Implemente as seguintes regras de negócio:
- A senha deve estar criptografada
- O usuário no momento do seu cadastro deve ter no mínimo 12 anos
4. Implemente os testes de unidade para o serviço
5. Altere o arquivo techshot/api/usuario.py para que ele utilize o serviço da classe InformacaoPessoal
6. Altere os testes de unidade para o arquivo techshot/api/usuario.py para que eles utilizem o serviço da classe InformacaoPessoal
7. Faça o commit e o push da sua branch de desenvolvimento
8. Crie um pull request para a branch main do repositório
