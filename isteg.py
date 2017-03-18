# # -*- coding: utf-8 -*-
# """
# Make sure you give execute privileges
# -----------------------------------------------------------------------------
#
#            Spark with Python: Your first Spark Program
#
#              Copyright : V2 Maestros @2016
#
# Please make sure to execute "SETUP Python for Spark.py" before running this
# -----------------------------------------------------------------------------
# """
# # -*- coding: utf-8 -*-
# """
# Make sure you give execute privileges
# -----------------------------------------------------------------------------
#
#            Spark with Python: Setup Spyder IDE for Spark
#
#              Copyright : V2 Maestros @2016
#
# Execute this script once when Spyder is started on Windows
# -----------------------------------------------------------------------------
# """
import os
import sys


from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
    # sc=SparkContext(master=None)
    # ss=SparkSession(sc)
    # warehouseLocation = "file:$C:/temp/sparkwarehouse"
    # spark = SparkSession.builder.appName("SparkSessionZipsExample").config("spark.sql.warehouse.dir", warehouseLocation).enableHiveSupport().getOrCreate()

    # SpSession = SparkSession \
    #     .builder \
    #     .master("spark://192.168.56.1:4040") \
    #     .appName("V2 Maestros") \
    #     .config("spark.executor.memory", "1g") \
    #     .config("spark.cores.max", "2") \
    #     .config("spark.sql.warehouse.dir", "C:/Users/arora/sparkWarehouse") \
    #     .getOrCreate
pyspark_submit_args = os.environ.get("PYSPARK_SUBMIT_ARGS", "")
if not "pyspark-shell" in pyspark_submit_args: pyspark_submit_args += " pyspark-shell"
os.environ["PYSPARK_SUBMIT_ARGS"] = pyspark_submit_args

conf = SparkConf()
    # conf.setMaster("spark:/192.168.56.1:4040")
    # conf.setMaster('local[2] pyspark-shell')
    # conf.setMaster("local")
conf.setAppName("spark_svm")
conf.set("spark.executor.memory", "12g")
sc = SparkContext(conf=conf)
ccRaw = sc.textFile("C:\\Users\\arora\\Documents\\nidhi\\big data project\\cs-training.csv")
ccRaw.take(5)
print ("Successfully imported Spark Modules")
print(ccRaw)



# import subprocess
# import os
# import sys
#
# # NOTE: Please change the folder paths to your current setup.
# # Windows
#
#     # Where you downloaded the resource bundle
#     # os.chdir("C:/Users/Kumaran/Dropbox/V2Maestros/Modules/Apache Spark/Python")
#     # Where you installed spark.
# os.environ['SPARK_HOME'] = 'C:\Spark\spark-2.1.0-bin-hadoop2.7'
# os.environ['JAVA_HOME']='C:\Program Files\Java\jdk1.8.0_121'
# # other platforms - linux/mac
#
# os.curdir
#
# # Create a variable for our r0oot path
# SPARK_HOME = os.environ['SPARK_HOME']
# JAVA_HOME=os.environ['JAVA_HOME']
# # Add the following paths to the system path. Please check your installation
# # to make sure that these zip files actually exist. The names might change
# # as versions change.
#
# # os.environ['PYSPARK_SUBMIT_ARGS']='--master local[2] pyspark-shell'
# sys.path.insert(0, os.path.join(SPARK_HOME, "python"))
# sys.path.insert(0, os.path.join(SPARK_HOME, "python", "lib"))
# sys.path.insert(0, os.path.join(SPARK_HOME, "python", "lib", "pyspark.zip"))
# sys.path.insert(0, os.path.join(SPARK_HOME, "python", "lib", "py4j-0.10.4-src.zip"))
# sys.path.insert(0, os.path.join(JAVA_HOME))
#
# subprocess.call(['C:\Spark\spark-2.1.0-bin-hadoop2.7\bin\spark-shell.cmd'])
#
# # Initialize SparkSession and SparkContext
# from pyspark.sql import SparkSession
# from pyspark import SparkContext
#
# # Create a Spark Session
# SpSession = SparkSession \
#     .builder \
#     .appName("V2 Maestros") \
#     .config("spark.executor.memory", "1g") \
#     .config("spark.cores.max", "2") \
#     .config("spark.sql.warehouse.dir", "C:/Users/arora/sparkWarehouse") \
#     .getOrCreate()
#
# # Get the Spark Context from Spark Session
# SpContext = SpSession.sparkContext
#
# # Test Spark
# testData = SpContext.parallelize([3, 6, 4, 2])
# testData.count()
# # check http://localhost:4040 to see if Spark is running
#
#
#
#
#
#
