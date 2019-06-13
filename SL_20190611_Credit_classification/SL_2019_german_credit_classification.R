# 20190505 Schneider Philipp
# Statistisches Lernen
# Abschlussprojekt
# Klassifikationsmethoden für German Credit Data



rm(list=ls())
# Workspace leeren.

install.packages("randomForest","e1071","gmodels")

library(randomForest)
library(e1071)
library(gmodels)


url="http://freakonometrics.free.fr/german_credit.csv"
credit=read.csv(url, header = TRUE, sep = ",")
str(credit)
F=c(1,2,4,5,7,8,9,10,11,12,13,15,16,17,18,19,20) 
# Diese Attribute sind kategorisch, werden aber noch wie numerische behandelt.
for(i in F) credit[,i]=as.factor(credit[,i])
# Wandelt sie in kategorische Attribute um.



set.seed(23)
# Wähle einen Startwert für den Zufallszahlengenerator.



selection = sample(1:1000,700,replace=FALSE)
# Wähle 700 Zufallszahlen von 1 bis 1000.

train = credit[selection,]
# Wähle anhand der Zufallszahlen nun Beobachtungen aus dem Datensatz.
# Dies ergibt die Trainingsdaten.

test = credit[-selection,]
# Der Rest wird als Testdatensatz definiert.

model1 = randomForest(Creditability ~ .,data = train)
# Das erste Random Forest Modell wird mit Standardeinstellungen gebildet.

pred1 = predict(model1, test, type="class")
# Treffe nun Vorhersagen für Testdaten.

table(pred1==test[,1])/300
# Rate an inkorrekt / korrekt klassifizierten Objekten.

CrossTable(x = test[,1], y = pred1, prop.chisq = FALSE)
# Die Konfusionsmatrix für das erste Modell.

model1$importance
# Zeigt die durchschnittliche Verbesserung des Gini-Index für jedes Attribut an.
# Je höher, desto besser.

credit = credit[,1:14]
credit = credit[,c(-10,-11)]
# Die unwichtigen Attribute werden entfernt.


train2 = credit[selection,]

test2 = credit[-selection,]
# Trainings- und Testdatensätze werden aus dem reduzierten Datensatz neu bestimmt.

mtrygrid=c(4,5,6,7,8,9,10)
# Der Wertebereich für die Attributanzahl in der Gittersuche.

ngrid=c(500,600,700,800,900,1000)
# Der Wertebereich für die Anzahl an Bäumen in der Gittersuche.


# ACHTUNG!
# Die Tune-Funktion kann einige Minuten in Anspruch nehmen!
tune.out=tune(randomForest, Creditability~., data=train2, ranges=list(mtry=mtrygrid,ntree=ngrid))

tune.out
# Das Ergebnis der Gittersuche mit Crossvalidation.


model2 = randomForest(Creditability~ ., data = train2, mtry = 10, ntree = 500)
# Das zweite Modell wird nun mit den gefundenen Parametern gebildet.

pred2 = predict(model2, test2, type="class")

table(pred2 == test2[,1])/300
# Die Vorhersagegenauigkeit ist ein wenig höher als beim ersten Modell.




#Konfusionsmatrix:
CrossTable(x = test2[,1], y = pred2, prop.chisq = FALSE)
