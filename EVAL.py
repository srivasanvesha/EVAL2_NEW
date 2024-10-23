df = pd.read_csv('file.cv')
df = pd.read_csv('file.cv')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[1], line 1
----> 1 df = pd.read_csv('file.cv')

NameError: name 'pd' is not defined

port pandas as pd
import pandas as pd
s
df = pd.read_csv('file.csv')
mongo_schema = {
    "certification_numer" : "Number",
    "provider" : "String",
    "telephone" : "Number",
    "CMS_region" : "Number",
    "ownership_type": "String",
    "certification_date" : "Date",
    "address": {
        "address1": "String",
        "address2": "String",
        "city": "String",
        "state": "String",
        "zip_code": "Number"
    },
}
go_schema
print(mongo_schema)
{'certification_numer': 'Number', 'provider': 'String', 'telephone': 'Number', 'CMS_region': 'Number', 'ownership_type': 'String', 'certification_date': 'Date', 'address': {'address1': 'String', 'address2': 'String', 'city': 'String', 'state': 'String', 'zip_code': 'Number'}}
df.type
non_profit = df[
    df.type
]
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
~\AppData\Local\Temp\ipykernel_11828\616132361.py in ?()
      1 non_profit = df[
----> 2     df.type
      3 ]

C:\ProgramData\anaconda3\Lib\site-packages\pandas\core\generic.py in ?(self, name)
   5985             and name not in self._accessors
   5986             and self._info_axis._can_hold_identifiers_and_holds_name(name)
   5987         ):
   5988             return self[name]
-> 5989         return object.__getattribute__(self, name)

AttributeError: 'DataFrame' object has no attribute 'type'

​
