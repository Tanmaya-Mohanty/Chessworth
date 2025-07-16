import chess
import chess.svg
import webbrowser
import os


class ChessworthBoard(chess.Board):
    """
    A chess board that implements standard rules with an additional custom rule:
    If a lower-value piece captures a higher-value one, both are removed from the board.
    """

    PIECE_VALUES = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: float('inf')
    }

    def push_custom(self, move):
        if move not in self.legal_moves:
            raise ValueError("Illegal move.")

        is_capture = self.is_capture(move)
        is_en_passant = self.is_en_passant(move)

        if is_capture:
            capturing_piece = self.piece_at(move.from_square)
            if not capturing_piece:
                raise ValueError("No capturing piece found at source square.")

            capturing_type = move.promotion if move.promotion else capturing_piece.piece_type

            if is_en_passant:
                captured_square = move.to_square + (8 if self.turn else -8)
                captured_piece = chess.Piece(chess.PAWN, not self.turn)
            else:
                captured_square = move.to_square
                captured_piece = self.piece_at(captured_square)

            if not captured_piece or captured_piece.piece_type == chess.KING:
                raise ValueError("Invalid capture!")

            capturing_value = self.PIECE_VALUES[capturing_type]
            captured_value = self.PIECE_VALUES[captured_piece.piece_type]

            if capturing_value < captured_value:
                self.remove_piece_at(move.from_square)
                self.remove_piece_at(captured_square)
                self.turn = not self.turn
                self.halfmove_clock = 0
                self.ep_square = None
                if not self.turn:
                    self.fullmove_number += 1
                return "mutual"

        test_board = self.copy(stack=True)
        chess.Board.push(test_board, move)
        if test_board.is_check() and test_board.turn == self.turn:
            raise ValueError("Move leaves your king in check!")

        super().push(move)
        return "normal"

    def show(self):
        """Save SVG and open in browser."""
        svg_code = chess.svg.board(self, size=500)
        with open("board.svg", "w", encoding="utf-8") as f:
            f.write(svg_code)
        print("Opening board.svg in browser...")
        webbrowser.open('file://' + os.path.realpath("board.svg"))


def play_game():
    board = ChessworthBoard()
    move_history = []
    board.show()

    while not board.is_game_over():
        print("\nMove history:", ' '.join(move_history))
        try:
            legal_move_sans = [board.san(m) for m in board.legal_moves]
        except:
            legal_move_sans = []
        print(f"Legal moves: {legal_move_sans}")

        move_input = input(f"{'White' if board.turn else 'Black'} to move ('q' to quit): ").strip()

        if move_input.lower() in ["quit", "exit", "abort", "q"]:
            confirm = input("Are you sure you want to quit the game? (y/n): ").strip().lower()
            if confirm == 'y':
                print("Game aborted.")
                return
            else:
                continue

        try:
            move = board.parse_san(move_input)
            result = board.push_custom(move)

            if result == "normal":
                move_history.append(move_input)
            elif result == "mutual":
                move_history.append(f"{move_input} (✖ mutual destruction)")

            board.show()
        except (ValueError, IndexError, AssertionError, RecursionError) as e:
            print(f"Invalid move: {e}")

    print("Game over!")
    print("Result:", board.result())


# Run the game
if __name__ == "__main__":
    play_game()
