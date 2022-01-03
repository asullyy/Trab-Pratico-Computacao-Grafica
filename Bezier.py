import numpy as np
from tkinter import *

## parametros iniciais
tamanhoTela = 600 
tamanhoPixel = int(tamanhoTela / 50)

## criar o canvas utilizando o tkinter
master = Tk()
tela = Canvas(master, width=tamanhoTela, height=tamanhoTela)
tela.pack()

## função que cria a grade
def CriarTemplate():
  aux = int(tamanhoTela / 2) + (tamanhoPixel / 2)

  for x in range(0, tamanhoTela, tamanhoPixel): # linhas horizontais
    tela.create_line(x, 0, x, tamanhoTela, fill='#808080')

  for y in range(0, tamanhoTela, tamanhoPixel): # linhas horizontais
    tela.create_line(0, y, tamanhoTela, y, fill='#808080')

  tela.create_line(0, aux - tamanhoPixel, tamanhoTela, aux - tamanhoPixel, fill="#f00") # linha central - horizontal
  tela.create_line(aux, 0, aux, tamanhoTela, fill="#f00") # linha central - vertical

def ConverterCoordenadas(x, y): # converter coordenadas para o sistema de grade
  real_x = int((tamanhoPixel * x) + (tamanhoTela / 2))
  real_y = int((tamanhoTela / 2) - (tamanhoPixel * y))

  return real_x, real_y

def DesenharPixel(x, y, cor): # desenha um pixel na grade
  x1, y1 = ConverterCoordenadas(x, y)
  tela.create_rectangle(x1, y1, x1 + tamanhoPixel, y1 - tamanhoPixel, fill=cor)

#-------------------------------------------------------
def algBezier():
  #os vetores abaixo guardarão as coordenadas dos pontos de controle

  coord_X = []
  coord_Y = []

  #a variável n guardará o número de pontos de controle
  n = int(input("Digite o número de pontos de controle(inclusos os pontos inicial e final): "))


  #dentro deste laço serão coletados as coordenadas dos pontos de controle, sendo o primeiro o ponto inicial e o último o ponto final
  for i in range(0,n):
    print("ponto {}".format(i))
    x = int(input("x: "))
    coord_X.append(x)
    y = int(input("y: "))
    coord_Y.append(y)

  #A função recursiva B, recebe como parametro uma lista (lista de de coordenadas), a 1° posição de um vetor, o n° de pontos e um instante t
  def B(coorArr, i, n, t):
    
      if n == 0:
          aux = coorArr[i]
          return aux
      else:
        aux = B(coorArr, i, n-1, t) * (1-t) + B(coorArr, i+1, n-1, t) * t
      
      return aux
        
  #o algoritmo Bezier recebe como parametro o n° de pontos de controle
  def Bezier(n):
    #os vetores guardarão os pontos X e Y calculados.
    ptsX = []
    ptsY = []
    #usamos a biblioteca numpy para contagem de instantes de 0 até 1. O intervalo foi definido de 0 até 1.1 para que o 1 também fosse usado.
    for t in np.arange(0, 1.1, 0.1):
      x = B(coord_X, 0, n - 1, t)
      #usamos o round(x,2) para definir quantas casas decimais terão nosso número, nesse caso, 2.
      ptsX.append(round(x, 2))
      y = B(coord_Y, 0, n - 1, t)
      ptsY.append(round(y,2))
    return [ptsX, ptsY]
  pts = Bezier(n)
  return pts

pixels = algBezier()
pontosX = pixels[0]
pontosY = pixels[1]

for i in range(len(pontosX)):
  DesenharPixel(pontosX[i],pontosY[i], '#f00')
CriarTemplate()
mainloop()

'''
pontos testes:
p0 = (-10,-10)
p1 = (-5,10)
p2 = (5,10)
p3 = (10, -10)
'''