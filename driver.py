"""
    A main driver program that will call the mapper and reducer multiple
    times until the centroids converge.
"""

import subprocess

from utils import *

if __name__ == "__main__":
    dataFile = 'input1.txt'
    numCentroids = 10
    outputFolder = "data-output"
    maxIterations = 10
    initialGeneID = None

    hadoopPath = "/home/ubuntu/hadoop-2.7.3/bin/"
    hdfsClearDataCommand = "{}hdfs dfs -rm -r ~/run-data".format(hadoopPath)
    hdfsMakeDirectoryCommand = "{}hdfs dfs -mkdir ~/run-data".format(hadoopPath)
    hdfsPutDataCommand = "{}hdfs dfs -put {} ~/run-data/".format(hadoopPath, dataFile)
    hdfsRemoveOutputCommand = "{}hdfs dfs -rm -r {}".format(hadoopPath, outputFolder)
    hadoopCommand = "{}hadoop jar /home/ubuntu//hadoop-2.7.3/share/hadoop/tools/lib/hadoop-*streaming*.jar -files mapper.py,reducer.py,centroids1.txt -mapper mapper.py -reducer reducer.py -input ~/run-data -output {}".format(
        hadoopPath, outputFolder)
    fetchCentroidsCommand = "{}hdfs dfs -cat {}/*".format(hadoopPath, outputFolder)

    converged = False
    iterations = 0
    tempStdOutput = None
    centroids = "centroids1.txt"

data = readDataFromFile(dataFile)
currentCentroids = assignInitialCentroids(initialGeneID, data, centroids, numCentroids)
print(currentCentroids)

subprocess.Popen(hdfsClearDataCommand, shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen(hdfsMakeDirectoryCommand, shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen(hdfsPutDataCommand, shell=True, stdout=subprocess.PIPE).stdout.read()

while not converged:
    subprocess.Popen(hdfsRemoveOutputCommand, shell=True, stdout=subprocess.PIPE).stdout.read()
    subprocess.Popen(hadoopCommand, shell=True, stdout=subprocess.PIPE).stdout.read()
    fetchedReducerOutput = subprocess.Popen(fetchCentroidsCommand, shell=True, stdout=subprocess.PIPE).stdout.read()

    updatedCentroids = processCentroids(fetchedReducerOutput, centroids)
    iterations += 1

    if checkConvergence(currentCentroids, updatedCentroids):
        converged = True

    if iterations == maxIterations:
        converged = True

    currentCentroids = updatedCentroids

print("Total Iterations: ", iterations)

resultClusters, finalClusters = assignCentroidToData(data, currentCentroids)

print ("Final Clusters (cluster, [GeneIDs]):")
index = 0
for cluster in finalClusters:
    stringOuptut = ",".join([str(i) for i in finalClusters[cluster]])
    print (
        "{}\t{}\t{}\t{}".format(cluster, len(finalClusters[cluster]), ",".join(str(x) for x in currentCentroids[index]),
                                stringOuptut))
    index += 1
