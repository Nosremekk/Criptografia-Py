import hashlib;


#text = "Olá mundo!";
#obj_hash = hashlib.sha256(text.encode());
#hash_compilado = obj_hash.hexdigest();
#print("O hash do texto",text, "é ", hash_compilado);


def arquivo_hash(caminho):
    h = hashlib.new("sha256")
    with open(caminho,"rb") as arquivo:
        while True:
            chunk = arquivo.read(1024)
            if (chunk == b""):
                break
            h.update(chunk)
    return h.hexdigest()

def verificar_integridade(primeiro_arq,segundo_arq):
    hash1 = arquivo_hash(primeiro_arq)
    hash2 = arquivo_hash(segundo_arq)

    if (hash1 == hash2):
        return "Arquivo intacto, sem modificadores"
    else:
        return "Arquivo modificado, possivelmente inseguro"


if __name__ == "__main__":
    print("SHA Hash of file is: ", arquivo_hash(r"venv/sample files/sample.txt"))
    print(verificar_integridade(r"venv/sample files/novo_sample.txt",r"venv/sample files/sample.txt"))