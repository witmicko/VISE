#!/usr/bin/env python
import os
import yaml

with open(os.path.join(os.path.dirname(__file__), 'settings.yaml')) as settings:
    settings = yaml.load(settings)
