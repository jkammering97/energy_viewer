#%%
import streamlit as st
import requests
import xmltodict, json
#%%
requ = requests.get('https://ghoapi.azureedge.net/api/Indicator?$filter=IndicatorName%20eq%20%27Ambient%20air%20pollution%20attributable%20deaths%27')
print(requ.content)
#%%
# retrieve dimesnion
dimensions = requests.get('http://apps.who.int/gho/athena/api/')

o = xmltodict.parse(dimensions.content)
metadata_dimensions = o['GHO']['Metadata']['Dataset']

dim_list = []
for dimension in metadata_dimensions:
    dim_list.append(dimension['Display'])
#%%
q[1]#['Dataset']
# %%
