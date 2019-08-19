# -*- coding: utf-8 -*-
import os
import dash

from .templates.index import render as layout

app = dash.Dash(__name__)

app.layout = layout

app.title = "Gloomhaven Campaign Manager"
