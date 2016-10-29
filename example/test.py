#!/usr/bin/env python3
from yafte import YaFTe
import datetime

# read the templafe from template.yaml
f = YaFTe('template.yaml')

# set a default text for the info text
f["info"] = "Created at "+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

# this adds a page and sets info and info2 to the specified value
f.add_page(info='This is really great!', info2='this is now something else')
# this uses the default value for info and only sets info2
f.add_page(info2='And again something new')

# This writes the pdf
f.output("./example.pdf")





