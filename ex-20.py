import math

areapint=int(input('Informe a area para pintura em m2: '))

qtdtint=(areapint/6)*1.1

qtdlata=qtdtint/18
qtdlataint=qtdtint//18
latas=qtdlataint+math.ceil(qtdlata-qtdlataint)
#qtdlatmet=qtdtint%18

qtdgalo=qtdtint/3.6
qtdgaloint=qtdtint//3.6
galoes=qtdgaloint+math.ceil(qtdgalo-qtdgaloint)
#qtdgalmet=qtdtint%3.6

print('a) latas: {}'.format(latas,))
print('b) galoes: {}'.format(qtdgaloint))

galoes2=math.ceil(((qtdlata-qtdlataint)*18)/3.6)
print('c) latas: {}, galoes: {}'.format(qtdgaloint,galoes2))
