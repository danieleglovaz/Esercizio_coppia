import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Star:
    
  def __init__(self, nome_file):

    self.data = pd.read_table(nome_file, sep=' ')

  #plottaggio
  def plot_vs_time(self, colonna1, colonna2):
    
    x = colonna1
    y = colonna2

    bins = pd.cut(self.data["age_parent"], np.array([0,1,5,30]))

    plt.figure(111, figsize=(10,8))

    for bin_value, group in self.data.groupby(bins):
      a = plt.scatter(
        self.data[colonna1], self.data[colonna2], c=self.data["age_parent"], cmap="viridis", s=10, alpha=0.8,
        label= f"Bin: {bin_value.left:.2f} to {bin_value.right:.2f}"
      )
    
    ax = plt.gca()  
    ax.yaxis.set_inverted(True)
    plt.colorbar(a)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

star1 = Star('Nemo_6670.dat')

star1.plot_vs_time("b-y", "M_ass")

star1.plot_vs_time("b-y", "MsuH")
