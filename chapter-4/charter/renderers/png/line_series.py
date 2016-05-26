# charter.renderers.png.line_series
#
# Renderer for drawing a line series onto the chart in PNG format.

from PIL import ImageFont

from ...constants import *

#############################################################################

def draw(chart, drawer):
    avail_width  = CHART_WIDTH - Y_AXIS_WIDTH - MARGIN
    bucket_width = avail_width / len(chart['x_axis'])

    max_top      = TITLE_HEIGHT
    bottom       = CHART_HEIGHT - X_AXIS_HEIGHT
    avail_height = bottom - max_top

    left   = Y_AXIS_WIDTH
    prev_y = None
    for y_value in chart['series']:
        y = ((y_value - chart['y_min']) /
             (chart['y_max'] - chart['y_min']))

        cur_y = max_top + (avail_height - int(y * avail_height))

        if prev_y != None:
            drawer.line([(left - bucket_width / 2, prev_y),
                         (left + bucket_width / 2), cur_y],
                         fill="#4040a0", width=1)
        prev_y = cur_y
        left = left + bucket_width



