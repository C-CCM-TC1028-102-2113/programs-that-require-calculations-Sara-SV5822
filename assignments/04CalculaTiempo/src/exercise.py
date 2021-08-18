def main():
  #escribe tu código abajo de esta línea
  edad=int(input('Dame tu edad: '))
  year=int(input('Dame el año actual: '))

  resultado= int((100-edad)+year)

  print('Cumplirás 100 años en el año: '+ str(resultado))

if __name__ == '__main__':
    main()
