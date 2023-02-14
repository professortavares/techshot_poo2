import hashlib

def codifica_senha(senha:str):
    return hashlib.sha3_256(senha.encode()).digest().hex()