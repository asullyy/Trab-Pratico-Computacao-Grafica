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

#------------------alg círculo-------------------
def circulo ():
  #recebendo as entradas
  raio = int(input("Digite o raio: "))
  x_central = int(input("Digite x: "))
  y_central = int(input("Digite y: "))

  #a função algoritmo recebe como parametro o raio, e as coord centrais.
  def algoritmo(raio):
    #vetore onde será guardado os valores de x; este inicia na origem (0) e vai até o raio. Logo, faremos um laço para preenchê-lo de 0 até o raio
    ptsX = []
    for i in range(0, raio):
      ptsX.append(i)

    #os valores de y, por sua vez, são calculados pelo algoritmo
    ptsY = [raio]

    x = 0
    y = raio
    e = raio*(-1)

    while x<=y:
      e+=(2*x)+1
      x+=1
      if e>=0:
        e+=2-(2*y)
        y-=1
        ptsY.append(y)
      else:
        ptsY.append(y)

    return [ptsX, ptsY]
  
  pts = algoritmo(raio)

  #a função desenha8 refletirá os pontos para cada octante

  def desenha8(list, x, y):
    total_ptsX = []
    total_ptsY = []

    ptsX = list[0]
    ptsY = list[1]
    
    #---------------Octante 1---------------
    for i in range(len(ptsX)):
      ptX = ptsX[i]+x
      total_ptsX.append(ptX)
      ptY = ptsY[i]+y
      total_ptsY.append(ptY)

    #---------------Octante 2---------------
    for i in range(len(ptsX)):
      ptX = ptsY[i]+x  
      total_ptsX.append(ptX)
      ptY = ptsX[i]+y
      total_ptsY.append(ptY)
  
    #---------------Octante 3---------------
    for i in range(len(ptsX)):
      ptX = ptsY[i]+x  
      total_ptsX.append(ptX)
      ptY = (ptsX[i]*-1)+y
      total_ptsY.append(ptY)

    #---------------Octante 4---------------
    for i in range(len(ptsX)):
      ptX = ptsX[i]+x  
      total_ptsX.append(ptX)
      ptY = (ptsY[i]*-1)+y
      total_ptsY.append(ptY)

    #---------------Octante 5---------------
    for i in range(len(ptsX)):
      ptX = (ptsX[i]*-1)+x  
      total_ptsX.append(ptX)
      ptY = (ptsY[i]*-1)+y
      total_ptsY.append(ptY)

    #---------------Octante 6---------------
    for i in range(len(ptsX)):
      ptX = (ptsY[i]*-1)+x  
      total_ptsX.append(ptX)
      ptY = (ptsX[i]*-1)+y
      total_ptsY.append(ptY)

    #---------------Octante 7---------------
    for i in range(len(ptsX)):
      ptX = (ptsY[i]*-1)+x  
      total_ptsX.append(ptX)
      ptY = ptsX[i]+y
      total_ptsY.append(ptY)

    #---------------Octante 8---------------
    for i in range(len(ptsX)):
      ptX = (ptsX[i]*-1)+x  
      total_ptsX.append(ptX)
      ptY = ptsY[i]+y
      total_ptsY.append(ptY)
    return[total_ptsX, total_ptsY]
  return desenha8(pts, x_central, y_central)

pixels = circulo()

ptX = pixels[0]
ptY = pixels[1]

for i in range(0, len(ptX)):
  DesenharPixel(pixels[0][i], pixels[1][i], '#f00')

CriarTemplate()
mainloop()

'''
PONTOS TESTE - AULA GUSTAVO RESQUE:
RAIO = 5
PONTOS = (6,3)
'''