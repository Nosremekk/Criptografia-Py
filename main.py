#!/usr/bin/env python3
from modules.hash import arquivo_hash, verificar_integridade
from modules.encryption import aes_ed, rsa_ed
from modules.password import checar_seguranca, hash_senha, verifica_senha
from getpass import getpass

def menu():
    print("\nSelecione a operação: ")
    print("1. Criptografar arquivo (Integridade/Hash)")
    print("2. Checar integridade de arquivo")
    print("3. Criptografia AES chave/fechadura")
    print("4. Criptografia RSA chave/fechadura")
    print("5. Testar e gerenciar senha")
    print("0. Exit")

print("Bem Vindo a Caixa de Ferramentas da Criptografia! \n")

if __name__ == "__main__":
    while True:
        menu()
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                caminho = input("Digite o caminho do arquivo para gerar o hash: ")
                try:
                    resultado = arquivo_hash(caminho)
                    print("Hash SHA-256 do arquivo:", resultado)
                except Exception as e:
                    print("Erro ao processar o arquivo:", e)

            case "2":
                arq1 = input("Digite o caminho do primeiro arquivo: ")
                arq2 = input("Digite o caminho do segundo arquivo: ")
                try:
                    resultado = verificar_integridade(arq1, arq2)
                    print("Resultado:", resultado)
                except Exception as e:
                    print("Erro ao verificar integridade:", e)

            case "3":
                mensagem = input("Digite a mensagem para criptografar com AES: ")
                chave, texto_cifrado, texto_plano = aes_ed(mensagem)
                print("Chave Hex:", chave)
                print("Texto Cifrado:", texto_cifrado)
                print("Texto Plano Recuperado:", texto_plano)

            case "4":
                mensagem = input("Digite a mensagem para criptografar com RSA: ")
                texto_cifrado, texto_plano = rsa_ed(mensagem)
                print("Texto Cifrado:", texto_cifrado)
                print("Texto Plano Recuperado:", texto_plano)

            case "5":
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
                print("Senha criptografada com Bcrypt: ", senha_criptografada.decode())
                
                tentativa = getpass("Coloque novamente sua senha para verificar: ")
                print(verifica_senha(tentativa, senha_criptografada))

            case "0":
                print("Saindo da Caixa de Ferramentas. Até logo!")
                break

            case _:
                print("Opção inválida! Escolha um número entre 0 e 5.")