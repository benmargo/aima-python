import collections, sys, os
from logic import *
from planning import *

############################################################
# Problem: Planning


# Blocks world modification
def blocksWorldModPlan():
    # BEGIN_YOUR_CODE (make modifications to the initial and goal states)
    initial_state = (
        "On(A, B) & Clear(A) & OnTable(B) & OnTable(D) & Clear(C) & On(C, D)"
    )
    goal_state = "On(B, A) & On(C, B) & On(D, C)"
    # END_YOUR_CODE

    planning_problem = PlanningProblem(
        initial=initial_state,
        goals=goal_state,
        actions=[
            Action(
                "ToTable(x, y)",
                precond="On(x, y) & Clear(x)",
                effect="~On(x, y) & Clear(y) & OnTable(x)",
            ),
            Action(
                "FromTable(y, x)",
                precond="OnTable(y) & Clear(y) & Clear(x)",
                effect="~OnTable(y) & ~Clear(x) & On(y, x)",
            ),
        ],
    )

    return linearize(GraphPlan(planning_problem).execute())


def logisticsPlan():
    # BEGIN_YOUR_CODE (use the previous problem as a guide and uncomment the starter code below if you want!)
    # can get rid of clear state and just use the On state
    universal_conditions = (
        "Block(C1) & Block(C2) & Block(C3) & Dest(D1) & Dest(D2) & Dest(D3)"
    )
    initial_states = [
        'In(Car, D1) & On(C1, Car) & ~Clear(Car) & In(C2, D1) & In(C3, D2)',
        'In(Car, D1) & On(C1, Car) & ~Clear(Car) & In(C2, D1) & In(C3, D2)',
        'In(Car, D1) & On(C1, Car) & ~Clear(Car) & In(C2, D1) & In(C3, D2)',
        'In(Car, D1) & On(C1, Car) & ~Clear(Car) & In(C2, D1) & In(C3, D2)'
    ]
    initial_states = [state + " & " + universal_conditions for state in initial_states]
    goal_states = [
        'In(C1, D3) & In(C2, D3) & In(C3, D3)',
        'In(C1, D2)',
        'In(C1, D1) & In(Car, D2)',
        'In(C1, D1) & In(Car, D2) & On(C3, Car)'
    ]
    test_case = 3
    planning_problem = PlanningProblem(
        initial=initial_states[test_case],
        goals=goal_states[test_case],
        actions=[
            Action(
                "Move(a, b)",
                precond="In(Car, a) & Dest(b)",  # need to do Dest(b) cuz then b can take on a value here
                effect="In(Car, b) & ~In(Car, a)",
            ),
            Action(
                "Unload(b, r)",
                precond="On(b, Car) & ~Clear(Car) & In(Car, r) & Block(b)",
                effect="~On(b, Car) & Clear(Car) & In(b, r)",
            ),
            Action(
                "Load(b, r)",
                precond="In(Car, r) & In(b, r) & Clear(Car) & Block(b)",  # note how ~On(b, Car) isn't in initial conditions, varaible needs to be assigned in precond
                effect="On(b, Car) & ~Clear(Car) & ~In(b, r)",
            ),
        ],
    )
    # END_YOUR_CODE

    return linearize(GraphPlan(planning_problem).execute())


# a = blocksWorldModPlan()
# print(a)

b = logisticsPlan()
print(b)

# pp = PlanningProblem(initial='Block(C1) & Block(C2) & In(Car, D1) & In(C1, D1) & In(C2, D1) & Clear(Car) & In(C1, D1) & Dest(D1) & Dest(D2) & Dest(D3)',
#                     goals='In(C1, D2) & In(C2, D2) & In(Car, D1)',
#                     actions=[Action('Move(a, b)',
#                                     precond='In(Car, a) & Dest(b)', # need to do Dest(b) cuz then b can take on a value here
#                                     effect='In(Car, b) & ~In(Car, a)'),
#                             Action('Unload(b, r)',
#                                    precond='On(b, Car) & ~Clear(Car) & In(Car, r) & Block(b)',
#                                    effect='~On(b, Car) & Clear(Car) & In(b, r)'),
#                             Action('Load(b, r)',
#                                    precond='In(Car, r) & In(b, r) & Clear(Car) & Block(b)', # note how ~On(b, Car) isn't in initial conditions, varaible needs to be assigned in precond
#                                    effect='On(b, Car) & ~Clear(Car) & ~In(b, r)')])
# ans = linearize(GraphPlan(pp).execute())
# print(ans)

# initial='In(Car, D1) & On(C1, Car) & Dest(D1) & Dest(D2) & Dest(D3) & In(C2, D1)',
#                     goals='In(Car, D2) & In(C1, D2) & In(C2, D2)',

"""
test that the car can move back and forward between rooms
test that the car can just load something and experiment with required preconditions
"""
