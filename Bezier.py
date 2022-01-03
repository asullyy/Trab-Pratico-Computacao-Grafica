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



#--------------------------------------------------
def bresenham(x1, y1, x2, y2):
  #vetor que guarda os pontos iniciais que irão ser aplicados no alg de Bresenham
  ptIniciais = [x1, y1, x2, y2]

  print("\nPontos iniciais = ({},{}),({},{})\n".format(ptIniciais[0], ptIniciais[1], ptIniciais[2], ptIniciais[3]))

  #valores de delta para aplicarmos na condicação de teste da 1° octante
  deltaX = x2-x1
  deltaY = y2-y1
  
  #este vetor guardará os booleanos das trocas realizadas ou não na função de reflexão, para posteriormente fazer a reflexão para octante original.
  #boolsTroca[0] = trocaxy
  #boolsTroca[1] = trocax
  #boolsTroca[2] = trocay
  boolsTroca = [False, False, False]

  def reflexao(x1,y1,x2,y2):
    if deltaX != 0:
      m = deltaY/deltaX
    else:
      m = deltaY

    if m>1 or m<-1:
      print("fazendo troca de x->y\n")
      aux = 0
      #trocando os valores do par (x1,y1)
      aux = ptIniciais[0]
      ptIniciais[0] = ptIniciais[1]
      ptIniciais[1] = aux

      #trocando os valores do par (x2,y2)
      aux = ptIniciais[2]
      ptIniciais[2] = ptIniciais[3]
      ptIniciais[3] = aux
      boolsTroca[0] = True
    if x1>x2:
      print("fazendo reflexão em x1 e x2\n")
      ptIniciais[0] = ptIniciais[0]*(-1)
      ptIniciais[2] = ptIniciais[2]*(-1)
      boolsTroca[1]= True
    if y1>y2:
      print("fazendo reflexão em y1 e y2\n")
      ptIniciais[1] = ptIniciais[1]*(-1)
      ptIniciais[3] = ptIniciais[3]*(-1)
      boolsTroca[2] = True

  #verificando se os pontos estão na primeira condição, caso uma das condições seja satisfeita os pontos NÃO estão na primeira octante.
  if deltaX < deltaY or deltaX<0 or deltaY<0:
    reflexao(x1,y1,x2,y2)
    print("Pontos Refletidos = ({},{}),({},{})".format(ptIniciais[0], ptIniciais[1], ptIniciais[2], ptIniciais[3]))


  def algoritmoB(ptIniciais):
    x1 = ptIniciais[0]
    y1 = ptIniciais[1]
    x2 = ptIniciais[2]
    y2 = ptIniciais[3]

    m = (y2-y1)/(x2-x1)
    e = m - 0.5

    #esta variável guarda uma cópia do valor de y1, para incrementá-lo.
    aux = y1
    aux2 = x1

    #vetores que guardam os valores de y e x que foram calculados pelo alg de breseham 
    ptsY = [y1]
    ptsX = [x1]

    for i in range(int(x1), int(x2)):
      if e>0:
        aux+=1
        ptsY.append(aux)
        e-=1
      else:
        ptsY.append(aux)
      e=e+m
      
      aux2+=1
      ptsX.append(aux2)
    #boolsTroca[0] = trocaxy
    #boolsTroca[1] = trocax
    #boolsTroca[2] = trocay
    if boolsTroca[0] == True:
        aux = ptsX
        ptsX = ptsY
        ptsY = aux
    if boolsTroca[1] == True:
      for i in range(0, len(ptsY)):
        ptsX[i] = ptsX[i]*-1
    if boolsTroca[2] == True:
      for i in range(0, len(ptsY)):
        ptsY[i] = ptsY[i]*-1
    return [ptsX, ptsY]
  
  paresOrdenados = algoritmoB(ptIniciais)
  
  return paresOrdenados

#--------------------------------------------------------

pixels = algBezier()
pontosX = pixels[0]
pontosY = pixels[1]

'''
#PRINTANDO COM BRESENHAM
for i in range(0, len(pontosX)-1):
  aux = bresenham(pontosX[i], pontosY[i], pontosX[i+1], pontosY[i+1])
  aux_x = aux[0]
  aux_y = aux[1]
  for i in range(len(aux_x)):
    DesenharPixel(aux_x[i],aux_y[i], '#f00')
'''
#PRINTANDO SEM BRESENHAM
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