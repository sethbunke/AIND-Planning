import os
import sys
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(parent), "aimacode"))
from aimacode.planning import Action
from aimacode.utils import expr
from aimacode.search import Node

import unittest

from my_air_cargo_problems import (
    air_cargo_p1, air_cargo_p2, air_cargo_p3,
)

from example_have_cake import have_cake

from my_planning_graph import (
    PlanningGraph, PgNode_a, PgNode_s, mutexify
)


class TestAirCargoProb1():
    
    def setUp(self):
        self.p1 = air_cargo_p1()
        self.act1 = Action(
            expr('Load(C1, P1, SFO)'),
            [[expr('At(C1, SFO)'), expr('At(P1, SFO)')], []],
            [[expr('In(C1, P1)')], [expr('At(C1, SFO)')]])
        
        print('test')

        n = Node(self.p1.initial)
        count = self.p1.h_ignore_preconditions(n)


    def setUp1(self):
        self.p1 = air_cargo_p1()
        self.act1 = Action(
            expr('Load(C1, P1, SFO)'),
            [[expr('At(C1, SFO)'), expr('At(P1, SFO)')], []],
            [[expr('In(C1, P1)')], [expr('At(C1, SFO)')]]
        )

        for action in self.p1.actions_list:
            print("{}{}".format(action.name, action.args))
        
        length = len(self.p1.actions_list)
        #self.assertEqual(len(self.p1.actions_list), 20)

    def setUp2(self):
        self.p1 = air_cargo_p1()
        self.act1 = Action(
            expr('Load(C1, P1, SFO)'),
            [[expr('At(C1, SFO)'), expr('At(P1, SFO)')], []],
            [[expr('In(C1, P1)')], [expr('At(C1, SFO)')]]
        )

        n = Node(self.p1.initial)
        count = self.p1.h_ignore_preconditions(n)
        #self.assertEqual(self.p1.h_ignore_preconditions(n),2)



class TestPlanningGraphLevels1():
    def setUp(self):
        self.p = have_cake()
        self.pg = PlanningGraph(self.p, self.p.initial)

        self.na1 = PgNode_a(Action(expr('Go(here)'),
                                   [[], []], [[expr('At(here)')], []]))
        self.na2 = PgNode_a(Action(expr('Go(there)'),
                                   [[], []], [[expr('At(there)')], []]))
        self.na3 = PgNode_a(Action(expr('Noop(At(there))'),
                                   [[expr('At(there)')], []], [[expr('At(there)')], []]))
        self.na4 = PgNode_a(Action(expr('Noop(At(here))'),
                                   [[expr('At(here)')], []], [[expr('At(here)')], []]))
        self.na5 = PgNode_a(Action(expr('Reverse(At(here))'),
                                   [[expr('At(here)')], []], [[], [expr('At(here)')]]))

    def test_add_action_level(self):
        # for level, nodeset in enumerate(self.pg.a_levels):
        #     for node in nodeset:
        #         print("Level {}: {}{})".format(level, node.action.name, node.action.args))

        len_a_levels_0 = len(self.pg.a_levels[0])

        len_a_levels_1 = len(self.pg.a_levels[1])

        # self.assertEqual(len(self.pg.a_levels[0]), 3, len(self.pg.a_levels[0]))
        # self.assertEqual(len(self.pg.a_levels[1]), 6, len(self.pg.a_levels[1]))
        pass

    def test_add_literal_level(self):
        # for level, nodeset in enumerate(self.pg.s_levels):
        #     for node in nodeset:
        #         print("Level {}: {})".format(level, node.literal))
        # self.assertEqual(len(self.pg.s_levels[0]), 2, len(self.pg.s_levels[0]))
        # self.assertEqual(len(self.pg.s_levels[1]), 4, len(self.pg.s_levels[1]))
        # self.assertEqual(len(self.pg.s_levels[2]), 4, len(self.pg.s_levels[2]))
        pass


    def test_inconsistent_effects_mutex(self):
        
        result_1 = PlanningGraph.inconsistent_effects_mutex(self.pg, self.na4, self.na5)


        result_2 = PlanningGraph.inconsistent_effects_mutex(self.pg, self.na1, self.na2)
        # self.assertTrue(PlanningGraph.inconsistent_effects_mutex(self.pg, self.na4, self.na5),
        #                 "Canceling effects not marked as mutex")
        # self.assertFalse(PlanningGraph.inconsistent_effects_mutex(self.pg, self.na1, self.na2),
        #                  "Non-Canceling effects incorrectly marked as mutex")
        
    
# t = TestAirCargoProb1()
# t.setUp2

class TestPlanningGraphLevels2():
    def setUp(self):
        pass

    def test1(self):
        result_1 = PlanningGraph.inconsistent_effects_mutex(None, None, None)

    def test2(self):
        result_1 = PlanningGraph.interference_mutex(None, None, None)

# t = TestPlanningGraphLevels1()
# t.setUp()
# t.test_inconsistent_effects_mutex()

t = TestPlanningGraphLevels2()
t.test2();