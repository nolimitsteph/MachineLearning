# Univariate Histograms
import numpy
from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import scatter_matrix

filename = 'pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

# histograms
data.hist()
pyplot.show()

# density plots
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()

#box plots
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
pyplot.show()

#multivariate plots
correlations = data.corr()

# plot correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show()


# plot correlation matrix without specifying the names for the attributes along the axes as
# well as the number of ticks
fig = pyplot.figure()
ax = fig.add_subplot(222)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
pyplot.show()
"""
3. Pourquoi le rendu de votre code actuel risque d'être étrange

Si vous modifiez uniquement cette ligne dans le script original, deux phénomènes visuels vont se produire :
1. La barre de couleur (fig.colorbar) va s'adapter : Matplotlib va automatiquement coller la barre verticale colorée juste à droite du petit graphique situé en haut à droite. Elle restera proportionnelle à la taille du graphique réduit.
2. Le graphique va paraître minuscule : Comme il n'occupe qu'un quart de l'espace, les écritures ou les cases de la matrice de corrélation seront très compactes si vous laissez la fenêtre à sa taille par défaut.

À quoi sert généralement cette modification ?

On utilise add_subplot(222) lorsqu'on souhaite faire un tableau de bord multi-graphiques. Par exemple, vous pourriez afficher l'histogramme en position 221, la matrice de corrélation en 222, les boxplots en 223 et le scatter plot en 224.
Souhaitez-vous voir le code complet pour remplir les 3 autres espaces vides (221, 223 et 224) avec les histogrammes et les boîtes à moustaches afin de créer un tableau de bord complet dans une seule fenêtre ?"""




# scatter plot matrix
scatter_matrix(data)
pyplot.show()
