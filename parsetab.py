
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftMULTDIVBINARIO COS DIV ENTERO EXP HEXADECIMAL IGUAL INF LOG MAS MEMORY MENOS MULT NAN REAL SINexpresion : MAS expresion expresion\n        | MENOS expresion expresion\n        | MULT expresion expresion\n        | DIV expresion expresionexpresion : EXP expresion\n        | LOG expresion\n        | SIN expresion\n        | COS expresionexpresion : ENTERO\n        | REALexpresion : BINARIOexpresion : HEXADECIMALexpresion : INF\n                 | NANexpresion : MEMORY IGUAL expresionexpresion : MEMORY'
    
_lr_action_items = {'MAS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[2,2,2,2,2,2,2,2,2,-9,-10,-11,-12,-13,-14,-16,2,2,2,2,-5,-6,-7,-8,2,-1,-2,-3,-4,-15,]),'MENOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[3,3,3,3,3,3,3,3,3,-9,-10,-11,-12,-13,-14,-16,3,3,3,3,-5,-6,-7,-8,3,-1,-2,-3,-4,-15,]),'MULT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[4,4,4,4,4,4,4,4,4,-9,-10,-11,-12,-13,-14,-16,4,4,4,4,-5,-6,-7,-8,4,-1,-2,-3,-4,-15,]),'DIV':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[5,5,5,5,5,5,5,5,5,-9,-10,-11,-12,-13,-14,-16,5,5,5,5,-5,-6,-7,-8,5,-1,-2,-3,-4,-15,]),'EXP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[6,6,6,6,6,6,6,6,6,-9,-10,-11,-12,-13,-14,-16,6,6,6,6,-5,-6,-7,-8,6,-1,-2,-3,-4,-15,]),'LOG':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[7,7,7,7,7,7,7,7,7,-9,-10,-11,-12,-13,-14,-16,7,7,7,7,-5,-6,-7,-8,7,-1,-2,-3,-4,-15,]),'SIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[8,8,8,8,8,8,8,8,8,-9,-10,-11,-12,-13,-14,-16,8,8,8,8,-5,-6,-7,-8,8,-1,-2,-3,-4,-15,]),'COS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[9,9,9,9,9,9,9,9,9,-9,-10,-11,-12,-13,-14,-16,9,9,9,9,-5,-6,-7,-8,9,-1,-2,-3,-4,-15,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[10,10,10,10,10,10,10,10,10,-9,-10,-11,-12,-13,-14,-16,10,10,10,10,-5,-6,-7,-8,10,-1,-2,-3,-4,-15,]),'REAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[11,11,11,11,11,11,11,11,11,-9,-10,-11,-12,-13,-14,-16,11,11,11,11,-5,-6,-7,-8,11,-1,-2,-3,-4,-15,]),'BINARIO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[12,12,12,12,12,12,12,12,12,-9,-10,-11,-12,-13,-14,-16,12,12,12,12,-5,-6,-7,-8,12,-1,-2,-3,-4,-15,]),'HEXADECIMAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[13,13,13,13,13,13,13,13,13,-9,-10,-11,-12,-13,-14,-16,13,13,13,13,-5,-6,-7,-8,13,-1,-2,-3,-4,-15,]),'INF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[14,14,14,14,14,14,14,14,14,-9,-10,-11,-12,-13,-14,-16,14,14,14,14,-5,-6,-7,-8,14,-1,-2,-3,-4,-15,]),'NAN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[15,15,15,15,15,15,15,15,15,-9,-10,-11,-12,-13,-14,-16,15,15,15,15,-5,-6,-7,-8,15,-1,-2,-3,-4,-15,]),'MEMORY':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,],[16,16,16,16,16,16,16,16,16,-9,-10,-11,-12,-13,-14,-16,16,16,16,16,-5,-6,-7,-8,16,-1,-2,-3,-4,-15,]),'$end':([1,10,11,12,13,14,15,16,21,22,23,24,26,27,28,29,30,],[0,-9,-10,-11,-12,-13,-14,-16,-5,-6,-7,-8,-1,-2,-3,-4,-15,]),'IGUAL':([16,],[25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,2,3,4,5,6,7,8,9,17,18,19,20,25,],[1,17,18,19,20,21,22,23,24,26,27,28,29,30,]),}

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
  ('expresion -> INF','expresion',1,'p_expresion_inf_nan','parser.py',60),
  ('expresion -> NAN','expresion',1,'p_expresion_inf_nan','parser.py',61),
  ('expresion -> MEMORY IGUAL expresion','expresion',3,'p_asignacion_memory','parser.py',67),
  ('expresion -> MEMORY','expresion',1,'p_expresion_memory','parser.py',73),
]
