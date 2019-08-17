import numpy as np
print("numpy has been imported ...")

import pandas as pd
print("pandas has been imported ...")

#from pyspark.sql import SparkSession
#spark = SparkSession.builder.getOrCreate()
#print("SparkSession has been initiated!")


df = pd.read_csv("/usr/src/app/input/titanic.csv", sep="\t")
print(df.head())

small_df = df.head()
small_df.to_csv("/usr/src/app/output/small_titanic.csv", index=False, sep=';')

print(f"\nHello Docker!")