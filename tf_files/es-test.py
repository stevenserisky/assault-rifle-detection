# coding: utf-8
from IPython.display import Image, display, clear_output
from elasticsearch import Elasticsearch

# Hold warnings
import warnings
warnings.filterwarnings('ignore')

# Setup ES 
try:
    es = Elasticsearch(
        [
            'https://elastic:diatonouscoggedkittlepins@elasticsearch.orange.opswerx.org:443'
        ],
        verify_certs=True
    )
    print("ES - Connected.")
except Exception as ex:
    print("Error: ", ex)

# Send results to ES
for x in range(5):
    tdoc = {
    'content': 'Test Message',
    'text': 'This is just a test...',
    'dude': 'SS',
    'number': x,
    }
    es_post = es.index(index="test", doc_type="_doc", body=tdoc)
    print('ES document sent.')
    print(tdoc)
