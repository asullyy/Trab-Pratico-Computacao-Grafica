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

def bresenham(x1,y1,x2,y2):
  #tratando casos de entrada: para os casos como (1,4),(1,1), observou-se que a ordem dos vertices deve estar de forma crescente para o bom funcionamento do algoritmo. Bem como para os casos como: (4,4), (4,1). Por isso faremos o tratamento de entradas abaixo colocando os vértices em ordem crescente nesses casos.

  if x1 == x2:
    if y1>y2:
      ptIniciais = [x2, y2, x1, y1]
    if y2>y1:
      ptIniciais = [x1, y1, x2, y2]

  if y1 == y2:
    if x1>x2:
      ptIniciais = [x2, y2, x1, y1]
    if x2>x1:
      ptIniciais = [x1, y1, x2, y2]

  if x1 != x2 and y1 != y2:
    ptIniciais = [x1, y1, x2, y2]

  #valores de delta para aplicarmos na condicação de teste da 1° octante
  deltaX = ptIniciais[2] - ptIniciais [0]
  deltaY = ptIniciais[3] - ptIniciais[1]
  
  #este vetor guardará os booleanos das trocas realizadas ou não na função de reflexão, para posteriormente fazer a reflexão para octante original.
  #boolsTroca[0] = trocaxy
  #boolsTroca[1] = trocax
  #boolsTroca[2] = trocay
  boolsTroca = [False, False, False]

  def reflexao():
    
    if deltaX != 0 and deltaY != 0:
      m = deltaY/deltaX
    else:
      if deltaX == 0:
        m = deltaY
      if deltaY == 0:
        m = 0
   
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
    reflexao()
    print("Pontos Refletidos = ({},{}),({},{})".format(ptIniciais[0], ptIniciais[1], ptIniciais[2], ptIniciais[3]))


  def algoritmoB(ptIniciais):
    
    x1 = ptIniciais[0]
    y1 = ptIniciais[1]
    x2 = ptIniciais[2]
    y2 = ptIniciais[3]

    deltaX = x2-x1
    deltaY = y2-y1

    if deltaX != 0 and deltaY != 0:
      m = deltaY/deltaX
    else:
      if deltaX == 0:
        m = deltaY
      if deltaY == 0:
        m = 0

    e = m - 0.5

    #esta variável guarda uma cópia do valor de y1, para incrementá-lo.
    aux = y1
    aux2 = x1

    #vetores que guardam os valores de y e x que foram calculados pelo alg de breseham 
    ptsY = [y1]
    ptsX = [x1]
    
    maxX = max(int(x1), int(x2))
    minX = min(int(x1), int(x2))

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
  
    #boolsTroca[0] = trocaxy
    #boolsTroca[1] = trocax
    #boolsTroca[2] = trocay
    
    if boolsTroca[2] == True:
      print("\nreflexão inversa y")
      for i in range(0, len(ptsY)):
        ptsY[i] = ptsY[i]*-1

    if boolsTroca[1] == True:
      print("\nreflexão inversa x")
      for i in range(0, len(ptsY)):
        ptsX[i] = ptsX[i]*-1

    if boolsTroca[0] == True:
        print("\nreflexão inversa x->y")
        aux = ptsX
        ptsX = ptsY
        ptsY = aux
        
    return [ptsX, ptsY]
  
  paresOrdenados = algoritmoB(ptIniciais)
  
  return paresOrdenados

#-----------Polilinhas---------------------------
n = int(input("Digite o número de vértices: "))

#coletando os vértices
ptsX = []
ptsY = []
for i in range(1,n+1):
  print("ponto {}".format(i))
  x = int(input("x: "))
  ptsX.append(x)
  y = int(input("y: "))
  ptsY.append(y)

for i in range(0, n-1):
  pixels = bresenham(ptsX[i], ptsY[i], ptsX[i+1], ptsY[i+1])
  pontosX = pixels[0]
  pontosY = pixels[1]
  for i in range(len(pontosX)):
    DesenharPixel(pontosX[i],pontosY[i], '#ff66b2')

#combinando o último ponto e o primeiro ponto
pixels = bresenham(ptsX[0], ptsY[0], ptsX[n-1], ptsY[n-1])
pontosX = pixels[0]
pontosY = pixels[1]
for i in range(len(pontosX)):
  DesenharPixel(pontosX[i],pontosY[i], '#ff66b2')
"""
DesenharPixel(6, 5, '#f00')
DesenharPixel(5, 7, '#f00')
DesenharPixel(5, 3, '#f00')
"""
CriarTemplate()
mainloop()

#-------------------------------------#
'''
PONTOS TESTE - FORMULADO:
P1 = (1,4)
P2 = (1,1)
P3 = (4,1)
P4 = (4,4)
'''