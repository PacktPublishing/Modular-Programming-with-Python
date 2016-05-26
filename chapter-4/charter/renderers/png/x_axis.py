# charter.renderers.png.x_axis
#
# Renderer for drawing an X axis onto the chart in PNG format.

from PIL import ImageFont

from ...constants import *

#############################################################################

def draw(chart, drawer):
    font = ImageFont.truetype("Helvetica", 12)
    label_height = font.getsize("Test")[1]

    avail_width  = CHART_WIDTH - Y_AXIS_WIDTH - MARGIN
    bucket_width = avail_width / len(chart['x_axis'])

    axis_top = CHART_HEIGHT - X_AXIS_HEIGHT
    drawer.line([(Y_AXIS_WIDTH, axis_top), (CHART_WIDTH - MARGIN, axis_top)],
                "#4040a0", 2) # Draw main axis line.

    left = Y_AXIS_WIDTH
    for bucket_num in range(len(chart['x_axis'])):
        drawer.line([(left, axis_top), (left, axis_top + TICKMARK_HEIGHT)],
                "#4040a0", 1) # Draw tickmark

        label_width = font.getsize(chart['x_axis'][bucket_num])[0]
        label_left = max(left, left + bucket_width/2 - label_width/2)
        label_top  = axis_top + TICKMARK_HEIGHT + 4

        drawer.text((label_left, label_top), chart['x_axis'][bucket_num],
                    "#000000", font)

        left = left + bucket_width

    drawer.line([(left, axis_top), (left, axis_top + TICKMARK_HEIGHT)],
                "#4040a0", 1) # Draw final tickmark.
