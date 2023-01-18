from datetime import datetime

from techshot.entidades import Usuario
from techshot.entidades import InformacaoPessoal

if __name__ == '__main__':
    usuario = Usuario('Fulano de Tal', '@fulano')
    print(usuario)
    print(usuario.nome_usuario)
    print(usuario.nome)
    print(usuario.informacoes_pessoais)
    info = InformacaoPessoal(email='a@a.com',
                             telefone='(11) 99999-9999',
                             senha='123456',
                             data_nascimento=datetime.now())

    usuario.informacoes_pessoais = info
    print('#'*20)
    print(usuario.informacoes_pessoais)
    print(usuario.informacoes_pessoais.email)
    print(usuario.informacoes_pessoais.telefone)
    print(usuario.informacoes_pessoais.senha)
    print(usuario.informacoes_pessoais.data_nascimento)



