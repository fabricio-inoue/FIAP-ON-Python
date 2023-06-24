inventario = []
def preencherInventario(lista):
  resp="S"
  while resp == "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    lista.append(equipamento)
    resp = input('Digite "S" para continuar: ').upper()

def exibirInventario(lista):
  for elemento in lista:
    print('Nome: ', elemento[0])
    print('Valor: ', elemento[1])
    print('Serial: ', elemento[2])
    print('Departamento: ', elemento[3])

def localizarPorNome(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor: ", elemento[1])
            print("Serial: ", elemento[2])

def depreciarPorNome(lista):
    depreciacao = input('Digite o nome do elemento a ser depreciado: ')
    for elemento in lista:
       if depreciacao==elemento[0]:
        print('Valor original: ', elemento[1])
        elemento[1] = elemento[1] * 0.9
        print('Valor novo: ', elemento[1])

def excluirPorSerial(lista):
   serial = input('Digite o serial a ser excluído: ')
   for elemento in lista:
      if elemento[2] == serial:
         inventario.remove(elemento)

def resumirValores(lista):
    valores = []
    for elemento in inventario:
      valores.append(elemento[1])
      average = sum(valores) / len(valores)
    if len(valores) > 0:
        print('Mais caro: ', max(valores))
        print('Mais barato: ', min(valores))
        print('Total: ', sum(valores))
        print('Média: ', average)
       

preencherInventario(inventario)

exibirInventario(inventario)

localizarPorNome(inventario)

depreciarPorNome(inventario)

excluirPorSerial(inventario)

resumirValores(inventario)