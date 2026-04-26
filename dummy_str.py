# dummy class for string
# with a write method

class DummyStr:
    def __init__(self) -> None:
        self.str = "";
    
    def write(self, data: str):
        self.str += data;

    def clear(self):
        self.str = "";