# charter.renderers.png.y_axis
#
# Renderer for drawing a Y-axis onto the chart in PNG format.

from PIL import ImageFont

from ...constants import *

#############################################################################

def draw(chart, drawer):
    font = ImageFont.truetype("Helvetica", 12)
    label_height = font.getsize("Test")[1]

    axis_top    = TITLE_HEIGHT
    axis_bottom = CHART_HEIGHT - X_AXIS_HEIGHT
    axis_height = axis_bottom - axis_top

    drawer.line([(Y_AXIS_WIDTH, axis_top),
                 (Y_AXIS_WIDTH, axis_bottom)],
                 "#4040a0", 2) # Draw main axis line.

    for y_value in chart['y_labels']:
        y = ((y_value - chart['y_min']) /
             (chart['y_max'] - chart['y_min']))
        
        y_pos = axis_top + (axis_height - int(y * axis_height))

        drawer.line([(Y_AXIS_WIDTH - TICKMARK_HEIGHT, y_pos),
                     (Y_AXIS_WIDTH, y_pos)],
                     "#4040a0", 1) # Draw tickmark.

        label_width,label_height = font.getsize(str(y_value))
        label_left = Y_AXIS_WIDTH - TICKMARK_HEIGHT - label_width - 4
        label_top = y_pos - label_height / 2

        drawer.text((label_left, label_top), str(y_value),
                    "#000000", font)


