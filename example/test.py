#!/usr/bin/env python3

from yafte import YaFTe
import datetime



f = YaFTe('template.yaml')
f.add_page()

f["info"] = "Created at "+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

#and now we render the page
f.render("./example.pdf")





