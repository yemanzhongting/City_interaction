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
path2="F:\\2016\\2016"
path3="F:\\2014"

files = os.listdir(path)

for filename in files:
    print(filename)

folders=[]

print files

for i in files:
    print i
    try:
        if i.split('.')[1]=='shp' and len(i.split('.'))==2:
            if i!='事件活动.shp':
                folders.append(i)
                print i
    except:
        pass
        # if i == '公共设施.shp':
        #     folders.append(i)
        #     print i

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

CITY_LIST=[]
import codecs
print folders
#with codecs.open('ChinaAll.csv','w','utf-8') as fh:
with codecs.open('NetChina.csv','r','utf-8') as f:
    Acities=f.readlines()[1:]
cities=[]
names=[]
for i in Acities:
    cities.append(i.split(',')[-1])
    names.append(i.split(',')[0])

print cities
print names

index=0

for city in cities:
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
            # if shprow.CITY not in CITY_LIST:
            if shprow.CITY==names[index]:
            #     CITY_LIST.append(shprow.CITY)

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

    index=index+1

    with codecs.open(str(city.replace('\r\n',''))+'2017pois.csv', 'w', 'utf-8') as fh:
    # with open(city+'2014pois.csv','w') as f:
        for i in range(0, len(CATEGORY)):
            for j in result:
                # print j[i]
                fh.write(str(j[i]))
                fh.write(',')
            fh.write('\n')

# print CITY_LIST
#
# print len(CITY_LIST)
# import codecs
#
# with codecs.open('ChinaAll.csv','w','utf-8') as fh:
#     for i in CITY_LIST:
#         fh.write(i)
#         fh.write('\n')
#     print("写入成功")

# result=[NAME,ADDRESS,TELEPHONE,PROVINCE,CITY,COUNTY,CODE,LON,LAT,TYPECODE,BASETYPE,SUBTYPE,CATEGORY]
#
# with open('2017pois.csv','w') as f:
#     for i in range(0, len(CATEGORY)):
#         for j in result:
#             # print j[i]
#             f.write(str(j[i]))
#             f.write(',')
#         f.write('\n')