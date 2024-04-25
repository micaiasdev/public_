from Node import Node

class ListaEncadeada:
  
  def __init__(self):
    self.inicio = None
    self.final = None
    self.tam = 0
    
  def isEmpty(self):
    return self.inicio is None
  
  def add(self, item):
    novo = Node(item)
    
    if self.inicio is None:
      self.final = novo
      self.inicio = novo 
    
    novo.nextData = self.inicio
    
    self.inicio = novo
    
    self.tam += 1
  
  def addFinal(self, item): 
    novo = Node(item)
    if self.final is None:
      self.final = novo
      self.inicio = novo  
    
    self.final.nextData = novo
    
    self.final = novo
    
  
  def size(self):
    return self.tam
  
  def search(self, atual, item):
       
    if atual is None:
      return atual
    
    if atual.data == item:
      return atual.data
    else:
      return self.search(atual.nextData, item)
  
  def remove(self, item):
    atual = self.inicio
    ant = None
    if atual is None:
      return None
    
    while atual is not None:
      if atual.data == item:
        if ant is None:
          self.inicio = atual.nextData
          return True
        else:
          ant.nextData = atual.nextData
          return True
      else:  
        ant = atual
        atual = atual.nextData
    return False          

  def __str__(self):
    string = ''
    atual = self.inicio
    while atual is not None:
      string += f"{atual.data} "
      atual = atual.nextData
    return string       

  
