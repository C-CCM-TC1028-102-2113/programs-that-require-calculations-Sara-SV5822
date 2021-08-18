def main():
  #escribe tu código abajo de esta línea
  w_i=float(input('Dame el peso inicial: '))
  w_f=float(input('Dame el peso final: '))
  mes=int(input('Dame la cantidad de meses: '))

  w_m=float((w_i-w_f)/mes)

  print('Lo que debes bajar por mes es: '+ str(w_m))

if __name__ == '__main__':
    main()
