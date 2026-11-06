# Globe Effect

A standalone interactive Three.js globe with animated flight arcs, camera tracking, and ripple effects. Originally created as a visual study for VA Astrolocality.

Open **astrolocality-globe.html** in a modern browser with WebGL enabled. This single file includes Three.js and land data; it needs no server, CDN, API, keys, or internet connection. It is a prototype, not integrated into VA web and not an astrology calculation.

## What was recreated

Reference: https://www.boardy.ai/ — observed in browser, including the site's actual public renderer with its public aggregated route feed mounted in a temporary local page overlay. This was necessary because the normal page initially rendered without route data. No remote changes were made.

- Cobalt sphere with soft directional shading, pale limb, and subtle 15-degree graticule.
- White circular dots sampled evenly over land: 28,825 land points from 100,000 Fibonacci-sphere samples.
- Thin translucent city-to-city route network, hidden behind the globe and subdued outside its silhouette.
- Raised great-circle arcs, a bright travelling head and illuminated travelled trail.
- Departure/arrival ripples that brighten, enlarge and slightly displace nearby land dots.
- Spring-damped longitude/latitude tracking with anticipation during travel.
- Floating city labels; drag rotation with inertia and three-second manual-control grace period.
- Pause, next-flight, reduced-motion initial pause, touch horizontal drag, and optional violet palette.

### Recovered behavior parameters

| Property | Reference value used |
| --- | --- |
| Departure dwell | 2.40 s |
| Flight | 1.45 s, cubic ease-in/out |
| Arrival dwell | 2.40 s |
| Fade | 0.45 s |
| Total cycle | 6.70 s |
| Arc height | 0.03 + 0.13 × angular distance, modulated by sin(pi × progress) |
| Surface clearance | 1.006 × globe radius |
| Camera spring rate | 7.5 |
| Camera anticipation | 0.12 s, with lead along route |
| Ripple angular speed | 0.42 rad/s |
| Drag takeover delay | 3 s |
| Camera field of view | 22 degrees |

## Deliberate differences / remaining fidelity limits

This is an independent behavior recreation, not a redistribution of Boardy's application bundle. It uses public-domain Natural Earth land polygons, not their embedded land mask; coastlines and point placement therefore differ. Illustrative routes are used instead of Boardy's live introduction data. Their endpoint shader is approximated with glow sprites. Label collision avoidance, adaptive device-quality tiers and the exact manual-to-auto timing blend are not reproduced. No pixel-identity or physical-phone usability claim is made.

For astrolocality, replace the illustrative `cities` / `pairs` in `globe.js` with calculated geographic endpoints/paths. The current curves are generic great-circle connections, **not** astrocartography/planetary angular lines. Computing such lines is separate work.

## Source

- `globe.js`: renderer, shaders, network geometry, labels, input, playback.
- `motion.mjs`: geographic projection, raised spherical arcs, spring and timing.
- `index.html`: small demonstration UI.
- `data/land.geojson`: Natural Earth 1:110m land polygons.
- `data/land-points.json`: precomputed dot cloud.
- `build_land.py`: regenerates the dot cloud with Python stdlib only.
- `build.py`: creates the offline single-file HTML.
- `test-motion.mjs`: Node built-in math/behavior tests.
Local inspection captures and reference bundles are intentionally excluded from this repository.

Run source locally:

```sh
git clone https://github.com/VerbalClaymore/Globe-Effect.git
cd Globe-Effect
python3 -m http.server 8766 --bind 127.0.0.1
```

Validate and package:

```sh
node --test test-motion.mjs
python3 build.py
```

Browser inspection hook: `window.globeStudy.getState()` reports frames, route, time, shader diagnostics and draw calls. `window.globeStudy.seek(routeIndex, seconds)` pauses at a deterministic frame for inspection; this sets a direct camera orientation, not the history-dependent live spring position. Judge tracking motion during playback rather than from seek frames.

## Verification

- Independent source-only review found no confirmed actionable blocker; reviewer did not execute the prototype. Browser checks below were performed separately.
- Six Node tests pass: unit geographic vectors, arc endpoint/altitude, antipodal/coincident finiteness, monotonic easing, spring convergence, timing boundaries.
- Real browser execution: all shader programs compile, live frame/time progression and automatic next-route transition observed.
- Offline file directly loaded and rendered.
- Pause holds time, next-flight advances route, actual CDP mouse drag changes orientation.
- Emulated reduced-motion preference starts paused.
- 390 CSS-pixel viewport inspected: no horizontal document overflow. This is emulation, not a physical phone test.
- Original renderer re-observed in departure/flight/arrival; reference screenshots retained separately from recreated frames.

## Third-party assets and provenance

Three.js 0.170.0 (MIT), vendored from https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js ; license in `vendor/THREE-LICENSE.txt`.

Natural Earth land polygons: https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_110m_land.geojson ; Natural Earth data is public domain: https://www.naturalearthdata.com/about/terms-of-use/ .

Reference-only browser assets were inspected at Boardy's public `/assets/connection-globe-cobalt-O0RYIM9_.js` and `/assets/connection-stage-renderer-DYjQdL9g.js`; these and the public introduction feed are excluded from this repository. Reference screenshots document comparison, not a license to reuse Boardy branding or its application.
