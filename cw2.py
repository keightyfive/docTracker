#!/usr/bin/env python3
# name: cw2.py
# author: Kevin Klein

"""
ASSESSED COURSEWORK 2 - DATA ANALYSIS OF A DOCUMENT TRACKER
-----------------------------------------------------------
This is a simple Python-based application that analyses and
displays tracking data from a major website.
"""
# ----------------------------------------------------------
"""
libraries
"""
# importing libraries
import sys
import json  # for reading/writing JSON files
import os.path  # for isfile etc
import numpy as np  #
import matplotlib.pyplot as plt  # for plotting histograms
import httpagentparser  # for finding the main browser in task3a
import re  # read library
from pprint import pprint  # pretty print
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

# ---------------------------------------------------
"""
These dictionaries are used to assign countries of the json file to continents
"""
# dictionary assigning continents to shortcuts
continents = {
  'AF': 'Africa',
  'AS': 'Asia',
  'EU': 'Europe',
  'NA': 'North America',
  'SA': 'South America',
  'OC': 'Oceania',
  'AN': 'Antarctica'
}
# dictionary assigning countries to continents 
cntry_to_cont = {
  'AF': 'AS',
  'AX': 'EU',
  'AL': 'EU',
  'DZ': 'AF',
  'AS': 'OC',
  'AD': 'EU',
  'AO': 'AF',
  'AI': 'NA',
  'AQ': 'AN',
  'AG': 'NA',
  'AR': 'SA',
  'AM': 'AS',
  'AW': 'NA',
  'AU': 'OC',
  'AT': 'EU',
  'AZ': 'AS',
  'BS': 'NA',
  'BH': 'AS',
  'BD': 'AS',
  'BB': 'NA',
  'BY': 'EU',
  'BE': 'EU',
  'BZ': 'NA',
  'BJ': 'AF',
  'BM': 'NA',
  'BT': 'AS',
  'BO': 'SA',
  'BQ': 'NA',
  'BA': 'EU',
  'BW': 'AF',
  'BV': 'AN',
  'BR': 'SA',
  'IO': 'AS',
  'VG': 'NA',
  'BN': 'AS',
  'BG': 'EU',
  'BF': 'AF',
  'BI': 'AF',
  'KH': 'AS',
  'CM': 'AF',
  'CA': 'NA',
  'CV': 'AF',
  'KY': 'NA',
  'CF': 'AF',
  'TD': 'AF',
  'CL': 'SA',
  'CN': 'AS',
  'CX': 'AS',
  'CC': 'AS',
  'CO': 'SA',
  'KM': 'AF',
  'CD': 'AF',
  'CG': 'AF',
  'CK': 'OC',
  'CR': 'NA',
  'CI': 'AF',
  'HR': 'EU',
  'CU': 'NA',
  'CW': 'NA',
  'CY': 'AS',
  'CZ': 'EU',
  'DK': 'EU',
  'DJ': 'AF',
  'DM': 'NA',
  'DO': 'NA',
  'EC': 'SA',
  'EG': 'AF',
  'SV': 'NA',
  'GQ': 'AF',
  'ER': 'AF',
  'EE': 'EU',
  'ET': 'AF',
  'FO': 'EU',
  'FK': 'SA',
  'FJ': 'OC',
  'FI': 'EU',
  'FR': 'EU',
  'GF': 'SA',
  'PF': 'OC',
  'TF': 'AN',
  'GA': 'AF',
  'GM': 'AF',
  'GE': 'AS',
  'DE': 'EU',
  'GH': 'AF',
  'GI': 'EU',
  'GR': 'EU',
  'GL': 'NA',
  'GD': 'NA',
  'GP': 'NA',
  'GU': 'OC',
  'GT': 'NA',
  'GG': 'EU',
  'GN': 'AF',
  'GW': 'AF',
  'GY': 'SA',
  'HT': 'NA',
  'HM': 'AN',
  'VA': 'EU',
  'HN': 'NA',
  'HK': 'AS',
  'HU': 'EU',
  'IS': 'EU',
  'IN': 'AS',
  'ID': 'AS',
  'IR': 'AS',
  'IQ': 'AS',
  'IE': 'EU',
  'IM': 'EU',
  'IL': 'AS',
  'IT': 'EU',
  'JM': 'NA',
  'JP': 'AS',
  'JE': 'EU',
  'JO': 'AS',
  'KZ': 'AS',
  'KE': 'AF',
  'KI': 'OC',
  'KP': 'AS',
  'KR': 'AS',
  'KW': 'AS',
  'KG': 'AS',
  'LA': 'AS',
  'LV': 'EU',
  'LB': 'AS',
  'LS': 'AF',
  'LR': 'AF',
  'LY': 'AF',
  'LI': 'EU',
  'LT': 'EU',
  'LU': 'EU',
  'MO': 'AS',
  'MK': 'EU',
  'MG': 'AF',
  'MW': 'AF',
  'MY': 'AS',
  'MV': 'AS',
  'ML': 'AF',
  'MT': 'EU',
  'MH': 'OC',
  'MQ': 'NA',
  'MR': 'AF',
  'MU': 'AF',
  'YT': 'AF',
  'MX': 'NA',
  'FM': 'OC',
  'MD': 'EU',
  'MC': 'EU',
  'MN': 'AS',
  'ME': 'EU',
  'MS': 'NA',
  'MA': 'AF',
  'MZ': 'AF',
  'MM': 'AS',
  'NA': 'AF',
  'NR': 'OC',
  'NP': 'AS',
  'NL': 'EU',
  'NC': 'OC',
  'NZ': 'OC',
  'NI': 'NA',
  'NE': 'AF',
  'NG': 'AF',
  'NU': 'OC',
  'NF': 'OC',
  'MP': 'OC',
  'NO': 'EU',
  'OM': 'AS',
  'PK': 'AS',
  'PW': 'OC',
  'PS': 'AS',
  'PA': 'NA',
  'PG': 'OC',
  'PY': 'SA',
  'PE': 'SA',
  'PH': 'AS',
  'PN': 'OC',
  'PL': 'EU',
  'PT': 'EU',
  'PR': 'NA',
  'QA': 'AS',
  'RE': 'AF',
  'RO': 'EU',
  'RU': 'EU',
  'RW': 'AF',
  'BL': 'NA',
  'SH': 'AF',
  'KN': 'NA',
  'LC': 'NA',
  'MF': 'NA',
  'PM': 'NA',
  'VC': 'NA',
  'WS': 'OC',
  'SM': 'EU',
  'ST': 'AF',
  'SA': 'AS',
  'SN': 'AF',
  'RS': 'EU',
  'SC': 'AF',
  'SL': 'AF',
  'SG': 'AS',
  'SX': 'NA',
  'SK': 'EU',
  'SI': 'EU',
  'SB': 'OC',
  'SO': 'AF',
  'ZA': 'AF',
  'GS': 'AN',
  'SS': 'AF',
  'ES': 'EU',
  'LK': 'AS',
  'SD': 'AF',
  'SR': 'SA',
  'SJ': 'EU',
  'SZ': 'AF',
  'SE': 'EU',
  'CH': 'EU',
  'SY': 'AS',
  'TW': 'AS',
  'TJ': 'AS',
  'TZ': 'AF',
  'TH': 'AS',
  'TL': 'AS',
  'TG': 'AF',
  'TK': 'OC',
  'TO': 'OC',
  'TT': 'NA',
  'TN': 'AF',
  'TR': 'AS',
  'TM': 'AS',
  'TC': 'NA',
  'TV': 'OC',
  'UG': 'AF',
  'UA': 'EU',
  'AE': 'AS',
  'GB': 'EU',
  'US': 'NA',
  'UM': 'OC',
  'VI': 'NA',
  'UY': 'SA',
  'UZ': 'AS',
  'VU': 'OC',
  'VE': 'SA',
  'VN': 'AS',
  'WF': 'OC',
  'EH': 'AF',
  'YE': 'AS',
  'ZM': 'AF',
  'ZW': 'AF'
}

