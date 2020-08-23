#!/bin/sh
search_dir=~/.leetcode
repo=~/Documents/LeetCode/leetCode/

for entry in $search_dir/*
do
    cp $entry $repo
done