"""Package the study as an offline, single-file HTML artifact."""
from pathlib import Path
import base64
root=Path(__file__).parent
source=(root/'globe.js').read_text()
for file in ['vendor/three.module.js','motion.mjs']:
    uri='data:text/javascript;base64,'+base64.b64encode((root/file).read_bytes()).decode()
    source=source.replace(f"'./{file}'",repr(uri))
start=source.index("const land=await fetch(")
end=source.index('\n',start)
source=source[:start]+'const land='+(root/'data/land-points.json').read_text()+';'+source[end:]
html=(root/'index.html').read_text().replace('<script type="module" src="./globe.js"></script>','<script type="module">\n'+source.replace('</script','<\\/script')+'\n</script>')
(root/'astrolocality-globe.html').write_text(html)
print(f'Built offline HTML: {len(html.encode()):,} bytes')
