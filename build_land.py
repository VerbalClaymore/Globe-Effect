"""Build evenly spaced land dots from public-domain Natural Earth polygons."""
import json, math
from pathlib import Path
root = Path(__file__).parent
data = json.loads((root / 'data/land.geojson').read_text())
polys = []
for f in data['features']:
    g = f['geometry']
    for rings in ([g['coordinates']] if g['type'] == 'Polygon' else g['coordinates']):
        ring = rings[0]
        polys.append((min(p[0] for p in ring), min(p[1] for p in ring), max(p[0] for p in ring), max(p[1] for p in ring), rings))
def inside(x, y, ring):
    hit = False
    a = ring[-1]
    for b in ring:
        if (a[1] > y) != (b[1] > y) and x < (b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:
            hit = not hit
        a = b
    return hit
points = []
for i in range(100000):
    y = 1 - 2*(i+.5)/100000
    angle = i * math.pi*(3-math.sqrt(5))
    lat = math.degrees(math.asin(y))
    lon = (math.degrees(angle)+180)%360-180
    for xmin,ymin,xmax,ymax,rings in polys:
        if xmin<=lon<=xmax and ymin<=lat<=ymax and inside(lon,lat,rings[0]) and not any(inside(lon,lat,r) for r in rings[1:]):
            r = math.sqrt(1-y*y)
            points.extend([round(r*math.sin(angle),6),round(y,6),round(r*math.cos(angle),6)])
            break
(root/'data/land-points.json').write_text(json.dumps(points,separators=(',',':')))
print(f'Generated {len(points)//3} land points from 100,000 Fibonacci-sphere samples')
