from random import randint
maquina = randint(0, 10)
print('-=-'*20)
print('TENTE ADIVINHAR O NUMERO QUE ESTOU PENSANDO DE 0 A 10...')
print('-=-'*20)
jogador = int(input('Qual número estou pensando de 0 a 10? '))

print('O número que eu escolhi foi {} ' .format(maquina))
if jogador == maquina:
    print('Parabéns, você acertou!!!')
else:
    print('Não foi dessa vez, eu pensei em {} e não no {} tente de novo!' .format(maquina, jogador))

print('-==-'*16)
#como eu pensei que iria funcionar  
