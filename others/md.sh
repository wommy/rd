#!/bin/bash
# ask user for location and title

read -p 'location? ' loc
read -p 'title? ' title

echo $(date)-$loc-$title >> $(date +"%m_%d_%H%M")-$loc-$title
vim $(date +"%m_%d_%H%M")-$loc-$title
