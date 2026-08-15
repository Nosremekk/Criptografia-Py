import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes

#Criptografando simetricos
def aes_ed(mensagem):
    chave = secrets.token_bytes(32)
    init_vec = secrets.token_bytes(12)
    aes = AESGCM(chave)

    chipertexto = init_vec + aes.encrypt(init_vec,mensagem.encode(),None)
    plaintexto = aes.decrypt(chipertexto[:12],chipertexto[12:],None)
    return chave.hex(), chipertexto.hex(), plaintexto.decode()

#Criptografia assimetrica
def rsa_ed(mensagem):
    chave_particular = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    chave_publica = chave_particular.public_key()
    chipertexto = chave_publica.encrypt(
        mensagem.encode(),
        padding.OAEP(
            mgf= padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    plaintexto = chave_particular.decrypt(
        chipertexto,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return chipertexto.hex(), plaintexto.decode()

if __name__ == "__main__":
    print(aes_ed("Olá Mundo!"))
    print(rsa_ed("Olá Mundo, seguro!"))

