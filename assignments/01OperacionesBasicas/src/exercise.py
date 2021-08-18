def main():
    #escribe tu código abajo de esta línea
  num_1=int(input('Introduce un número: '))
  num_2=int(input('Introduce un número: '))

  suma=num_1+num_2
  resta=num_1-num_2
  mult=num_1*num_2

  mensaje='''Suma= {}
  Resta= {}
  Multiplicación= {}'''

  print(mensaje.format(suma,resta,mult))
    
    pass


if __name__ == '__main__':
    main()
