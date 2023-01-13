# Visão do produto

![](./piui_abacaxi.jpg)

## Elevator Pitch

O **piui** 
é **uma rede social** específica para 
o público **desenvolvedor de software**
que **permite a interação entre programadores**.

## Personas

- Programadores, desenvolvedores, engenheiros de software, etc.
- Pessoas que gostam de programar, mas não são profissionais da área.
- Pessoas que gostam de programar e querem aprender mais sobre a área.
- Pessoas que gostam de programar e querem compartilhar conhecimento.
- Pessoas que gostam de programar e querem se conectar com outros programadores.
- Público jovem (12+)
- Pessoas que gostam de games, animes, mangás, cultura geek, etc.

## Requisitos gerais

1. O sistema deve ser acessível via web (mobile ou navegador)
2. O sistema deve permitir que o usuário se registre e crie uma conta
3. Permite que os usuário possam postar conteúdo de programação
4. Permite que os usuário possam reagir a conteúdo que foi postado por outros usuários
5. Permite que os usuário possam comentar em conteúdo que foi postado por outros usuários
6. Permite que os usuário possam seguir outros usuários
7. Permite que os usuário possam criar comunidades e possam postar conteúdo nelas
8. Permite que os usuários vejam o engajamento  
99. Permite que os usuários possam cancelar a conta

## Requisitos específicos

### Detalhamento do requisito 2:

- 2.1 O sistema deve permitir que o usuário se registre e crie uma conta informando seu nome, nome de usuário (@), email, telefone, senha e data de nascimento.

### Detalhamento do requisito 3:
    
- 3.1 O sistema deve permitir que os usuários possam postar conteúdo de programação (em formato texto)
- 3.2 O usuário poderá postar projetos pessoais (link do github, por exemplo)
- 3.3 O usuário poderá postar dúvidas sobre programação
- 3.3 O usuário poderá postar dicas sobre programação
- 3.4 O usuário poderá postar links para conteúdos sobre programação
- 3.5 O usuário poderá postar trecho de código
- 3.6 O usuário poderá postar desafios de programação
- 3.7 O usuário poderá postar figuras relacionadas a programação
- 3.8 O usuário poderá postar vídeos relacionados a programação


### Detalhamento do requisito 4:

- 4.1 O usuário poderá reagir a um post com um emoji
- 4.2 O usuário poderá reagir a um post com um like
- 4.3 O usuário poderá reagir a um post com um dislike

## User Stories

### Stories do requisito específico 2.1
- Eu, **enquanto usuário**, quero me registrar no sistema 
informando meu nome, nome de usuário (@), email, telefone, senha e data de nascimento, 
**para que eu possa usar o sistema posteriormente**. 
   - Critério de aceite: Após o registro do usuário verificar que senha deve ser criptografada.
   - Critério de aceite: Após o registro do usuário verificar que o email deve ser único.
   - Critério de aceite: Após o registro do usuário verificar que o nome de usuário deve ser único.
   - Critério de aceite: Após o registro do usuário verificar que a data de nascimento deve ser válida.
   - Critério de aceite: Após o registro do usuário verificar que o email deve ser válido.
   - Critério de aceite: Após o registro do usuário verificar que o nome deve ser maior que 3 caracteres.
   - Critério de aceite: Após o registro do usuário verificar que a senha deve ser maior que 8 caracteres, contendo letras maículas, minúsculas e números.
   - Critério de aceite: Após o registro do usuário verificar que o email deve ser maior que 8 caracteres.
   - Critério de aceite: Após o registro do usuário verificar que a partir da data de nascimento que o usuário possui mais de 12 anos.
   - Critério de aceite: Após o registro do usuário verificar que o nome deve ser menor que 50 caracteres.
   - Critério de aceite: Após o registro do usuário verificar que o email deve ser menor que 50 caracteres.
   - Critério de aceite: Após o registro do usuário verificar que a senha deve ser menor que 50 caracteres.
   - Critério de aceite: Após o registro do usuário verificar que a data de nascimento deve ser menor que 130 anos.
   - Critério de aceite: Após o registro do usuário verificar que a senha deve ser válida.
   - Critério de aceite: Após o registro do usuário verificar que o telefone informado deve ser válido.
   - Critério de aceite: Após o registro do usuário verificar que o telefone deve ser maior que 10 caracteres e é numérico.

### Stories do requisito específico 3.2

- Eu, **enquanto usuário**, quero postar projetos pessoais, 
para que eu possa **divulgar o meu trabalho com outros usuários** 
de forma que o meu conteúdo chegue a mais pessoas e eu ganhe
engajamento na rede.

- Eu, **enquanto usuário**, quero postar projetos pessoais,
para que eu possa **receber feedback** de outros usuários
de forma que eu possa **melhorar o meu trabalho**.