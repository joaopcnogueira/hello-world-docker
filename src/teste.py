import numpy as np
print("numpy has been imported ...")

import pandas as pd
print("pandas has been imported ...")

from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
print("SparkSession has been initiated!")

print(f"Hello Docker!")