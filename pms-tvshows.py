#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests as R

res = R.get("http://0.0.0.0:32400/library/sections/3/refresh")
if res.ok: print "Section 'TV Shows' updated!!"
