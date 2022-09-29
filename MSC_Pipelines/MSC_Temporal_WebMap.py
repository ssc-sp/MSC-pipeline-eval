# Databricks notebook source
# install additional required libraries
%pip install tabulate
%pip install OWSLib
%pip install plotly
%pip install geopandas

# COMMAND ----------

# import libraries and initiate parameters
from datetime import datetime, timedelta
import re
import warnings

# The following modules must first be installed to use 
# this code out of Jupyter Notebook
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy
from owslib.wms import WebMapService
import pandas
from tabulate import tabulate

# Ignore warnings from the OWSLib module
warnings.filterwarnings('ignore', module='owslib', category=UserWarning)

# Parameters choice
# Layer:
layer = 'RADAR_1KM_RRAI'
# Coordinates:
y, x = 49.288, -123.116
# Local time zone (in this exemple, the local time zone is UTC-07:00):
time_zone = -7

# COMMAND ----------

wms = WebMapService('https://geo.weather.gc.ca/geomet?SERVICE=WMS' +
                    '&REQUEST=GetCapabilities',
                    version='1.3.0',
                    timeout=300)
frameRate = 1

