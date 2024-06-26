#import PIL.Image
#import PIL.ExifTags
import phonenumbers
import folium
import pandas as pd
import numpy as np
import plotly.express as px
from phonenumbers import geocoder
import webbrowser
import gmplot
from opencage.geocoder import OpenCageGeocode
#import openrouteservice as ors

'''
def matrix(L1):
  for i in L1:
    for j in i:
      print(j,end="\t")
    print()
'''

R=6371 # radius of earth
def degtorad(degrees):
  return degrees*(np.pi/180)


def distance(lat1,lon1,lat2,lon2):
  d_lat=degtorad(lat2-lat1)
  d_lon=degtorad(lon2-lon1)

  a=np.sin(d_lat/2)**2+ np.cos(degtorad(lat1)) * np.cos(degtorad(lat2)) * np.sin(d_lon/2)**2
  c=2*np.arctan2(np.sqrt(a),np.sqrt(1-a))
  return R*c

#dist=distance(22.488540958444293,88.36633469004033,22.516608987371367,88.41689322299352)

#print("distance==",round(dist,2),"km")
#dist=str(round(dist,1))+"km"


Key="1cc863a87e114ed09ad173e0be2c3413"
geocoder=OpenCageGeocode(Key)



lat1=22.488540958444293  # base mohit
long1=88.36633469004033
print(lat1,"base",long1)
l1=[lat1,long1,"MOHIT","blue"]

lat2=22.516814670376156  # suruchi
long2=88.41685082136387
print(lat2,"suruchi",long2)
l2=[lat2,long2,"suruchi","red"]

lat3=22.665829013300787 # atyasha
long3=88.37024910404209
print(lat3,"atyasha",long3)
l3=[lat3,long3,"atyasha","red"]

lat4=22.498554644123246 
long4=88.34648368923628
print(lat4,"cherry",long4)
l4=[lat4,long4,"cherry","red"]


lat5=22.590275715257853 
long5=88.39234202209045
print(lat5,"priyanshu",long5)
l5=[lat5,long5,"priyanshu","red"]

lat6=22.59156482719839 
long6=88.36498940273046
print(lat6,"dishika",long6)
l6=[lat6,long6,"dishika","red"]


lat7=22.50725677978552 
long7=88.40439826040037
print(lat7,"shivam",long7)
l7=[lat7,long7,"shivam","red"]

lat8,long8=25.1872850, 86.1016990
print(lat8,"khushi",long8)
l8=[lat8,long8,"khushi","red"]


mapp=folium.Map(location=[lat1,long1],zoom_start=50)

'''
#mapp=folium.Map(location=[lat2,long2],zoom_start=100)

#folium.Marker([lat1,long1],radius=5,popup="HERE").add_to(mapp)
#folium.Marker([lat2,long2],radius=5,popup="HERE").add_to(mapp)

#gmap1 = gmplot.GoogleMapPlotter(lat1,long1,13,marker=True)
#gmap1 = gmplot.GoogleMapPlotter(lat2,long2,13,marker=True)
#gmap1.marker(lat1,long1)
#gmap1.marker(lat2,long2)
#gmap1.draw("mygmap.html")

#mapp.save("mymap.html")

#webbrowser.open("mymap.html",new=2)

#‘green’, ‘purple’, ‘orange’

#L1=[[22.516814670376156,88.41685082136387,"Suruchi","red"],[22.488540958444293,88.36633469004033,"Mohit","blue"]]
'''

L1=[l1,l2,l3,l4,l5,l6,l7,l8]
points=[]
for i in L1:
    folium.Marker([i[0],i[1]],popup=i[2],icon=folium.Icon(color=i[3],icon_colour="white",prefix="fa",icon="location-dot")).add_to(mapp)
    points.append([i[0],i[1]])

L2=[l2,l3,l4,l5,l6,l7,l8]
for i in L2:
  dist=distance(lat1,long1,i[0],i[1])

  print("base->",i[2],"->",round(dist,2),"km")
  dist=str(round(dist,1))+"km"
  folium.PolyLine([[lat1,long1],[i[0],i[1]]],color="black",dash_array='5',opacity=".85",popup=dist).add_to(mapp)


for i in L2:
  L3=L2.copy()
  L3.remove(i)
  for j in L3:
    dist=distance(i[0],i[1],j[0],j[1])

    print(i[2],"->",j[2],"distance==",round(dist,2),"km")
    dist=str(round(dist,1))+"km"
    folium.PolyLine([[i[0],i[1]],[j[0],j[1]]],color="black",dash_array='5',opacity=".85",popup=dist).add_to(mapp)

'''
# shortest path

num=len(L1)

L5= [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
# matrix(L5)
# khali matrix bana liya
for i in range(0,1):
  for j in range(1,len(L1)):
    dist=round(distance(L1[i][0],L1[i][1],L1[j][0],L1[j][1]),2)
    L5[i][j]=dist
matrix(L5)
# first row ko populate kar diya
summ=0
L6=L5.copy()


for i in range (0,8):
  print("fixed element",L5[i][0]);
  print(min(L5[i]))
  newfix=L5[i].index(min(L5[i]));
  L6.pop(newfix)
  summ=summ+min(L5[i])
  print(newfix,summ)

#gmap1.draw("mygmap.html")
'''

mapp.save("mymap.html")

webbrowser.open("mymap.html",new=2)

