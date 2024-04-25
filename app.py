from ListaEncadeada import ListaEncadeada

if __name__ == "__main__":

  myList = ListaEncadeada()

  for i in range(4):
    myList.add(i)
  
  """ print(myList.__str__())
  print("Vazio: ", myList.isEmpty())
  print("tamanho: ", myList.size())
  print("Item:", myList.search(myList.inicio, 2)) """
  
  #print(myList.remove(0))
  """ print(myList.__str__())
  print("Item:", myList.search(myList.inicio, 1)) """
  
  #myList.addFinal(5)
  
  print(myList.__str__())
  