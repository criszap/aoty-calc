import calc
import reform

dir = "D:\+++\CODING\AOTY Score Calculator\moosic.txt"

moosic_f = open(dir, "r", encoding="utf-8")
calc.calcScore(moosic_f.read())
moosic_f.close()

moosic_f = open(dir, "r", encoding="utf-8")
reform.aotyFormat(moosic_f.read())
moosic_f.close()


# FILE FORMAT:

# ALBUM
# TITLE
#
# [1] Track 1
# Scores Are
#
# [2] Track 2
# Out Of 100
#
# [3] Track 3
# Example Below
#
# [4] Through Me
# 95