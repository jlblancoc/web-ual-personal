#!/usr/bin/env python3
"""Render GPS paths from KML files as small static SVG thumbnails.

Used for the per-sequence "path overview" images of the Malaga Urban Dataset.
The SVGs are self-contained (no map tiles, no scripts), so pages load fast and
do not depend on any third-party service.

Usage:
    tools/make_path_svgs.py KML_DIR OUT_DIR

KML_DIR must contain "malaga-urban-dataset-extract-NN_CAM_GPS.kml" for each
extract and, optionally, "full.kml" with the path of the entire dataset.
"""
import math
import re
import sys
from pathlib import Path

WIDTH = 400
HEIGHT = 260
PAD = 26
EARTH_RADIUS = 6371000.0


def read_path(kml_file):
    """Returns a list of (lon, lat) tuples from all LineStrings in a KML file."""
    text = Path(kml_file).read_text(encoding='utf-8')
    points = []
    for block in re.findall(r'<coordinates>(.*?)</coordinates>', text, re.S):
        for item in block.split():
            fields = item.split(',')
            points.append((float(fields[0]), float(fields[1])))
    return points


def to_meters(points, lat0):
    """Local equirectangular projection, in meters, with y pointing up."""
    kx = math.radians(1.0) * EARTH_RADIUS * math.cos(math.radians(lat0))
    ky = math.radians(1.0) * EARTH_RADIUS
    return [(lon * kx, lat * ky) for lon, lat in points]


def path_length(xy):
    total = 0.0
    for a, b in zip(xy, xy[1:]):
        total += math.hypot(b[0] - a[0], b[1] - a[1])
    return total


def nice_scale(extent_m):
    """Largest 1/2/5 x 10^n length not exceeding a third of the extent."""
    target = extent_m / 3.0
    magnitude = 10 ** math.floor(math.log10(target))
    for factor in (5, 2, 1):
        if factor * magnitude <= target:
            return factor * magnitude
    return magnitude


def render(points, title, width=WIDTH, height=HEIGHT, background=None):
    lat0 = sum(p[1] for p in points) / len(points)
    xy = to_meters(points, lat0)
    xs = [p[0] for p in xy]
    ys = [p[1] for p in xy]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    span_x = max(max_x - min_x, 1.0)
    span_y = max(max_y - min_y, 1.0)
    scale = min((width - 2 * PAD) / span_x, (height - 2 * PAD - 12) / span_y)
    off_x = (width - span_x * scale) / 2.0 - min_x * scale
    off_y = (height - 12 - span_y * scale) / 2.0 + max_y * scale

    def px(p):
        return off_x + p[0] * scale, off_y - p[1] * scale

    # Keep SVGs small: at most about 1500 vertices per path
    step = max(1, len(xy) // 1500)
    drawn = xy[::step]
    if drawn[-1] != xy[-1]:
        drawn.append(xy[-1])
    coords = ' '.join('%.1f,%.1f' % px(p) for p in drawn)
    sx, sy = px(xy[0])
    ex, ey = px(xy[-1])

    bar_m = nice_scale(max(span_x, span_y))
    bar_px = bar_m * scale
    bar_label = ('%d km' % (bar_m / 1000)) if bar_m >= 1000 else ('%d m' % bar_m)
    bar_x = 12
    bar_y = height - 12

    out = []
    out.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" '
               'width="%d" height="%d" role="img">' % (width, height, width, height))
    out.append('<title>%s</title>' % title)
    out.append('<rect width="%d" height="%d" rx="6" fill="#f3f4f6"/>' % (width, height))
    if background:
        out.append(background(px))
    out.append('<polyline points="%s" fill="none" stroke="#d9480f" stroke-width="3" '
               'stroke-linejoin="round" stroke-linecap="round"/>' % coords)
    out.append('<circle cx="%.1f" cy="%.1f" r="5" fill="#2f9e44" stroke="#fff" stroke-width="1.5"/>'
               % (sx, sy))
    out.append('<circle cx="%.1f" cy="%.1f" r="5" fill="#1c1c1c" stroke="#fff" stroke-width="1.5"/>'
               % (ex, ey))
    out.append('<path d="M%.1f %.1fv-4h%.1fv4" fill="none" stroke="#555" stroke-width="1.5"/>'
               % (bar_x, bar_y, bar_px))
    out.append('<text x="%.1f" y="%.1f" font-family="sans-serif" font-size="11" fill="#555">%s</text>'
               % (bar_x + bar_px + 6, bar_y, bar_label))
    out.append('</svg>')
    return '\n'.join(out) + '\n', path_length(xy)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    kml_dir = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    for kml in sorted(kml_dir.glob('malaga-urban-dataset-extract-*_CAM_GPS.kml')):
        num = re.search(r'extract-(\d+)_', kml.name).group(1)
        svg, length = render(read_path(kml), 'GPS path of extract #%s' % num)
        (out_dir / ('extract-%s.svg' % num)).write_text(svg, encoding='utf-8')
        print('extract %s: %.0f m' % (num, length))

    full = kml_dir / 'full.kml'
    if full.exists():
        svg, length = render(read_path(full), 'GPS path of the entire dataset',
                             width=800, height=520)
        (out_dir / 'full.svg').write_text(svg, encoding='utf-8')
        print('full: %.0f m' % length)
    return 0


if __name__ == '__main__':
    sys.exit(main())