# -------------------------------------------------------------------------------------

"""
data processing methods
"""
# declaring the name of the file, in this case issuu_sample.json
file_name = 'sample_500k_lines.json'
# an array named data, an entire list of json data will be loaded into it
data = []

# open json file using the 'with' syntax, uft-8 encoding ------------------------------
with open(file_name, encoding='utf-8') as data_file:
    # looping through the data file, reading it line by line
    for i in data_file:
        # adding an item to the end of the list with the append function
        # at the same time, decoding json with loads function
        data.append(json.loads(i))  # ----------------------------------------------------

"""
TASK 2. views by country / continent: displays from which countries and continents the
        document has been viewed

TASK 2.a) Application takes string as an input which specifies a document
          and returns countries of viewers
"""
# method for task 2a ------------------------------------------------------------------
def task2a(document_id):
    # create a new dictionary
    counts = {}
    # looping through the array named data
    for n in data:
        # checking if the parameter document id is equal to the key "subject_doc_id" in the json file
        if document_id == n.get("subject_doc_id"):
            # checking for all visitor countries in the dictionary, accessing the key attribure
            if n.get("visitor_country") in counts.keys():
                # if we found something, we increment
                counts[n.get("visitor_country")] += 1
            else:
                # otherwise we update the dictionary
                counts.update({n.get("visitor_country"): 1})
    return counts  # -------------------------------------------------------------------


