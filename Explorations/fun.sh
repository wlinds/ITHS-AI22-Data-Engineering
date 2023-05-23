#!/bin/bash
# This is a fun shell script that greets you and tells you the date and 
time

USER=$(whoami)
DATE=$(date +"%A, %B %d, %Y")
TIME=$(date +"%I:%M %p")

say -r 250 "Whats up, $USER. Today is $DATE. The time is $TIME. Keep it 
real dawg."
