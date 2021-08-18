def main():
  #escribe tu código abajo de esta línea
  cal_1=float(input('Calificación de la materia: '))
  cal_2=float(input('Calificación de la materia: '))
  cal_3=float(input('Calificación de la materia: '))
  cal_4=float(input('Calificación de la materia: '))

  prom=(cal_1+cal_2+cal_3+cal_4)/4

  print('El promedio es: '+ str(prom))

if __name__ == '__main__':
    main()
