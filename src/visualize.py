#!/usr/bin/env python3


# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()


# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)


# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]


# print the count values
# change to Reverse = False because we want it from small to big in the plot
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=False)
for k,v in items:
        print(k,':',v)


# get the biggest 10 items of items
first_10_items = items[-10:]


# set the language of hashtag in the title of plots
if args.key == "#coronavirus":
    lang = "English"
else: 
    lang = "Korean"


# unzip it: separate key and value into 2 lists
k, v = zip(*first_10_items)


# build the bar plot
if args.input_path == "reduced.lang":
    x = "Language"
if args.input_path == "reduced.country":
    x = "Country"

plt.bar([i for i in range(len(k))], v, color = 'yellow', width = 0.6) # assign 1 to 10 to each top ten number of tweets because in this way it won't order the x-axis alphabetically be default
plt.xlabel(x)
plt.title("#coronavirus Tweets in " + lang + " in 2020 By " + x) 
plt.xticks([i for i in range(len(k))], k) # replace the 1-10 number with the code of countries
plt.savefig(x + "_" + lang + ".png")

