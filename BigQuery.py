import os
from google.cloud import bigquery
import pandas as pd
from pandas_gbq import read_gbq

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
client = bigquery.Client()
project_id = 'eae01-411520'
dataset_id = 'eae01-411520.DS01'

query = """
SELECT
   *
   FROM
  `eae01-411520`.DS01.AWSalesLine LIMIT 2
  
    """
#display table
job = client.query(query)
job.to_dataframe()
rows = job.result()
df=rows.to_dataframe()
print(df)

#dataset name
#dataset = client.get_dataset(dataset_id)
#dataSetName = dataset.friendly_name
#print( dataSetName)

#datasets = list(client.list_datasets())  # Make an API request.
#project = client.project

#if datasets:
    #for dataset in datasets:
        #print(f"{dataset.dataset_id}")
#else:
   # print(" project does not contain any datasets")

