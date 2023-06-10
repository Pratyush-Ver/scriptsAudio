#!/bin/sh
#sound card verification
#card number identification
#

card = $(arecord -l | grep card | awk '{print $2}' | sed 's/://g';)
device = $(arecord -l | grep card | awk '{print $8}' | sed 's/://g';)
