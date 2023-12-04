def bienvenida():
    print('*' * 68)
    print('* Te doy la bienvenida al juego del ahorcado de codigopiton.com :) *')
    print('*' * 68)


def jugar_al_ahorcado(diccionario):

    tablero, palabra, letras_erroneas = inicializar_juego(diccionario)  # paso 1
    while len(letras_erroneas) < len(simbolos):  # pasos 7 y 8
        mostrar_escenario(len(letras_erroneas))  # paso 2
        mostrar_tablero(tablero, letras_erroneas)  # paso 3
        letra = pedir_letra(tablero, letras_erroneas)  # paso 4
        procesar_letra(letra, palabra, tablero, letras_erroneas)  # paso 5
        if comprobar_palabra(tablero):  # paso 6
            print('¡Enhorabuena, lo has logrado!')
            break
    else:
        print(f'¡Lo siento! ¡Has perdido! La palabra a adivinar era {palabra}.')
        mostrar_escenario(len(letras_erroneas))  # paso 7

    mostrar_tablero(tablero, letras_erroneas)


def jugar_otra_vez():
    return input('Deseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ')


def despedida():
    print('*' * 68)
    print('* Gracias por jugar al ahorcado de codigopiton.com. ¡Hasta pronto! *')
    print('*' * 68)


if __name__ == '__main__':

