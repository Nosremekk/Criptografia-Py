from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def checar_seguranca(senha):
    resultado = zxcvbn(senha)
    pontuacao = resultado["score"]
    if pontuacao == 3:
        return "Forte o suficiente, pontuação de 3"
    elif pontuacao == 4:
        return "Senha muito forte! pontuação de 4"
    else:
        feedback = resultado.get("feedback", {})
        alerta = feedback.get("warning", "")
        sugestoes = feedback.get("suggestions", [])
        resposta = "Fraca, pontuação de " + str(pontuacao)
        if alerta:
            resposta += "\nAlerta: " + alerta
        if sugestoes:
            resposta += "\nSugestão:"
            for sugestao in sugestoes:
                resposta += " " + sugestao
        return resposta

def hash_senha(senha):
    salt = bcrypt.gensalt()
    criptografado = bcrypt.hashpw(senha.encode(), salt)
    return criptografado

def verifica_senha(senha_tentada, criptografado):
    if bcrypt.checkpw(senha_tentada.encode(), criptografado):
        return "Senha correta, acesso liberado!"
    else:
        return "Incorreto, acesso negado."

if __name__ == "__main__":
    while True:
        senha1 = getpass("Coloque a senha para testar a segurança: ")
        resultado_teste = checar_seguranca(senha1)
        print(resultado_teste)
        if resultado_teste.startswith("Fraca"):
            print("Escolha uma senha mais forte.\n")
        else:
            print("Senha aceita!\n")
            break    

    senha_criptografada = hash_senha(senha1)
    print("Senha criptografada: ", senha_criptografada)
    
    tentativa = getpass("Coloque novamente sua senha para verificar: ")
    print(verifica_senha(tentativa, senha_criptografada))