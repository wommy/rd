#!/bin/bash
# ask user for location and topic

echo where are you
read -p 'location: ' location
echo whats this about
read -p 'topic: ' topic

echo $(date)-$location-$topic >> $(date +"%m_%d_%H%M")-$location-$topic
