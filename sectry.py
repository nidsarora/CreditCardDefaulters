import os

from pyspark import SparkContext
import csv
import pandas as pd

from pyspark import SparkContext
from pyspark import SQLContext
filepath= "C:\\Users\\arora\\Documents\\nidhi\\big data project"

pyspark_submit_args = os.environ.get("PYSPARK_SUBMIT_ARGS", "")
if not "pyspark-shell" in pyspark_submit_args: pyspark_submit_args += " pyspark-shell"
os.environ["PYSPARK_SUBMIT_ARGS"] = pyspark_submit_args
sc =SparkContext()
print(sc)

df1=pd.DataFrame.from_csv('cs-training.csv')
