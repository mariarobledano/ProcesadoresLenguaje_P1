
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftMULTDIVBINARIO COS DIV ENTERO EXP HEXADECIMAL LOG MAS MENOS MULT REAL SINexpresion : MAS expresion expresion\n        | MENOS expresion expresion\n        | MULT expresion expresion\n        | DIV expresion expresionexpresion : EXP expresion\n        | LOG expresion\n        | SIN expresion\n        | COS expresionexpresion : ENTERO\n        | REALexpresion : BINARIOexpresion : HEXADECIMAL'
    
_lr_action_items = {'MAS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[2,2,2,2,2,2,2,2,2,-9,-10,-11,-12,2,2,2,2,-5,-6,-7,-8,-1,-2,-3,-4,]),'MENOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[3,3,3,3,3,3,3,3,3,-9,-10,-11,-12,3,3,3,3,-5,-6,-7,-8,-1,-2,-3,-4,]),'MULT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[4,4,4,4,4,4,4,4,4,-9,-10,-11,-12,4,4,4,4,-5,-6,-7,-8,-1,-2,-3,-4,]),'DIV':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[5,5,5,5,5,5,5,5,5,-9,-10,-11,-12,5,5,5,5,-5,-6,-7,-8,-1,-2,-3,-4,]),'EXP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[6,6,6,6,6,6,6,6,6,-9,-10,-11,-12,6,6,6,6,-5,-6,-7,-8,-1,-2,-3,-4,]),'LOG':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[7,7,7,7,7,7,7,7,7,-9,-10,-11,-12,7,7,7,7,-5,-6,-7,-8,-1,-2,-3,-4,]),'SIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[8,8,8,8,8,8,8,8,8,-9,-10,-11,-12,8,8,8,8,-5,-6,-7,-8,-1,-2,-3,-4,]),'COS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[9,9,9,9,9,9,9,9,9,-9,-10,-11,-12,9,9,9,9,-5,-6,-7,-8,-1,-2,-3,-4,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[10,10,10,10,10,10,10,10,10,-9,-10,-11,-12,10,10,10,10,-5,-6,-7,-8,-1,-2,-3,-4,]),'REAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[11,11,11,11,11,11,11,11,11,-9,-10,-11,-12,11,11,11,11,-5,-6,-7,-8,-1,-2,-3,-4,]),'BINARIO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[12,12,12,12,12,12,12,12,12,-9,-10,-11,-12,12,12,12,12,-5,-6,-7,-8,-1,-2,-3,-4,]),'HEXADECIMAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[13,13,13,13,13,13,13,13,13,-9,-10,-11,-12,13,13,13,13,-5,-6,-7,-8,-1,-2,-3,-4,]),'$end':([1,10,11,12,13,18,19,20,21,22,23,24,25,],[0,-9,-10,-11,-12,-5,-6,-7,-8,-1,-2,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,2,3,4,5,6,7,8,9,14,15,16,17,],[1,14,15,16,17,18,19,20,21,22,23,24,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expresion","S'",1,None,None,None),
  ('expresion -> MAS expresion expresion','expresion',3,'p_expresion_operacion','parser.py',12),
  ('expresion -> MENOS expresion expresion','expresion',3,'p_expresion_operacion','parser.py',13),
  ('expresion -> MULT expresion expresion','expresion',3,'p_expresion_operacion','parser.py',14),
  ('expresion -> DIV expresion expresion','expresion',3,'p_expresion_operacion','parser.py',15),
  ('expresion -> EXP expresion','expresion',2,'p_expresion_funcion','parser.py',26),
  ('expresion -> LOG expresion','expresion',2,'p_expresion_funcion','parser.py',27),
  ('expresion -> SIN expresion','expresion',2,'p_expresion_funcion','parser.py',28),
  ('expresion -> COS expresion','expresion',2,'p_expresion_funcion','parser.py',29),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','parser.py',41),
  ('expresion -> REAL','expresion',1,'p_expresion_numero','parser.py',42),
  ('expresion -> BINARIO','expresion',1,'p_expresion_binario','parser.py',46),
  ('expresion -> HEXADECIMAL','expresion',1,'p_expresion_hexadecimal','parser.py',50),
]
