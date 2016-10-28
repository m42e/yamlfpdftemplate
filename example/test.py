#!/usr/bin/env python3

from yafte import YaFTe
import datetime



f = YaFTe('template.yaml')

f["info"] = "Created at "+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

f.add_page(info='This is fucking great!', info2='this is now something else')
f.add_page(info='And again something new')

#and now we render the page
f.output("./example.pdf")





