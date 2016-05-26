""" chart.py

    This module implements the chart-related functions for the Charter package.
"""
def new_chart():
    return {}

def set_title(chart, title):
    chart['title'] = title

def set_x_axis(chart, x_axis):
    chart['x_axis'] = x_axis

def set_y_axis(chart, minimum, maximum, labels):
    chart['y_min']    = minimum
    chart['y_max']    = maximum
    chart['y_labels'] = labels

def set_series_type(chart, series_type):
    chart['series_type'] = series_type

def set_series(chart, series):
    chart['series'] = series

