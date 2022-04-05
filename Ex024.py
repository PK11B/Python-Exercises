# Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra "Santo".

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('Começa com Santo: {}'.format("santo" in cidade[:5].lower()))

# procura = 'santo' in cidade
# 
# if procura == True:
#   print('A cidade começa com Santo')
# else:
#   print('A cidade não começa com Santo')