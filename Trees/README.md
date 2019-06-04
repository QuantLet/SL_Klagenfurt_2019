[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **BaumProjekt** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of QuantLet : BaumProjekt

Published in : 'Trees'

Description : 'Applies random forests to classify real trees, based on Marius Sterlings DEDA_RandForest.'

Keywords : 'Random forest, feature importance, classification, decision tree comparision, trees, Linz'

See also : 'DEDA_RandForest'

Authors : Miriam Köberl, Marius Sterling

Submitted : July 3 2019 by Miriam Köberl

Example : 

```

### PYTHON Code
```python

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:25:51 2019

Code von Marius Sterling
Adaptiert von Miriam Koeberl
"""

#Decision Trees for Real Trees

import pandas 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pydot

#The file comes from https://www.data.gv.at/katalog/dataset/f660cf3f-afa9-4816-aafb-0098a36ca57d
#If downloaded anew, be careful with the seperators in the CSV. 
baum = pandas.read_csv("FME_BaumdatenBearbeitet_OGD_20190205.csv")

baum = baum[['Gattung','Art','Hoehe','Schirmdurchmesser','Stammumfang']]
baum.info()

#Eine gattung auswählen, die anderen auskommentieren
#genus = baum[baum.Gattung == 'Chamaecyparis']
#genus = baum[baum.Gattung == 'Fagus']
#genus = baum[baum.Gattung == 'Gleditsia']
#genus = baum[baum.Gattung == 'Larix']
#genus = baum[baum.Gattung == 'Liquidambar']
genus = baum[baum.Gattung == 'Populus']
#genus = baum[baum.Gattung == 'Tilia']

print set(genus.Art)

#Recoding species to numbers- 
genus_Art = range(len(genus.Art))
for i in genus_Art:
    for j in range(0,len(set(genus.Art))):
        if genus.Art.iloc[i] == list(set(genus.Art))[j]:
            genus_Art[i] = j

genus_Art = pandas.Series(genus_Art)    
genus= genus[['Hoehe','Schirmdurchmesser','Stammumfang']]

X_train, X_test, y_train, y_test = train_test_split(
    genus, 
    genus_Art,
    test_size=0.33, # ratio of data that is used for testing
    random_state=1, # setting random seed 
    stratify = genus_Art # Keeps the ratio of the labels in train and test the same as in the initial data
)

n_features = 3 #Hoehe,Schirmdurchmesser,Stammumfang
rf = RandomForestClassifier(
n_estimators=200, # Number of Trees grown
max_features=n_features, # Number of randomly picked features for split
max_depth=5, # Max Number of nested splits
random_state=1, # Seed for random number generator
)

#Seeing how good the accuracy is on the test and training data sets.
rf.fit(X_train,y_train)
print('The train accuracy: %.4f'%rf.score(X_train,y_train))
print('The test accuracy: %.4f'%rf.score(X_test,y_test))

#Extracting 10 trees from the random forest
for i in np.arange(10):
    tree = rf.estimators_[i]
    export_graphviz(
        tree, 
        out_file='tree.dot',
        feature_names=list(X_train.columns),
        rounded=True,
        precision=4,
        filled=True
    )
    (graph,) = pydot.graph_from_dot_file('tree.dot')
    graph.set_bgcolor('transparent')
    graph.write_png('RF_one_tree_no_%i.png'%i)
img = mpimg.imread('RF_one_tree_no_%i.png'%i)
plt.imshow(img)
plt.show(block=False)

#Print the first the first extracted tree and say how accurate it alone is in classifying the train and test data.
tree = rf.estimators_[0]
print('The train accuracy: %.4f'%tree.score(X_train,y_train))
print('The test accuracy: %.4f'%tree.score(X_test,y_test))
pandas.DataFrame(confusion_matrix(y_test, tree.predict(X_test)))


#Plots the importance of the features in the random forest.
feature_imp = pandas.DataFrame(rf.feature_importances_,index=('Hoehe','Schirmdurchmesser','Stammumfang'))
ax = feature_imp.plot(kind='barh', figsize=(12, 10), zorder=2)
plt.xlabel('Feature Importance')
plt.ylabel('Variable')
plt.tight_layout()
plt.savefig('RF_feature_importance.png', dpi=600, transparent=True)

# Setting mesh grid for the map classification
rf = RandomForestClassifier(
    n_estimators=300,
    random_state=1,
    max_depth=5
)


s=100
lab = ['Schirmdurchmesser','Stammumfang']
rf.fit(X_train[lab],y_train)
n_features = 2
r = abs(X_train.max() - X_train.min())
x_min = X_train.min() - r * 0.1
x_max = X_train.max() + r * 0.1
r /= s

xx, yy = np.meshgrid(
    np.arange(x_min[lab[0]], x_max[lab[0]], r[lab[0]]), 
    np.arange(x_min[lab[1]], x_max[lab[1]], r[lab[1]])
)


# Setting colors for the plots


n_classes = len(set(genus_Art))
if n_classes == 2:
    colors = ['b','r']
elif n_classes == 3:
    colors = ['b','g','r']
else:
    import matplotlib.cm as cm
    cmap = cm.get_cmap('rainbow', n_classes)    # PiYG
    colors = [cmap(i) for i in range(cmap.N)]


plt.figure()
ax = plt.gca()
Z = rf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contourf(xx, yy, Z, alpha=.4)
for b in set(y_train):
    idx = y_train == b
    idx2 = y_test == b
ax.set_xlim(xx.min(), xx.max())
ax.set_ylim(yy.min(), yy.max())
plt.xlabel(lab[0])
plt.ylabel(lab[1])
plt.legend(
    loc='center left',bbox_to_anchor=(1,0.5), title='Dataset',
    fancybox=False
)
plt.savefig('RF_contour.png',dpi=300,transparent=True)
plt.show()


# Prediction probabilies for the different classes

for cl in range(n_classes):
    plt.figure()
    ax = plt.gca()
    Z = rf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:,cl]
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=.4)
    for b in set(y_train):
        idx = y_train == b
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    plt.xlabel(lab[0])
    plt.ylabel(lab[1])
    plt.legend(
        loc='center left',bbox_to_anchor=(1,0.5), title='Dataset',
        fancybox=False
    )
    plt.tight_layout()
    plt.savefig('RF_contour_prob_class_%i.png'%cl,dpi=300,transparent=True)
    plt.show()


# ## Comparison

# ### Accuracy vs. number of trees


rf = RandomForestClassifier(
    n_estimators=200, # Number of Trees grown
    max_features=min(10,n_features), # Number of randomly picked features for split 
    max_depth=5, # Max Number of nested splits
    random_state=42,
)
res = []
for i in range(1,150,1):
    rf.n_estimators = i
    rf.fit(X_train,y_train)
    d = dict({'n_estimators':i})
    d.update({'train':rf.score(X_train,y_train)})
    d.update({'test':rf.score(X_test,y_test)})
    res.append(d)
res = pandas.DataFrame(res)
res.plot('n_estimators')
plt.ylabel('Accuracy')
plt.xlabel('Number of trees')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5), title='Dataset',fancybox=False)
plt.savefig('RF_accuracy_number_of_trees.png',dpi=300,transparent=True)
plt.tight_layout()
plt.show()


# ### Accuracy vs. Number of Samples per leaf
#Careful! Some of the samples have some categories with very few items. 
#This means that the test or training dataset might have none of them, 
#causing problems.

rf = RandomForestClassifier(
    n_estimators=500,
    max_features=min(10,n_features),
    min_samples_leaf=1,
    random_state=42,
)
min_sample_class = min([sum(y_train==i) for i in set(y_train)])
res = []

if min_sample_class <= 1:
    print 'A training set has maximally one sample.'
else:
    for i in range(1,min_sample_class):
        rf.min_samples_leaf = i
        rf.fit(X_train,y_train)
        d = dict({'min_samples_leaf':i})
        d.update({'train':rf.score(X_train,y_train)})
        d.update({'test':rf.score(X_test,y_test)})
        res.append(d)
    res = pandas.DataFrame(res)
    res.plot('min_samples_leaf')
    plt.ylabel('Accuracy')
    plt.xlabel('Minimum number of samples in each leaf')
    plt.legend(loc='center left',bbox_to_anchor=(1,0.5), title='Dataset',fancybox=False)
    plt.savefig('RF_accuracy_number_of_samples_per_leaf.png',dpi=300,transparent=True)
    plt.tight_layout()
    plt.show()

```

automatically created on 2019-06-04