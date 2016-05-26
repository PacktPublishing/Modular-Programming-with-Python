""" charter.renderers.renderer

    This module renders a given chart element in a given format.
"""
from .png import title       as title_png
from .png import x_axis      as x_axis_png
from .png import y_axis      as y_axis_png
from .png import bar_series  as bar_series_png
from .png import line_series as line_series_png

from .pdf import title       as title_pdf
from .pdf import x_axis      as x_axis_pdf
from .pdf import y_axis      as y_axis_pdf
from .pdf import bar_series  as bar_series_pdf
from .pdf import line_series as line_series_pdf

renderers = {
    'png' : {
        'title'       : title_png,
        'x_axis'      : x_axis_png,
        'y_axis'      : y_axis_png,
        'bar_series'  : bar_series_png,
        'line_series' : line_series_png
    },
    'pdf' : {
        'title'       : title_pdf,
        'x_axis'      : x_axis_pdf,
        'y_axis'      : y_axis_pdf,
        'bar_series'  : bar_series_pdf,
        'line_series' : line_series_pdf
    }
}

def draw(format, element, chart, output):
    renderers[format][element].draw(chart, output)

