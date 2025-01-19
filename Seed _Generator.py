import random as rd
import hashlib

print ("                      Welcome to Seed Generator                   ")
print (           "Choose one of the following options type (12) or (24)"             )

quantidade = int (input("How many words do you want a Seed ? : " ""))

#to open wordlist in txt
with open('wordlist.txt', 'r', encoding='utf-8') as file:

    palavras = file.read().splitlines() #.txt to list


#Random entropy 
if quantidade == 12:
    entropia_bits = 128
elif quantidade == 24:
    entropia_bits = 256
else:
    raise ValueError("Error: number of words should be 12 or 24")


# Generate random entropy with the correct number of bits
entropia = rd.getrandbits(entropia_bits)
entropia_bin = bin(entropia)[2:].zfill(entropia_bits)

# Calcular o checksum 
checksum = hashlib.sha256(entropia.to_bytes(entropia_bits // 8, byteorder='big')).hexdigest()
checksum_bits = bin(int(checksum, 16))[2:].zfill(256)

#Determine the number of checksum bits to use
checksum_length = entropia_bits // 32
entropia_completa = entropia_bin + checksum_bits[:checksum_length]

#Split into groups of 11 bits
indices_final = [int(entropia_completa[i:i + 11], 2) for i in range(0, len(entropia_completa), 11)]
palavras_final = [palavras[indice] for indice in indices_final]


print("Your words (seed):", " ".join(palavras_final))

# Generate a extended Key (optional)
chave_estendida = hashlib.sha512(entropia_completa.encode()).hexdigest()
print("Extended Key (optional):", chave_estendida)