#!/bin/bash

chmod u+x main.py
xz -d Wordlists/rockyou*.xz
cat Wordlists/rockyou_pt_* > Wordlists/rockyou.txt
rm Wordlists/rockyou_pt_*
rm -- "$0"
