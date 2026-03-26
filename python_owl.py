

#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 Ontology design facility
===============================================================================

This program is part of the ProcessModelling suite

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "16.09.2019"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "5.04"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"


import sys
import os

ProMo_path = os.path.join("../../","ProMo")



root = os.path.abspath(ProMo_path)      #os.path.join("../../"{{ProMo}}) #ProcessModeller_v7_04"))

ext = [root, os.path.join(root, 'packages'), \
             os.path.join(root, 'tasks'), \
             os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration')
       ]
# print(os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration'))

# emmo = "/home/heinz/1_Gits/ProcessModeller/ProcessModeller_v7_04/packages/OntologyBuilder/EMMO_Integration/"

sys.path.extend(ext)
from OntologyBuilder.EMMO_Integration.emmo_attach import ProMoOwlOntology
from Common.exchange_board import ProMoExchangeBoard

from owlready2 import *

ontology = ProMoExchangeBoard("processes_distributed_no_interface_eqs") #'flash_03')


variables = ontology.variables

name = "play"
owlfile = name+".owl"

# onto  = O.setup_ontology(name)
o = ProMoOwlOntology()
onto = o.setupOnto()

with onto:
  class ProMoVar(onto.VAR):
    pass

  class has_function(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

  class function(Thing):
    domain  = [ProMoVar]
    range   = [ProMoVar]
    pass

  class is_function_of(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

# V_1
label = variables[V_1]["label"]
network = variables[V_1]["network"]
variable_type = variables[V_1]["type"]
label = variables[V_1]["label"]
doc = variables[V_1]["doc"]
onto_ID = "V_V_1"
V_V_1 = onto.ProMoVar( onto_ID )
V_V_1.label = label
V_V_1.network = network
V_V_1.variable_type = variable_type
V_V_1.comment = doc

units = variables[V_1]["units"].asList()
V_V_1.time = [ units[0] ]
V_V_1.length = [ units[1] ]
V_V_1.amount = [ units[2] ]
V_V_1.mass = [ units[3] ]
V_V_1.temperature = [ units[4] ]
V_V_1.current = [ units[5] ]
V_V_1.light = [ units[6] ]

# V_4
label = variables[V_4]["label"]
network = variables[V_4]["network"]
variable_type = variables[V_4]["type"]
label = variables[V_4]["label"]
doc = variables[V_4]["doc"]
onto_ID = "V_V_4"
V_V_4 = onto.ProMoVar( onto_ID )
V_V_4.label = label
V_V_4.network = network
V_V_4.variable_type = variable_type
V_V_4.comment = doc

units = variables[V_4]["units"].asList()
V_V_4.time = [ units[0] ]
V_V_4.length = [ units[1] ]
V_V_4.amount = [ units[2] ]
V_V_4.mass = [ units[3] ]
V_V_4.temperature = [ units[4] ]
V_V_4.current = [ units[5] ]
V_V_4.light = [ units[6] ]

# V_5
label = variables[V_5]["label"]
network = variables[V_5]["network"]
variable_type = variables[V_5]["type"]
label = variables[V_5]["label"]
doc = variables[V_5]["doc"]
onto_ID = "V_V_5"
V_V_5 = onto.ProMoVar( onto_ID )
V_V_5.label = label
V_V_5.network = network
V_V_5.variable_type = variable_type
V_V_5.comment = doc

units = variables[V_5]["units"].asList()
V_V_5.time = [ units[0] ]
V_V_5.length = [ units[1] ]
V_V_5.amount = [ units[2] ]
V_V_5.mass = [ units[3] ]
V_V_5.temperature = [ units[4] ]
V_V_5.current = [ units[5] ]
V_V_5.light = [ units[6] ]

# functions assignments

#V_1

V_V_1.has_function = []
#V_4

V_V_4.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_1 )
F_ID = "F_E_3"
F_E_3 = onto.function( F_ID )
F_E_3.is_function_of = incidence_list
V_V_4.has_function.append( F_E_3 )
#V_5

V_V_5.has_function = []
incidence_list = []
F_ID = "F_E_4"
F_E_4 = onto.function( F_ID )
F_E_4.is_function_of = incidence_list
V_V_5.has_function.append( F_E_4 )

onto.save("variables.owl")
