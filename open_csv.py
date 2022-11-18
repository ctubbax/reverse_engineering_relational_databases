# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:19:31 2022

@author: carlo

This function opens a csv file and converts it to an array with dictionaries

"""
import csv
def open_csv(file_name):

    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        file = []
        for row in reader:
            file.append(row)

    return file
