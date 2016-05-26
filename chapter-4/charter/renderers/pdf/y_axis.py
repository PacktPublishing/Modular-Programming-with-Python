# charter.renderers.pdf.y_axis
#
# Renderer for drawing a Y axis onto the chart in PDF format.

from ...constants import *

#############################################################################

def draw(chart, canvas):
    label_height = 12 * 1.2

    axis_top    = CHART_HEIGHT - TITLE_HEIGHT
    axis_bottom = X_AXIS_HEIGHT
    axis_height = axis_top - axis_bottom

    # Draw main axis line.

    canvas.setStrokeColorRGB(0.25, 0.25, 0.625)
    canvas.setLineWidth(2)
    canvas.line(Y_AXIS_WIDTH, axis_top, Y_AXIS_WIDTH, axis_bottom)

    for y_value in chart['y_labels']:
        y = ((y_value - chart['y_min']) /
             (chart['y_max'] - chart['y_min']))

        y_pos = axis_bottom + int(y * axis_height)

        # Draw tickmark.

        canvas.setLineWidth(1)
        canvas.line(Y_AXIS_WIDTH - TICKMARK_HEIGHT, y_pos,
                    Y_AXIS_WIDTH, y_pos)

        # Draw label.

        label_width = canvas.stringWidth(str(y_value),
                                         "Helvetica", 12)
        label_left   = Y_AXIS_WIDTH - TICKMARK_HEIGHT - label_width - 4
        label_bottom = y_pos - label_height/4

        canvas.setFont("Helvetica", 12)
        canvas.setFillColorRGB(0.0, 0.0, 0.0)
        canvas.drawString(label_left, label_bottom, str(y_value))

