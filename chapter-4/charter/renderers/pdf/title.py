# charter.renderers.pdf.title
#
# Renderer for drawing a title onto the chart in PDF format.

from ...constants import *

#############################################################################

def draw(chart, canvas):
    text_width  = canvas.stringWidth(chart['title'], "Helvetica", 24)
    text_height = 24 * 1.2

    left   = CHART_WIDTH/2 - text_width/2
    bottom = CHART_HEIGHT - TITLE_HEIGHT/2 + text_height/2

    canvas.setFont("Helvetica", 24)
    canvas.setFillColorRGB(0.25, 0.25, 0.625)
    canvas.drawString(left, bottom, chart['title'])

