"""airit_simulation.py
author: Chase Lewis
created: November 2017"""

import rit_lib

Passenger = struct_type("Passenger", (str, "name"), (str,"ticket"), (bool, "bag"))

Gate = struct_type("Gate", (list, "lines"), (int, "num_passenger"), (int, "max_size"))

Aircraft = struct_type("Aircraft" , (Stack, "no_bag"), (int, "num_passengers"), (int, "max_size"), (Stack, "carry_ons")
                       


def read_passenger(file):
    line = readline(file).strip().split(",")
    if line == "":
        return None
    else:
        one_passenger = Passenger(line[1] + " " + line[2], line[2],line[3], "True" == line[0])
        return one_passenger
def line_up(gate, file):
    for passenger in file:
        one_passenger = read_passenger(file)
        for gate in one_passenger:
            line = int(one_passenger.ticket[0])
            enqueue(gate.lines[line - 1], one_passenger)
            gate.num_passenger += 1
            gate.lines[line - 1].size += 1
            if gate.num_passengers > gate.max_size:
                return False
            else:
                return True
                                   
                

                        

