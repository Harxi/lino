from typing import Any

from .parser import ltypes as ltypes

class Core:
    points = {}
    stack = []
    
    def __init__(self, code: list[ltypes.Node], **kwargs: dict[str, int]):
        self.code = code
        self.token = ltypes.Node(None)
        self.registers = kwargs | {"sp": ltypes.Integer(0)}
    
    def _token_pop(self) -> None:
        tmp = self.token.value[0]
        if not self.exist(str(tmp))[0]:
            raise NameError # TO DO / ADD ERROR
            
        if isinstance(tmp, ltypes.Name):
            if self.stack != []:
                self.registers["sp"].value -= 1
                self.registers[str(tmp)] = self.stack.pop()
            else: 
                self.registers[str(tmp)] = 0
            return
        raise TypeError # TO DO / ADD ERROR
    
    def _token_push(self) -> None:
        tmp = self.token.value[0]
        self.registers["sp"].value += 1
        self.stack += [tmp]
    
    
    def exist(self, n: str) -> tuple:
        return True if n in self.registers else False, True if n in self.points else False
        
    def get(self, n: str, flag: int) -> Any:
        if isinstance(n, ltypes.Name):
            if flag == 0:
               return self.registers[n.name]
               
            if flag == 1:
               return self.points[n.name]
               
        if isinstance(d, ltypes.Float) or isinstance(d, ltypes.Integer) or isinstance(d, ltypes.String):
            return d.value      
    
    def execute(self) -> None:
        for token in self.code:
            self.token = token
            if isinstance(token, ltypes.Instruction):
                self.__getattribute__(f"_token_{token.name}")()
        print(self.stack, self.registers)