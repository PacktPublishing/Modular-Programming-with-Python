# charter.renderers.pdf.x_axis
#
# Renderer for drawing an X axis onto the chart in PDF format.

from ...constants import *

#############################################################################

def draw(chart, canvas):
    label_height = 12 * 1.2

    avail_width  = CHART_WIDTH - Y_AXIS_WIDTH - MARGIN
    bucket_width = avail_width / len(chart['x_axis'])

    # Draw main axis line.

    axis_top = X_AXIS_HEIGHT
    canvas.setStrokeColorRGB(0.25, 0.25, 0.625)
    canvas.setLineWidth(2)
    canvas.line(Y_AXIS_WIDTH, axis_top, CHART_WIDTH - MARGIN, axis_top)

    left = Y_AXIS_WIDTH
    for bucket_num in range(len(chart['x_axis'])):

        # Draw tickmark.

        canvas.setLineWidth(1)
        canvas.line(left, axis_top, left, axis_top - TICKMARK_HEIGHT)

        # Draw label.

        label_width  = canvas.stringWidth(chart['x_axis'][bucket_num],
                                          "Helvetica", 12)
        label_left   = max(left, left + bucket_width/2 - label_width/2)
        label_bottom = axis_top - TICKMARK_HEIGHT - 4 - label_height

        canvas.setFont("Helvetica", 12)
        canvas.setFillColorRGB(0.0, 0.0, 0.0)
        canvas.drawString(label_left, label_bottom,
                          chart['x_axis'][bucket_num])

        left = left + bucket_width

    # Draw final tickmark.

    canvas.setStrokeColorRGB(0.25, 0.25, 0.625)
    canvas.setLineWidth(1)
    canvas.line(left, axis_top, left, axis_top - TICKMARK_HEIGHT)

