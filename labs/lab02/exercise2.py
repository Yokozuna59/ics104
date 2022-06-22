##
# This program calculate the number of tiles used, gap on each side and number of used black, white and gray tiles.
#

totalWidth = 26
print("Total width =", totalWidth)

tileWidth = 1
print("Tile width =", tileWidth)

# Write your code below this line
ADDITIONAL_BLACK_TILE = 1
sequenceLength = 4

# Calculate the of number of groups in the whole sequence after the first black tile
widthWithoutBlackTile = totalWidth - tileWidth
numberOfWhilteBlackGrayTileGroup = widthWithoutBlackTile // (ADDITIONAL_BLACK_TILE * tileWidth)

# Calculate the number of tiles used in whole sequence
numberOfTiles = sequenceLength * numberOfWhilteBlackGrayTileGroup + ADDITIONAL_BLACK_TILE
print("Number of tiles =", numberOfTiles)

# Calculate the length of gap on each side
lengthOfUsedTiles = numberOfTiles * tileWidth
totalGap = totalWidth - lengthOfUsedTiles
gapِAtEachEnd = totalGap / 2
print("Gapِ at each end =", gapِAtEachEnd)

# Calculate the number of black tiles with the first tile
numberOfBlackTiles = numberOfWhilteBlackGrayTileGroup + 1
print("Number of Black Tiles", numberOfBlackTiles)

# Calculate the number of white tiles
numberOfWhiteTiles = numberOfWhilteBlackGrayTileGroup
print("Number of White Tiles", numberOfWhiteTiles)

# Calculate the number of gray tiles
numberOfGrayTiles = 2 * numberOfWhilteBlackGrayTileGroup
print("Number of Gray Tiles", numberOfGrayTiles)