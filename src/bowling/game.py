from bowling.frame import Frame


class BowlingGame:
    frames = []

    def add_frame(self, frame: Frame):
        self.frames.append(Frame)

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        # To be implemented
        pass

    def score(self) -> int:
        """ Get the score from the game """
        score = 0
        for frame in self.frames:
            score += frame.score()
        return score

    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        # To be implemented
        pass
