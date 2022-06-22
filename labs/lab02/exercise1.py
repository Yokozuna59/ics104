##
# This program calculate the number of used tiles, gap on each side and number of used black and white tiles.
#

totalWidth = 23
print("Total width =", totalWidth)

tileWidth = 2
print("Tile width =", tileWidth)

# Write your code below this line
ADDITIONAL_BLACK_TILE = 1
sequenceLength = 2

# Calculate the of number of pairs in the whole sequence after the first black tile
widthWithoutBlackTile = totalWidth - tileWidth
numberOfWhilteBlackTilePairs = widthWithoutBlackTile // (sequenceLength * tileWidth)

# Calculate the number of tiles used in whole sequence
numberOfTiles = sequenceLength * numberOfWhilteBlackTilePairs + ADDITIONAL_BLACK_TILE
print("Number of tiles =", numberOfTiles)

# Calculate the length of gap on each side
lengthOfUsedTiles = numberOfTiles * tileWidth
totalGap = totalWidth - lengthOfUsedTiles
gapِAtEachEnd = totalGap / 2
print("Gapِ at each end =", gapِAtEachEnd)

# Calculate the number of black tiles with the first tile
numberOfBlackTiles = numberOfWhilteBlackTilePairs + ADDITIONAL_BLACK_TILE
print("Number of Black Tiles", numberOfBlackTiles)

# Calculate the number of white tiles
numberOfWhiteTiles = numberOfWhilteBlackTilePairs
print("Number of White Tiles", numberOfWhiteTiles)