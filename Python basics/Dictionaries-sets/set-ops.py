#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 16:01:37 2022

@author: ajit
"""

metroCities = {'Mumbai', 'Chennai', 'New Delhi', 'Pune', 'Bangalore', 'Hyderabad'}
coastalCities = {'Surat', 'Vizag', 'Chennai', 'Panaji', 'Mumbai', 'Cochin'}

print(type(metroCities))
print(type(coastalCities))

# 1) Metro cities which are also coastal.

metroAndCoastal = metroCities & coastalCities
print('\n', metroAndCoastal)

# 2) Either of them but not both

onlyMetroOrCoastal = metroCities ^ coastalCities
print('\n', onlyMetroOrCoastal)