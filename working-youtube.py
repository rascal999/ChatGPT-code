#!/usr/bin/env python3

import webbrowser
import random

# Define a list of YouTube video URLs.
videos = [
  "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "https://www.youtube.com/watch?v=gvdf5n-zI14",
  "https://www.youtube.com/watch?v=Uw5Ij56ZhNs",
  "https://www.youtube.com/watch?v=rYEDA3JcQqw",
  "https://www.youtube.com/watch?v=Ls_zvbLlKZ8",
]

# Generate a random number to select a video from the list.
index = random.randint(0, len(videos) - 1)

# Open the selected video in the default web browser.
webbrowser.open(videos[index])
