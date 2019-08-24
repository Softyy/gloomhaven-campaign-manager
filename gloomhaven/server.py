# -*- coding: utf-8 -*-
import os
import dash

from dash_bootstrap_components.themes import BOOTSTRAP

from .templates.index import render as layout

app = dash.Dash(__name__, external_stylesheets=[BOOTSTRAP])

app.layout = layout

app.title = "Gloomhaven Campaign Manager"
