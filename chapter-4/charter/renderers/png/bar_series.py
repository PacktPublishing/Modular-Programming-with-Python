# charter.renderers.png.bar_series
#
# Renderer for drawing a bar series onto the chart in PNG format.

from PIL import ImageFont

from ...constants import *

#############################################################################

def draw(chart, drawer):
    avail_width  = CHART_WIDTH - Y_AXIS_WIDTH - MARGIN
    bucket_width = avail_width / len(chart['x_axis'])

    max_top      = TITLE_HEIGHT
    bottom       = CHART_HEIGHT - X_AXIS_HEIGHT
    avail_height = bottom - max_top

    left = Y_AXIS_WIDTH
    for y_value in chart['series']:
        bar_left = left + MARGIN / 2
        bar_right = left + bucket_width - MARGIN / 2

        y = ((y_value - chart['y_min']) /
             (chart['y_max'] - chart['y_min']))

        bar_top = max_top + (avail_height - int(y * avail_height))

        drawer.rectangle([(bar_left, bar_top),
                          (bar_right + 1,
                           bottom)],
                          fill="#e8e8f4", outline="#4040a0")

        left = left + bucket_width
