#!/usr/bin/env python3

from music21 import note, stream, duration

# Create a stream for the melody
melody = stream.Stream()

# Define the notes and durations for the melody
notes = [
  ("C", 4), ("E", 4), ("G", 4),
  ("C5", 2), ("C5", 2),
  ("G", 4), ("E", 4), ("C", 4),
  ("G", 2), ("G", 2),
  ("E", 4), ("C", 4), ("G", 4),
  ("E", 2), ("E", 2)
]

# Add the notes to the melody
for pitch, duration in notes:
  n = note.Note(pitch)
  n.duration = duration.Duration(1/duration)
  melody.append(n)

# Play the melody
melody.show("midi")
