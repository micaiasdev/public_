class Node:
  
  def __init__(self, atualData):
    self.data = atualData
    self.nextData = None

  def getData(self):
    return self.data
  
  def getnextData(self):
    return self.nextData