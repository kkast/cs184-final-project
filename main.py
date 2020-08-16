
from fontTools import ttLib


tt = ttLib.TTFont("FontAwesome.ttf")
tt.saveXML("FontAwesome.xml")


# from fontTools.ttLib import TTFont
#
# p = 'example.ttf'
#
# f = TTFont(p)
# cmap = f.getBestCmap()  # look up the encoding
#
# for char in sorted(cmap):
#     print(chr(char))
