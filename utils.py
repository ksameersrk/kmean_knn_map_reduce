import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA


def readDataFromFile(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    data = []
    for line in lines:
        s = line.strip().split("\t")
        data.append(s)
    return np.array(data).astype(float)


def assignInitialCentroids(genes, data, filename, numCentroids):
    if genes:
        samplePoints = [i - 1 for i in genes]
    else:
        samplePoints = np.random.randint(0, data.shape[0], numCentroids)
    output = open(filename, 'w')
    for i in samplePoints:
        x = "\t".join([str(data[i][j]) for j in xrange(len(data[i]))])
        output.write(x + "\n")
    output.close()
    return data[samplePoints]


def checkConvergence(oldClusters, newClusters):
    for i in xrange(len(oldClusters)):
        if np.linalg.norm(oldClusters[i] - newClusters[i]) > 0:
            return False
    return True


def processCentroids(data, filename):
    data = data.split('\n')
    output = []
    outputFile = open(filename, 'w')
    for i in data:
        temp = i.split("\t")
        if len(temp) > 1:
            temp = temp[1:]
            output.append(np.array(temp, dtype=float))
            writeData = "\t".join([str(temp[j]) for j in xrange(len(temp))])
            outputFile.write(writeData + "\n")

    outputFile.close()
    return output


def generateMatrices(groundTruth, result):
    N = len(groundTruth)
    P = [[0 for j in xrange(N)] for i in xrange(N)]
    C = [[0 for j in xrange(N)] for i in xrange(N)]
    for i in xrange(N):
        for j in xrange(N):
            if groundTruth[i] == groundTruth[j]:
                P[i][j] = 1
                P[j][i] = 1
    for i in xrange(N):
        for j in xrange(N):
            if result[i] == result[j]:
                C[i][j] = 1
                C[j][i] = 1
    return P, C


def assignCentroidToData(data, centroids):
    resultClusters = []
    finalClusters = {}
    geneID = 1
    for point in data:
        cluster = min([(a[0], np.linalg.norm(point - a[1])) for a in enumerate(centroids)], key=lambda x: x[1])[0]
        resultClusters.append(cluster)

        if cluster not in finalClusters:
            finalClusters[cluster] = []
        finalClusters[cluster].append(geneID)
        geneID += 1
    return resultClusters, finalClusters
