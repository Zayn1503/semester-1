# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
music = {
    "Drake" : [("ICEMAN", 2026), ("Views", 2016), ("Take Care", 2011)],
    "Travis Scott" : [("ASTROWORLD", 2018), ("UTOPIA", 2023), ("Birds In The Trap Sing McKnight", 2016)],
    "PARTYNEXTDOOR" : [("PARTYPACK", 2020), ("PARTYMOBILE", 2020), ("Seven Days", 2017)]
}

# (keys are artist names, values are lists of album names)

# Pretty-print the data structure

pprint(music)

# Display details of one album recorded by a specific artist
