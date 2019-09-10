# -*- coding: utf-8 -*-
import os
import dash

from dash_bootstrap_components.themes import BOOTSTRAP

from .templates.index import render as layout

FONT_AWESOME = {
    'href': 'https://use.fontawesome.com/releases/v5.8.2/css/all.css',
    'rel': 'stylesheet',
    'integrity': 'sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay',
    'crossorigin': 'anonymous'
}

app = dash.Dash(__name__, external_stylesheets=[BOOTSTRAP, FONT_AWESOME])

# Sets the html template fo the dash application
file_path = os.path.dirname(os.path.realpath(__file__))
index_path = os.path.join(file_path, 'templates', 'index.html')
with open(index_path) as index_fs:
    app.index_string = index_fs.read()

app.layout = layout

app.title = "Gloomhaven Campaign Manager"