"""
TASK 2.b) Here, the data of countries previously collected is grouped by continents
          using the dictionary continents and cntry_to_cont declared at the top of this file
"""
# method for task 2b -----------------------------------------------------------------
def task2b(document_id):
    # using the data previously retrieved by storing data of task2a in a variable named countries
    countries = task2a(document_id)
    # create a new dictionary
    counts = {}
    # looping through the dictionary
    for i in countries.keys():
        # if an element in the dictionary named cntry_to_cont is in the dictionary counts
        if cntry_to_cont[i] in counts.keys():
            counts[cntry_to_cont[i]] += 1
        else:
            counts.update({cntry_to_cont[i]: 1})
    return counts  # --------------------------------------------------------------------


"""
TASK 3. Views by browser: identifying the most popular browser
        the application examines the file and counts the number of occurences for each value

TASK 3.a) The application returns all the browser identifiers of the viewers
"""
# method for task 3a -------------------------------------------------------------------
def task3a():
    # creating an new dictionary
    counts = {}
    # looping through the array data
    for m in data:
        # for one iterarion, if the key "visitor_useragent" is in the dictionary counts
        # if not we use get()
        if httpagentparser.simple_detect(m.get("visitor_useragent"))[1] in counts.keys():
            # incrementing
            counts[httpagentparser.simple_detect(m.get("visitor_useragent"))[1]] += 1
        # otherwise we update the dictionary
        else:
            counts.update({httpagentparser.simple_detect(m.get("visitor_useragent"))[1]: 1})
    return counts  # ---------------------------------------------------------------------


"""
TASK 3.b) The data previously collected in the above task distinguished as only the main browser name
"""
# method for task 3b -------------------------------------------------------------------
def task3b():
    # passing the data processed by task3a
    distinguish = task3a()
    # creating an new dictionary
    counts = {}
    # looping through
    for j in distinguish.keys():
        # using the findall function of the re library to find numbers in the strings
        # and only output the main browser name in order to distinguish them
        read = re.findall(".+ [0-9]", j)
        # looping through the shortend data
        for i in read:
            # for each browser name minus the first number
            if i[:-2] in counts.keys():
                #
                counts[i[:-2]] += distinguish[j]
            else:
                # update dictionary
                counts.update({i[:-2]: distinguish[j]})
    return counts  # --------------------------------------------------------------------


"""
TASK 4. Reader profiles: identifying the most avid readers
"""
def task4():
    # create a new dictionary
    counts = {}
    # loop through the array data
    for t in data:
        # if there is event readtime available
        if t.get("event_readtime") is not None:
            # if there is a subject doc id in the dictionary
            if t.get("subject_doc_id") in counts.keys():
                counts[t.get("subject_doc_id")] += t.get("event_readtime")
            else:
                counts.update({t.get("subject_doc_id"): t.get("event_readtime")})
    result = sorted(counts.items(), key=lambda t: t[1], reverse=True)[:10]
    return result

