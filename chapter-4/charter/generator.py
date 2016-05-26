""" generator.py

    This module implements the chart-generation logic for the Charter package.
"""
from PIL import Image, ImageDraw

from reportlab.pdfgen.canvas import Canvas

from .constants import *
from .renderers import renderer

#############################################################################

def generate_chart(chart, filename):
    if filename.lower().endswith(".pdf"):
        format = "pdf"
    elif filename.lower().endswith(".png"):
        format = "png"
    else:
        print("Unsupported file format: " + filename)
        return

    if format == "pdf":
        output = Canvas(filename)
    elif format == "png":
        image  = Image.new("RGB", (CHART_WIDTH, CHART_HEIGHT),
                           "#ffffff")
        output = ImageDraw.Draw(image)

    renderer.draw(format, "title",  chart, output)
    renderer.draw(format, "x_axis", chart, output)
    renderer.draw(format, "y_axis", chart, output)
    if chart['series_type'] == "bar":
        renderer.draw(format, "bar_series", chart, output)
    elif chart['series_type'] == "line":
        renderer.draw(format, "line_series", chart, output)

    if format == "pdf":
        output.showPage()
        output.save()
    elif format == "png":
        image.save(filename, format="png")

