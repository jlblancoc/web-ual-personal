#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Production settings, used by `make publish` and `make ftp_upload`.
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401,F403

SITEURL = 'https://w3.ual.es/~jlblanco'
RELATIVE_URLS = False

SITELOGO = '%s/%s' % (SITEURL, SITELOGO_PATH)
FAVICON = '%s/%s' % (SITEURL, FAVICON_PATH)

DELETE_OUTPUT_DIRECTORY = True
