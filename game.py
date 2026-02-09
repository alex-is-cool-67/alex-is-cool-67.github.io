import os
import random

def clear_screen():
    # This clears the window so it looks like a game
    os.system('clear')

class Game:
    def __init__(self):
        self.x = 2
        self.y = 2
        self.essence = 0
        self.form = "Human"
        self.goal_x = 5
        self.goal_y = 5
        self.playing = True

    def draw(self):
        clear_screen()
        print("=== SHAPESHIFTER ADVENTURE ===")
        print(f"FORM: {self.form} | ESSENCE: {self.essence}")
        print("Controls: w (up), s (down), a (left), d (right), q (quit)")
        print("-" * 30)

        for y in range(10):
            row = ""
            for x in range(10):
                if x == self.x and y == self.y:
                    row += " P "  # Player
                elif x == self.goal_x and y == self.goal_y:
                    row += " * "  # Power-up
                elif x == 0 or x == 9 or y == 0 or y == 9:
                    row += " # "  # Wall
                else:
                    row += " . "
            print(row)

    def play(self):
        while self.playing:
            self.draw()
            move = input("\nMove (w/a/s/d): ").lower()

            if move == 'w': self.y -= 1
            if move == 's': self.y += 1
            if move == 'a': self.x -= 1
            if move == 'd': self.x += 1
            if move == 'q': self.playing = False

            # Don't walk through walls
            self.x = max(1, min(self.x, 8))
            self.y = max(1, min(self.y, 8))

            # Pick up power-up
            if self.x == self.goal_x and self.y == self.goal_y:
                self.essence += 1
                self.goal_x = random.randint(1, 8)
                self.goal_y = random.randint(1, 8)
                
                # SHAPESHIFT LOGIC
                if self.essence == 3:
                    self.form = "Werewolf"
                elif self.essence == 7:
                    self.form = "Dragon"

if __name__ == "__main__":
    game = Game()
    game.play()