# -------------------------------------------------------------------

"""
TASK 5.
TASK 5.a) function takes document id as an argument and returns all visitor ids
"""
def task5a(document_id):
    # create a new dictionary
    counts = {}
    # looping through array
    for r in data:
        # checking if the passed doc id is in the array
        if document_id == r.get("subject_doc_id"):
            # checking if visitor if is in the dictionary
            if r.get("visitor_uuid") in counts.keys():
                counts[r.get("visitor_uuid")] += 1
            else:
                counts.update({r.get("visitor_uuid"): 1})
    return counts  # ---------------------------------------------------------------------


"""
TASK 5.b) function takes visitor id as an argument and returns all document ids read by this visitor
"""
def task5b(visitor_id):
    # create a new dictionary
    counts = {}
    for v in data:
        if visitor_id == v.get("visitor_uuid"):
            if v.get("subject_doc_id") in counts.keys():
                counts[v.get("subject_doc_id")] += 1
            else:
                counts.update({v.get("subject_doc_id"): 1})
    return counts  # ---------------------------------------------------------------------


"""
TASK 5.c) method generates an also liked documents list
"""
# high order function 
def task5c(document_id, visitor_id, sort):
    count = {}
    # new list for users
    users = []
    docs = {}
    # looping through data
    for c in data:
        # check if passed document_id is equal to document id in data
        if document_id == c.get("subject_doc_id") and c.get("event_type") == "read":
            # check if visitor is not ins users list
            if c.get("visitor_uuid") not in users:
                # if no then add him to users list
                users.append(c.get("visitor_uuid"))
    # looping through users list
    for u in users:
        # checking visitor id
        if not u == visitor_id:
            # calling other function
            temp = task5b(u)
            # append to list of documents
            docs.update(temp)
    if sort is not None:
        # sort the result
        result = sort(docs)
    else:
        result = docs
    return result  # ---------------------------------------------------------------------


"""
TASK 5.d) sorting function based on readership profile
"""
def task5d(stuff):
    counts = {}
    l = list(stuff.keys())
    # looping through data
    for g in data:
        # if the document id is in the list
        if g.get("subject_doc_id") in l:
          # check if the key event_readtime is there
            if not g.get("event_readtime") is None:
              # if it is in the dictionary counts
                if g.get("subject_doc_id") in counts.keys():
                  # we increment the count 
                    counts[g.get("subject_doc_id")] += g.get("event_readtime")
                  # otherwise the dictionary gets uodated  
                else:
                    counts.update({g.get("subject_doc_id"): g.get("event_readtime")})
    result = sorted(counts.items(), key=lambda t: t[1], reverse=True)
    return result  # ----------------------------------------------------------------------


"""
TASK 5.e) sorting function based on number of readers in the same document
"""
def task5e(data):
    result = sorted(data.items(), key=lambda t: t[1], reverse=True)
    return result  # -----------------------------------------------------------------------


"""
TASK 6.) shows passed method as histogram
"""
def show_histo(dict, title="title"):
    """Take a dictionary of counts and show it as a histogram."""
    plt.bar(range(len(dict)), list(dict.values()), align="center")
    plt.xticks(range(len(dict)), list(dict.keys()))
    plt.title(title)
    plt.show()  # ------------------------------------------------------------------------


"""
#---------------------------------------------------------------------------------------

calling methods down here for testing

#---------------------------------------------------------------------------------------

# with the array, we can access the document id
#print(data[1]["subject_doc_id"])
#calling method task2b with document id as argument
t = task2b("140101080405-6e5e88732ba9a4cb392c512322ec12b5")

show_histo(t,title="Number of countries represented, now using a function")
#show_histo(t,title="Number of countries represented, now using a function")
#task2b("140227072831-649625805917e1f042bdb1f645d588ff")
#task3a()
#task5a("140224195414-e5a9acedd5eb6631bb6b39422fba6798")
#task5b("232eeca785873d35")
#higherOrder(test)
#task5c("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", "b2a24f14bb5c9ea3", task5d)
"""
