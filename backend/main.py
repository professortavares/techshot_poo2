from techshot.entidades import Usuario

if __name__ == '__main__':
    usuario = Usuario('Fulano de Tal', '@fulano')
    print(usuario)
    print(usuario.nome_usuario)
    print(usuario.nome)
    print(usuario.informacoes_pessoais)



