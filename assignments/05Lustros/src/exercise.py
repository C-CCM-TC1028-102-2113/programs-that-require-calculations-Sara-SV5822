def main():
  #escribe tu código abajo de esta línea
  born=int(input('Dame el año de nacimiento: '))
  now=int(input('Dame el año actual'))

  lustro= (now-born)/5

  print('Los lustros que has vivido son: '+ str(lustro))

if __name__ == '__main__':
    main()
