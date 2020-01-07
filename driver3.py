#!/usr/bin/env python
import os
import subprocess

FNULL = subprocess.PIPE
OUTPUT_DIR = '/home/ubuntu/run-data/output'

inputs = raw_input("Enter the Gender(Male=0, Female=1), Age, Salary and Spending Score separated by space: ").strip()
# inputs = "1 21 33 81"
dataFile = 'input3.txt'
hadoopPath = "/home/ubuntu/hadoop-2.7.3/bin/"
hdfsClearDataCommand = "{}hdfs dfs -rm -r /home/ubuntu/run-data".format(hadoopPath)
hdfsMakeDirectoryCommand = "{}hdfs dfs -mkdir /home/ubuntu/run-data".format(hadoopPath)
hdfsMakeDirectoryCommand2 = "{}hdfs dfs -mkdir /home/ubuntu/run-data/output".format(hadoopPath)
hdfsPutDataCommand = "{}hdfs dfs -put {} /home/ubuntu/run-data/".format(hadoopPath, dataFile)
hdfsRemoveOutputCommand = "{}hdfs dfs -rm -r {}".format(hadoopPath, OUTPUT_DIR)
subprocess.Popen(hdfsClearDataCommand, shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen(hdfsMakeDirectoryCommand, shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen(hdfsMakeDirectoryCommand2, shell=True, stdout=subprocess.PIPE).stdout.read()
subprocess.Popen(hdfsPutDataCommand, shell=True, stdout=subprocess.PIPE).stdout.read()

status = subprocess.call("/home/ubuntu/hadoop-2.7.3/bin/hdfs dfs -test -d " + OUTPUT_DIR, stdout=FNULL, stderr=FNULL, shell=True)
if status == 0: subprocess.call("/home/ubuntu/hadoop-2.7.3/bin/hdfs dfs -rm -r " + OUTPUT_DIR, stdout=FNULL, stderr=FNULL, shell=True)

hadoopCommand = "{}hadoop jar /home/ubuntu/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-*streaming*.jar -files mapper3.py,reducer3.py -mapper 'mapper3.py {}' -reducer reducer3.py -input ~/run-data -output {}".format(
        hadoopPath, inputs, OUTPUT_DIR)
subprocess.Popen(hadoopCommand, shell=True, stdout=subprocess.PIPE).stdout.read()