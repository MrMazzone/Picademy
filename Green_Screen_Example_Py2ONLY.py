from SimpleCV import *

gs = Image("./../sampleimages/greenscreen.png")
background = Image("./../sampleimages/icecave.png")
matte = gs.hueDistance(color=Color.GREEN, minvalue = 40).binarize()
result = (gs-matte)+(background-matte.invert())
result.save('result.png')