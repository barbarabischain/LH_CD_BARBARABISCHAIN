import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch

fig = plt.figure(dpi=150)
ax = fig.add_subplot(111)

xmin=-74.3
xmax=-73.6
ymin=40.45
ymax=41
m = Basemap(projection='merc',lat_ts=10,llcrnrlon=xmin, urcrnrlon=xmax,llcrnrlat=ymin,urcrnrlat=ymax, resolution='c')
m.readshapefile('/nfs/homes/babischa/LH_CD_BARBARABISCHAIN/maps/nyzones','mapa', drawbounds=True)
m.drawparallels(np.arange(ymin,ymax, .1), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(xmin,xmax, .2), labels=[0,0,0,1], fontsize=10)

zones={'QW':'blue','BKS':'red','SI':'green','MN':'purple','BX':'pink','BKN':'yellow','QE':'orange'}
colors=[]
patches   = []

for info , shape in zip(m.mapa_info, m.mapa):
    if (info['zone']):
        patches.append( Polygon(np.array(shape), True) )
        colors.append(zones[info['zone']])
ax.add_collection(PatchCollection(patches, facecolor=colors, edgecolor='k', linewidths=1., zorder=2))
# print(colors)
# print(patches)
plt.savefig('mapa.png', dpi=300, bbox_inches='tight')

gdf = gpd.read_file("nyzones.shp")
print(gdf)
