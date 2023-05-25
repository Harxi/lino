from typing import Any

class Node:
    def __init__(self, value: Any):
        self.value = value
    
    def __float__(self):
        return float(self.value)
    
    def __int__(self):
        return int(self.value)
    
    def __str__(self):
        return str(self.value)
  
class String(Node):
    def __init__(self, value: str):
        super().__init__(value)
        
    def __repr__(self):
        return f"<LinoCore[STR]:{self.value}>"

class Integer(Node):
    def __init__(self, value: int):
        super().__init__(value)

    def __repr__(self):
        return f"<LinoCore[INT]:{self.value}>"

class Float(Node):
    def __init__(self, value: float):
        super().__init__(value)
    
    def __repr__(self):
        return f"<LinoCore[FLT]:{self.value}>"

class Name(Node):
    def __init__(self, value: int):
        super().__init__(value)
    
    def __repr__(self):
        return f"<LinoCore[NM]:{self.value}>"

class Point(Node):
    def __init__(self, name: str, value: list[Node]):
        super().__init__(value)
        self.name = name
    
    def __repr__(self):
        return f"<LinoCore[PNT]:{self.name} {{ {', '.join([str(x) for x in self.value])} }}>"

class Instruction(Node):
    def __init__(self, name: str, value: list[Node]):
        super().__init__(value)
        self.name = name
    
    def __repr__(self):
        return f"<LinoCore[INS]:{self.name} {', '.join([str(x) for x in self.value])}>"