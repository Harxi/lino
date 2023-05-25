from . import ltypes

from lark import Transformer

class Tokens(Transformer):
    def STRING(self, s) -> ltypes.Node:
        return ltypes.String(str(s)[1:-1])
        
    def INT(self, i) -> ltypes.Node:
        return ltypes.Integer(int(i))
    
    def FLOAT(self, f) -> ltypes.Node:
        return ltypes.Float(f)
    
    def HEX(self, h) -> ltypes.Node:
        return ltypes.Integer(int(str(h), 16))
    
    def CNAME(self, n) -> ltypes.Node:
        return ltypes.Name(n)
        
    def instruction(self, i) -> ltypes.Node:
        return ltypes.Instruction(i[0], i[1:])
    
    def point(self, p) -> ltypes.Node:
        return ltypes.Point(p[0], p[1:])