# -*- coding: utf-

import operator as op
from functools import partial

class Operation(object):

    def __init__(self, attribute, operation, operand):
        self.attribute = attribute
        self.operation = operation
        self.operand = operand

    def evaluate(self, item):
        return self.attribute, getattr(op, self.operation)(getattr(item, self.attribute), self.operand)


class Condition(object):

    def __init__(self, attribute, operator, operand):
        self.attribute = attribute
        self.operator = operator
        self.operand = operand

    def evaluate(self, item):
        return getattr(op, self.operator)(getattr(item, self.attribute), self.operand)


class Rule(object):

    def __init__(self, item_names, conditions, operations):
        self.item_names = item_names
        self.conditions = conditions
        self.operations = operations

    def check_scope(self, item_name):
        """ We make sure the rule applies to the targeted item. """
        return item_name in self.item_names

    def apply(self, item, callback):
        if self.check_scope(item.name):
            # we make sure all conditions are met
            if all(condition.evaluate(item) for condition in self.conditions):
                # we apply the operations
                for operation in self.operations:
                    attribute, new_value = operation.evaluate(item)
                    # we need this callback because we may not update the Item class
                    callback(item, attribute, new_value)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    min_quality = 0
    max_quality = 50

    def __init__(self, items, rules):
        self.items = items
        self.rules = rules

    def update(self, days=1):
        for day in range(days):
            for item in self.items:
                for rule in self.rules:
                    callback = partial(self.update_attribute, min_quality=self.min_quality, max_quality=self.max_quality)
                    rule.apply(item, callback)

    @staticmethod
    def update_attribute(item, attribute, value, min_quality, max_quality):
        if attribute == "quality":
            if not min_quality <= value <= max_quality:
                return
        setattr(item, attribute, value)
