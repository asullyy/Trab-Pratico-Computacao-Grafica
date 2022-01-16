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
#----------------------POLILINHAS-----------------------
def Bresenham (xInicial, yInicial, xFinal, yFinal):

  pontos = [xInicial, yInicial, xFinal, yFinal]

  #bool_reflexao [0] = trocaX
  #bool_reflexao [1] = trocaY
  #bool_reflexao [2] = trocaXY
  bool_reflexao = [False, False, False]
  
  def reflexao(m):
    if xInicial>xFinal:
      bool_reflexao[0] = True
      if xInicial != 0:
        pontos[0] = xInicial*(-1)
      if xFinal != 0:
        pontos[2] = xFinal*(-1)

    if yInicial>yFinal:
      bool_reflexao[1] = True
      if yInicial != 0:
        pontos[1] = yInicial*(-1)
      if yFinal != 0:
        pontos[3] = yFinal*(-1)

    if m>1 or m<-1:
      bool_reflexao[2] = True
      aux = pontos[0]
      pontos[0] = pontos[1]
      pontos[1] = aux

      aux = pontos[2]
      pontos[2] = pontos[3]
      pontos[3] = aux

  def calculaBresenham(pontos):
    xInicial = pontos[0]
    yInicial = pontos[1]
    xFinal = pontos[2]
    yFinal = pontos[3]

    deltaX = xFinal - xInicial 
    deltaY = yFinal - yInicial

    if deltaX == 0:
      m = deltaY
      #não existe divisão por zero, assim m será igual a deltaY
    if deltaY == 0:
      m = 0;
      #todo número dividido por zero é igual a 0
    if deltaY and deltaX != 0:
      m = deltaY/deltaX

    e = m - 0.5

    #estas variáveis guardam uma cópia do valor de yInicial e xInicial para incrementá-los.
    aux = yInicial
    aux2 = xInicial

    #vetores que guardam os valores de y e x que foram calculados pelo alg de breseham 
    ptsY = [yInicial]
    ptsX = [xInicial]

    maxX = max(int(xInicial), int(xFinal))
    minX = min(int(xInicial), int(xFinal))

    for i in range(minX, maxX):
      if e>0:
        aux+=1
        ptsY.append(aux)
        e-=1
      else:
        ptsY.append(aux)

      e=e+m
      aux2+=1
      ptsX.append(aux2)
    
   
    return(ptsX, ptsY)

  def reflexaoInversa(pontos):
    ptsX = pontos[0]
    ptsY = pontos[1]

    if bool_reflexao[2] == True:
      aux = ptsX
      ptsX = ptsY
      ptsY = aux

    if bool_reflexao[1] == True:
      for i in range(0, len(ptsY)):
        ptsY[i] = ptsY[i]*(-1)
  
    if bool_reflexao[0] == True:
      for i in range(0, len(ptsX)):
        ptsX[i] = ptsX[i]*(-1)
    
    return(ptsX, ptsY)
    

  #1° PASSO: calcular deltaX, delta Y e m;
  deltaX = xFinal - xInicial 
  deltaY = yFinal - yInicial
  
  if deltaX == 0:
    m = deltaY
    #não existe divisão por zero, assim m será igual a deltaY
  if deltaY == 0:
    m = 0;
    #todo número dividido por zero é igual a 0
  if deltaY != 0 and deltaX != 0:
    m = deltaY/deltaX
  
  #verificar se os pontos estão na 1° octante. Caso não estejam, aplica-se a reflexão.
  if deltaX<deltaY or deltaX<0 or deltaY<0:
    reflexao(m)

  #2° PASSO: aplicar o algoritmo de Bresenham
  b_pontos = calculaBresenham(pontos)

  #3° PASSO: aplicar a reflexão reversa caso necessário
  pontosFinais =  reflexaoInversa(b_pontos)

  return pontosFinais

#-----------Polilinhas---------------------------
def polilinhas(n, ptsX, ptsY):
  for i in range(0, n-1):
    pixels = Bresenham(ptsX[i], ptsY[i], ptsX[i+1], ptsY[i+1])
    pontosX = pixels[0]
    pontosY = pixels[1]
    for i in range(len(pontosX)):
      DesenharPixel(pontosX[i],pontosY[i], '#f00')

  #combinando o último ponto e o primeiro ponto
  pixels = Bresenham(ptsX[0], ptsY[0], ptsX[n-1], ptsY[n-1])
  pontosX = pixels[0]
  pontosY = pixels[1]
  for i in range(len(pontosX)):
    DesenharPixel(pontosX[i],pontosY[i], '#f00')

#---------------------------VARREDURA------------------------
def varredura():
  nVertices = int(input("Digite o número de vértices: "))

  #coletando os vértices
  ptsX = []
  ptsY = []
  for i in range(1,nVertices+1):
    print("ponto {}".format(i))
    x = float(input("x: "))
    ptsX.append(x)
    y = float(input("y: "))
    ptsY.append(y)

  Ymin = int(min(ptsY))
  Ymax = int(max(ptsY))

  #Chamando o polilinhas para desenhar o polígono
  polilinhas(nVertices, ptsX, ptsY)

  #1° PASSO: achar os valores de Ymax, Ymin, Xymin e m/1
  dadosArestas = []

  for i in range(0, nVertices):
    aux = []
    if i == nVertices-1:
      x1 = ptsX[i]
      y1 = ptsY[i]
      x2 = ptsX[0]
      y2 = ptsY[0]

    else:
      x1 = ptsX[i]
      y1 = ptsY[i]
      x2 = ptsX[i+1]
      y2 = ptsY[i+1]

    #Ymax
    aux.append(max(y1,y2))

    #Ymin e Xymin
    if y1<y2:
      aux.append(y1)
      aux.append(x1)
    else:
      aux.append(y2)
      aux.append(x2)

    #m
    deltaX = x2 - x1
    deltaY = y2 - y1

    if deltaX == 0:
      m = deltaY
      #não existe divisão por zero, assim m será igual a deltaY
    if deltaY == 0:
      m = 0;
      #todo número dividido por zero é igual a 0
    if deltaY and deltaX != 0:
      m = deltaY/deltaX

    if m != 0:
      aux.append(round(1/m, 3))
    else:
      aux.append(0)

    dadosArestas.append(aux)


  #2° PASSO: Iniciar a varredura para os valores de Yvarredura. 
  X = []
  Y = []
  #intervalo da varredura é de 0 até o valor máximo de y das arestas.
  for i in range(Ymin+1, Ymax):
    aux = []
    for j in dadosArestas:
      if i>=j[1] and i<=j[0]:
        x = j[3]*(i-j[1])+j[2]
        if x not in aux:
          aux.append(x)
    aux.sort()
    X.append(aux)
    Y.append(i)

  return [X,Y]

pontos = varredura()
ptsX = pontos[0]
ptsY = pontos[1]

for i in range(0,len(ptsY)):
  y = ptsY[i]
  x = ptsX[i]

  if len(x)%2 == 0:
    for j in range(0, len(x), 2):
      for k in range(round(x[j])+1, round(x[j+1])):
          DesenharPixel(k, y, '#ff66b2')
  if len(x)%3 == 0:
    for j in range(0,len(x)-1):
      for k in range(round(x[j])+1, round(x[j+1])):
          DesenharPixel(k, y, '#ff66b2')
      

CriarTemplate()
mainloop()
"""
#EXEMPLO:
P1(0,8)
P2(3,1)
P3(5,6)
P4(9,1)
P5(10,10)

#ORIENTAÇÕES:
Insira o número de vertices do seu polígono e em seguite digite suas coordenadas.
"""