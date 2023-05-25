from . import transform

from lark import Lark

lino = Lark.open('lino/parser/lino.lark', parser='lalr', start='start', transformer=transform.Tokens())