# Lab 02

## Exercise 1

- Convert the following pseudo code into python. Run your program for different input values.
  - widthWithoutBlackTile = Total Width - Tile Width
  - Number of white-black tile pairs = the integer part of
    $$\frac{widthWithoutBlackTile}{(2 * TileWidth)}$$
  - Number of Tiles = 1 + 2 * Number of white-black tile pairs
  - Length of used tiles = Number of Tiles * Tile width
  - Total gap = Total Width - Length of used tiles
  - Gap at each end = Total gap / 2

**My Answer**: [lab02Ex1.py](lab02Ex1.py)

## Exercise 2

- Suppose the architect specifies a pattern with black, gray, and white tiles, like this:

<p align="center">
    <img src="https://user-images.githubusercontent.com/87622592/173446434-757b85ff-231d-4d9c-a3db-4e712ead10af.png" alt="sequence-image">
</p>

Again, the first and last tile should be black. Solve this problem by modifying the pseudo code of the previous exercise.

**My Answers**: Pseudo Code: [lab02Ex2_pseuso_code.md](lab02Ex2_pseuso_code.md), Python Code: [lab02Ex2.py](lab02Ex2.py)
