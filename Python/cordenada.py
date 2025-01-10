import os

def solicitar_cord():
    quadrante_x = int(input('Insira uma cordenada x:'))
    quadrante_y = int(input('Insira uma cordenada y:'))

    if quadrante_x > 0 and quadrante_y > 0:
        print('Você esta no primeiro quadrante')
    elif quadrante_x < 0 and quadrante_y > 0:
        print('Você esta no segundo quadrante')
    elif quadrante_x < 0 and quadrante_y < 0:
        print('Você esta no terceiro quadrante')
    elif quadrante_x > 0 and quadrante_y < 0:
        print('Você esta no quarto quadrante')
    else:
        print('O ponto está localizado no eixo ou origem')
    
def main(): 
    solicitar_cord()

if __name__ == '__main__':
    main()