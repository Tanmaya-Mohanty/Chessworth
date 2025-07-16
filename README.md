# Chessworth
Chessworth is a variant of chess that is quite similar to standard chess, expect for when a weaker piece (piece having relatively less worth e.g. pawn) captures a stronger piece (e.g. a knight), both of them get off the board.

This rule adds a unique layer of strategic depth and sacrifice.

## Features

- Built on top of the `python-chess` library.
- Enforces standard rules plus the **mutual destruction rule**.
- Detects check, checkmate, stalemate, and illegal moves.
- Playable in Jupyter Notebook with interactive SVG board.

## Mutual Destruction Rule

If a lower-value piece (e.g. a pawn) captures a higher-value piece (e.g. a rook), **both pieces are removed**.

| Piece    | Value |
|----------|-------|
| Pawn     | 1     |
| Knight   | 3     |
| Bishop   | 3     |
| Rook     | 5     |
| Queen    | 9     |
| King     | ∞     |

## Requirements

- Python 3.7+
- `python-chess`
- `IPython`

Install them with:

```bash
pip install python-chess ipython
