import random as rd
import hashlib

print ("                      Bem vindo ao Seed Generator                   ")
print (           "Escolha uma das seguintes opções digite (12) ou (24)"             )

quantidade = int (input("Você quer uma Seed de quantas palavras? : " ""))

#Para abrir a wordlist em txt
with open('wordlist.txt', 'r', encoding='utf-8') as file:
#Ler arquivo e converter cada item em uma lista
    palavras = file.read().splitlines()


#Gerar entropia aleatória
if quantidade == 12:
    entropia_bits = 128
elif quantidade == 24:
    entropia_bits = 256
else:
    raise ValueError("Erro: quantidade de palavras deve ser 12 ou 24")


# Gerar entropia aleatória com o número correto de bits
entropia = rd.getrandbits(entropia_bits)
entropia_bin = bin(entropia)[2:].zfill(entropia_bits)

# Calcular o checksum 
checksum = hashlib.sha256(entropia.to_bytes(entropia_bits // 8, byteorder='big')).hexdigest()
checksum_bits = bin(int(checksum, 16))[2:].zfill(256)

# Determinar o número de bits do checksum a serem usados
checksum_length = entropia_bits // 32
entropia_completa = entropia_bin + checksum_bits[:checksum_length]

# Dividir em grupos de 11 bits
indices_final = [int(entropia_completa[i:i + 11], 2) for i in range(0, len(entropia_completa), 11)]
palavras_final = [palavras[indice] for indice in indices_final]

# Exibir as palavras finais
print("Palavras geradas (seed):", " ".join(palavras_final))

# Chave estendida (opcional)
chave_estendida = hashlib.sha512(entropia_completa.encode()).hexdigest()
print("Chave estendida (opcional):", chave_estendida)