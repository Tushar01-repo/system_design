# Game save and restore system

# Memento
class Memento:
    def __init__(self, level, health, position):
        self._state = {
            "level": level,
            "health": health,
            "position": position
        }

    def get_state(self):
        return self._state
    

# originitor
class GameOriginitor:
    def __init__(self):
        self._level = 0
        self._health = 100
        self._position = (0,0)

    def play(self, level, health, position):
        self._level = level
        self._health = health
        self._position = position

    def get_state(self):
        return f"level : {self._level} | health : {self._health} | position : {self._position}"

    def save(self):
        return Memento(self._level, self._health, self._position)
    
    def restore(self, memento):
        # as get_state returns a dict
        state = memento.get_state()
        self._level = state["level"]
        self._health = state["health"]
        self._position = state["position"]

    
# caretaker
class History:
    def __init__(self):
        self._checkpoints = []

    def save_checkpoint(self, memento):
        self._checkpoints.append(memento)

    def load_checkpoint(self, index):
        if index < 0 or index>=len(self._checkpoints):
            raise IndexError("invalid checkpoint index")
        
        return self._checkpoints[index]
    

# client code 
if __name__ == "__main__":
    # Initialize
    game = GameOriginitor()
    history = History()

    # 🎮 Play Level 1
    game.play(1, 100, (0, 0))
    history.save_checkpoint(game.save())

    # 🎮 Play Level 2
    game.play(2, 80, (10, 5))
    history.save_checkpoint(game.save())

    # 🎮 Play Level 3
    game.play(3, 50, (20, 10))

    print("Current State:")
    print(game.get_state())  
    # Level 3, Health 50, Position (20, 10)

    print("\nRestoring to Checkpoint 0...")
    memento = history.load_checkpoint(0)
    game.restore(memento)

    print(game.get_state())  
    # Level 1, Health 100, Position (0, 0)

    print("\nRestoring to Checkpoint 1...")
    memento = history.load_checkpoint(1)
    game.restore(memento)

    print(game.get_state())  
    # Level 2, Health 80, Position (10, 5)


    

        