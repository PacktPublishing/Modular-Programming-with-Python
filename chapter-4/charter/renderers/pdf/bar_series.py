# charter.renderers.pdf.line_series
#
# Renderer for drawing a bar series onto the chart in PDF format.

from ...constants import *

#############################################################################

def draw(chart, canvas):
    avail_width  = CHART_WIDTH - Y_AXIS_WIDTH - MARGIN
    bucket_width = avail_width / len(chart['x_axis'])

    bottom       = X_AXIS_HEIGHT
    max_top      = CHART_HEIGHT - TITLE_HEIGHT
    avail_height = max_top - bottom

    left = Y_AXIS_WIDTH
    for y_value in chart['series']:
        bar_left  = left + MARGIN / 2
        bar_width = bucket_width - MARGIN

        y = ((y_value - chart['y_min']) /
             (chart['y_max'] - chart['y_min']))

        bar_height = int(y * avail_height)

        canvas.setStrokeColorRGB(0.25, 0.25, 0.625)
        canvas.setFillColorRGB(0.906, 0.906, 0.953)
        canvas.rect(bar_left, bottom, bar_width, bar_height,
                    stroke=True, fill=True)

        left = left + bucket_width

