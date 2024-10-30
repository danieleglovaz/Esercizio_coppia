import pandas as pd

class Star:
    
    def __init__(self, MsuH, b_y, age_parent):
       self.MsuH = MsuH
       self.b_y = b_y
       self.age_parent = age_parent
  
data = pd.read_table('Nemo_6670.dat', sep=' ')

Star = Star(data['MsuH'],data['b-y'],data['age_parent'])

#plottaggio