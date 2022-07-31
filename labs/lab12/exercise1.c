#include <stdio.h>
#define ADDITIONAL_BLACK_TILE 1

int main(void) {
    int totalWidth, tileWidth, widthWithOutBlackTile,
        numberOfWhiteBlackTilePairs, numberOfTiles,
        numberOfBlackTiles, numberOfWhiteTiles,
        lengthOfTilesUsed, totalGap;

    double gapOnEashSide;

    totalWidth = 23;
    tileWidth = 2;

    widthWithOutBlackTile = totalWidth - tileWidth;
    numberOfWhiteBlackTilePairs = widthWithOutBlackTile/(2 * tileWidth);
    numberOfTiles = 1 + 2 * numberOfWhiteBlackTilePairs;
    lengthOfTilesUsed = numberOfTiles * tileWidth;
    totalGap = totalWidth - lengthOfTilesUsed;
    gapOnEashSide = totalGap / 2.0;

    numberOfBlackTiles = numberOfWhiteBlackTilePairs + ADDITIONAL_BLACK_TILE;
    numberOfWhiteTiles = numberOfWhiteBlackTilePairs;

    printf("Total Width = %d\n", totalWidth);
    printf("Tile width = %d\n", tileWidth);
    printf("Number of tiles %d\n", numberOfTiles);
    printf("Gap on each sides = %.1lf\n", gapOnEashSide);
    printf("Number of black tiles %d\n", numberOfBlackTiles);
    printf("Number of white tiles %d\n", numberOfWhiteTiles);
}