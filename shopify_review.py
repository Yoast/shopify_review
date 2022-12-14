import os
import json
#import airflow
#from airflow import DAG

if os.path.exists("review.json"):
  os.remove("review.json")
    
os.popen('scrapy runspider ./shopify_review/spiders/review.py -o review.json')
