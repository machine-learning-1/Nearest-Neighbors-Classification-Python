import csv
import random
import math
import operator
from	matplotlib	import	pyplot	as	plt

def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	n_feature = len(dataset[0])-1
	for x in range(len(dataset)-1):
		for y in range(n_feature):
			dataset[x][y] = float(dataset[x][y])
	return dataset

def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) -1 < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]


def euclidiana(valor1, valor2):
	distance = 0
	n_features = len(valor2)
	for x in range(n_features-1):
		distance += pow(float(valor1[x]) - float(valor2[x]), 2)
	return math.sqrt(distance)

def vecino(dataset,prueba):
	distancia = 0
	distances = []
	for n in range(len(dataset)):
		distancia = euclidiana(dataset[n],prueba)
		distances.append((dataset[n],distancia))
	distances.sort(key=operator.itemgetter(1))
	return distances

def entrenar(testData,datos_entrenamiento,):
	performance = 0
	for n in range(len(testData)):
		distancias = vecino(datos_entrenamiento,testData[n])
		if testData[n][-1] == distancias[0][0][-1]:
			performance +=1
	return (performance/float(len(testData)) * 100)

#Esta funcion (entrenamiento_vs_limiar) es opcional, sino tienes matplot lib puedes borrarla y usar sólo
#la funcion main()
def entrenamiento_vs_limiar(): 
	archivo = 'iris.data'
	datos = loadCsv(archivo)
	limiar = 0
	vector =[]
	d = [10, 20, 30, 40,50,60,70,80,90,100]
	for x in range(10):
		datos_entrenamiento, testData = splitDataset(datos,limiar)
		performance = entrenar(testData,datos_entrenamiento)
		vector.append(performance)
		limiar = limiar + .1

	plt.plot(d,	vector,	color='green',	marker='o',	linestyle='solid')
	plt.title("Porcentaje de entrenamiento")
	plt.ylabel("Performance")
	plt.show()

def main():
	archivo = 'iris.data'
	limiar = 0.7
	datos = loadCsv(archivo)
	datos_entrenamiento, testData = splitDataset(datos,limiar)
	prueba_single = [4.7, 3.2, 1.3, 0.2,'Iris-setosa']#iris
	performance = entrenar(testData,datos_entrenamiento)
	print performance	

#main() 
entrenamiento_vs_limiar()
