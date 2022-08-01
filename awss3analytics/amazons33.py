import boto3
import numpy as np
from botocore.handlers import disable_signing
from mimetypes import MimeTypes
from tabulate import tabulate
import os
import filetype
import matplotlib.pyplot as plt
from tkinter import *
import seaborn as sn
session = boto3.Session()
#Then use the session to get the resource
s3 = session.resource('s3')
s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
my_bucket = s3.Bucket('analyticsdataraksh')
ob1={}
ob2={}
for my_bucket_object in my_bucket.objects.all():
  ob2.update({my_bucket_object.key.split('.')[0]: my_bucket_object.size})
  ob1.update({my_bucket_object.key.split('.')[0]: my_bucket_object.key.split('.')[1]})
names = list(ob2.keys())
values = np.array(list(ob2.values()))
values1= list(ob1.values())
plt.title("AWS S3 objects names vs size")
colors = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan']
porcent = 100.*values/values.sum()
patches, texts = plt.pie(values, colors=colors, startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(names, porcent)]
sort_legend = True
if sort_legend:
     patches, labels, dummy =  zip(*sorted(zip(patches, labels, values), key=lambda names: names[2], reverse=True))
plt.legend(patches, labels, loc='upper right', bbox_to_anchor=(-0.1, 1.),
            fontsize=8)
plt.show()
plt.savefig('piechart.png', bbox_inches='tight')
plt.title("AWS s3 File size vs File Type")
plt.pie(values)
plt.legend(labels=values1, loc='upper center', 
           bbox_to_anchor=(0.5, -0.04), ncol=6)

# Display

plt.show() 
