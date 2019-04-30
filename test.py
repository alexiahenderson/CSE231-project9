#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:22:04 2019

@author: alexiapaige
"""

filename = input("Enter the name of the file: ")
while True:
    if filename == "" or filename == " ":
        filename = "pass.txt"
        fileopen = open("pass.txt", "r")
    else:
        try:
            fileopen = open(filename, "r")
            break
        except FileNotFoundError:
            print("file not found, try again.")
            print(filename)  

