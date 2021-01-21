# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2020/12/21 19:56'
import arcpy
# import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
#F:\POI数据\2017\2017

# path = r"H:\\科研数据\\武汉市17年点shp"

path="H:\\Example\\regionshp"
path="E:\\Githubresponsity\\arcgis\\wuhan"

path="F:\\2017\\2017"

files = os.listdir(path)

# for filename in files:
#     print(filename)
folders=[]
for i in files:
    if i.split('.')[1]=='shp' and len(i.split('.'))==2:
        if i!='事件活动.shp':
            folders.append(i)
            print i

NAME = []
ADDRESS = []
TELEPHONE = []
PROVINCE = []
CITY = []
COUNTY = []
CODE = []
LON = []
LAT = []
TYPECODE = []
BASETYPE = []
SUBTYPE = []
CATEGORY = []

for file in folders:
    shppath = os.path.join(path,file)

    #提取shp文件中的'FID', 'POINT_X', 'POINT_Y'字段
    shpfields = ['NAME','ADDRESS','TELEPHONE','PROVINCE','CITY','COUNTY','CODE','LON','LAT','TYPECODE','BASETYPE','SUBTYPE','CATEGORY']

    shprows = arcpy.SearchCursor(shppath, shpfields)
    while True:
        shprow = shprows.next()
        if not shprow:
            break
        if shprow.CITY=="武汉市":
            NAME.append(shprow.NAME)
            ADDRESS.append(shprow.ADDRESS)
            TELEPHONE.append(shprow.TELEPHONE)
            PROVINCE.append(shprow.PROVINCE)
            CITY.append(shprow.CITY)
            COUNTY.append(shprow.COUNTY)

            CODE.append(shprow.CODE)
            LON.append(shprow.LON)
            LAT.append(shprow.LAT)
            TYPECODE.append(shprow.TYPECODE)
            BASETYPE.append(shprow.BASETYPE)
            SUBTYPE.append(shprow.SUBTYPE)
            CATEGORY.append(shprow.CATEGORY)

result=[NAME,ADDRESS,TELEPHONE,PROVINCE,CITY,COUNTY,CODE,LON,LAT,TYPECODE,BASETYPE,SUBTYPE,CATEGORY]

with open('2017pois.csv','w') as f:
    for i in range(0, len(CATEGORY)):
        for j in result:
            # print j[i]
            f.write(str(j[i]))
            f.write(',')
        f.write('\n')