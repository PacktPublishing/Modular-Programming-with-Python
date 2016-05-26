# charter.renderers.pdf.line_series
#
# Renderer for drawing a line series onto the chart in PDF format.

from ...constants import *

#############################################################################

def draw(chart, canvas):
    avail_width  = CHART_WIDTH - Y_AXIS_WIDTH - MARGIN
    bucket_width = avail_width / len(chart['x_axis'])

    bottom       = X_AXIS_HEIGHT
    max_top      = CHART_HEIGHT - TITLE_HEIGHT
    avail_height = max_top - bottom

    left   = Y_AXIS_WIDTH
    prev_y = None
    for y_value in chart['series']:
        y = ((y_value - chart['y_min']) /
             (chart['y_max'] - chart['y_min']))

        cur_y = bottom + int(y * avail_height)

        if prev_y != None:
            canvas.setStrokeColorRGB(0.25, 0.25, 0.625)
            canvas.setLineWidth(1)
            canvas.line(left - bucket_width / 2, prev_y,
                        left + bucket_width / 2, cur_y)

        prev_y = cur_y
        left = left + bucket_width

