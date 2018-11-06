#!/usr/bin/env python
# -*- coding: utf-8 -*

from gilded_rose_refactoring_kata import gilded_rose

DEXTERITY_VEST = "+5 Dexterity Vest"
AGED_BRIE = "Aged Brie"
ELIXIR_OF_THE_MONGOOSE = "Elixir of the Mongoose"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_TAFKAL80ETC = "Backstage passes to a TAFKAL80ETC concert"
CONJURED_MANA_CAKE = "Conjured Mana Cake"

FIXTURES = {
    0: [
        gilded_rose.Item(name=DEXTERITY_VEST, sell_in=10, quality=20),
        gilded_rose.Item(name=AGED_BRIE, sell_in=2, quality=0),
        gilded_rose.Item(name=ELIXIR_OF_THE_MONGOOSE, sell_in=5, quality=7),
        gilded_rose.Item(name=SULFURAS, sell_in=0, quality=80),
        gilded_rose.Item(name=SULFURAS, sell_in=-1, quality=80),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=15, quality=20),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=10, quality=49),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=5, quality=49),
        gilded_rose.Item(name=CONJURED_MANA_CAKE, sell_in=3, quality=6),  # <-- :O
    ],
    1: [
        gilded_rose.Item(name=DEXTERITY_VEST, sell_in=10 - 1, quality=20 -1),
        gilded_rose.Item(name=AGED_BRIE, sell_in=2 - 1, quality=0 + 1),
        gilded_rose.Item(name=ELIXIR_OF_THE_MONGOOSE, sell_in=5 - 1, quality=7 - 1),
        gilded_rose.Item(name=SULFURAS, sell_in=0, quality=80),
        gilded_rose.Item(name=SULFURAS, sell_in=-1, quality=80),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=15 - 1, quality=20 + 1),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=10 - 1, quality=49 + 1),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=5 - 1, quality=49 + 1),
        gilded_rose.Item(name=CONJURED_MANA_CAKE, sell_in=3 - 1, quality= 6 - 1 * 2),
    ],
    # tests the aceelerated decrease of the quality attribute
    # "Once the sell by date has passed, Quality degrades twice as fast"
    11: [
        # double decrease in quality
        gilded_rose.Item(name=DEXTERITY_VEST, sell_in=10 - 11, quality=20 - 11 - 1 * 2),
        # AGED_BRIE actually increases in Quality the older it gets
        # TODO: Aged Brie should be 0 + 11, but was 20 in the legacy program
        gilded_rose.Item(name=AGED_BRIE, sell_in=2 - 11, quality=11),
        # The Quality of an item is never more than 50
        gilded_rose.Item(name=ELIXIR_OF_THE_MONGOOSE, sell_in=5 - 11, quality=0),
        # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
        gilded_rose.Item(name=SULFURAS, sell_in=0, quality=80),
        gilded_rose.Item(name=SULFURAS, sell_in=-1, quality=80),
        # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        # TODO: legacy program returned 38 for the first instance of BACKSTAGE_TAFKAL80ETC
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=15 - 11, quality=20 + 4 * 1 + 5 * 2 + 2 * 3),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=10 - 11, quality=0),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=5 - 11, quality=0),
        # no special rule
        gilded_rose.Item(name=CONJURED_MANA_CAKE, sell_in=3 - 11, quality=0),
    ],
    # this tests the limits of the quality property (0 < quality < 50)
    51: [
        # no special rule
        gilded_rose.Item(name=DEXTERITY_VEST, sell_in=10 - 51, quality=0),
        # AGED_BRIE actually increases in Quality the older it gets
        # The Quality of an item is never more than 50
        gilded_rose.Item(name=AGED_BRIE, sell_in=2 - 51, quality=50),
        # no special rule
        gilded_rose.Item(name=ELIXIR_OF_THE_MONGOOSE, sell_in=5 - 51, quality=0),
        # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
        gilded_rose.Item(name=SULFURAS, sell_in=0, quality=80),
        gilded_rose.Item(name=SULFURAS, sell_in=-1, quality=80),
        # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=15 - 51, quality=0),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=10 - 51, quality=0),
        gilded_rose.Item(name=BACKSTAGE_TAFKAL80ETC, sell_in=5 - 51, quality=0),
        # no special rule
        gilded_rose.Item(name=CONJURED_MANA_CAKE, sell_in=3 - 51, quality=0),
    ],
}

ADD = "add"
SUB = "sub"
LE = "le"
GT = "gt"
EQ = "eq"

RULES = [
    # the default rule:
    # "At the end of each day our system lowers both values for every item"
    gilded_rose.Rule(
        item_names=[
            DEXTERITY_VEST,
            ELIXIR_OF_THE_MONGOOSE,
        ],
        conditions=[],
        operations=[
            gilded_rose.Operation(attribute="sell_in", operation=SUB, operand=1),
            gilded_rose.Operation(attribute="quality", operation=SUB, operand=1),
        ]
    ),
    # "Conjured" items degrade in Quality twice as fast as normal items
    gilded_rose.Rule(
        item_names=[
            CONJURED_MANA_CAKE
        ],
        conditions=[],
        operations=[
            gilded_rose.Operation(attribute="sell_in", operation=SUB, operand=1),
            gilded_rose.Operation(attribute="quality", operation=SUB, operand=2),
        ]
    ),
    # "Aged Brie" actually increases in Quality the older it gets
    gilded_rose.Rule(
        item_names=[
            AGED_BRIE
        ],
        conditions=[],
        operations=[
            gilded_rose.Operation(attribute="sell_in", operation=SUB, operand=1),
            gilded_rose.Operation(attribute="quality", operation=ADD, operand=1),
        ]
    ),
    # Once the sell by date has passed, Quality degrades twice as fast
    gilded_rose.Rule(
        item_names=[
            DEXTERITY_VEST,
            ELIXIR_OF_THE_MONGOOSE,
            CONJURED_MANA_CAKE
        ],
        conditions=[
            gilded_rose.Condition(attribute="sell_in", operator=LE, operand=0),
        ],
        operations=[
            gilded_rose.Operation(attribute="quality", operation=SUB, operand=1),
        ]
    ),
    gilded_rose.Rule(
        item_names=[
            CONJURED_MANA_CAKE
        ],
        conditions=[
            gilded_rose.Condition(attribute="sell_in", operator=LE, operand=0),
        ],
        operations=[
            gilded_rose.Operation(attribute="quality", operation=SUB, operand=1),
        ]
    ),
    # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    gilded_rose.Rule(
        item_names=[
            BACKSTAGE_TAFKAL80ETC
        ],
        conditions=[
            gilded_rose.Condition(attribute="sell_in", operator=GT, operand=0),
        ],
        operations=[
            gilded_rose.Operation(attribute="quality", operation=ADD, operand=1),
        ]
    ),
    gilded_rose.Rule(
        item_names=[
            BACKSTAGE_TAFKAL80ETC
        ],
        conditions=[],
        operations=[
            gilded_rose.Operation(attribute="sell_in", operation=SUB, operand=1),
        ]
    ),
    # Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    gilded_rose.Rule(
        item_names=[
            BACKSTAGE_TAFKAL80ETC
        ],
        conditions=[
            gilded_rose.Condition(attribute="sell_in", operator=LE, operand=10),
        ],
        operations=[
            gilded_rose.Operation(attribute="quality", operation=ADD, operand=1),
        ]
    ),
    gilded_rose.Rule(
        item_names=[
            BACKSTAGE_TAFKAL80ETC
        ],
        conditions=[
            gilded_rose.Condition(attribute="sell_in", operator=LE, operand=5),
        ],
        operations=[
            gilded_rose.Operation(attribute="quality", operation=ADD, operand=1),
        ]
    ),
    # Quality drops to 0 after the concert
    gilded_rose.Rule(
        item_names=[
            BACKSTAGE_TAFKAL80ETC
        ],
        conditions=[
            gilded_rose.Condition(attribute="sell_in", operator=LE, operand=0),
        ],
        operations=[
            gilded_rose.Operation(attribute="quality", operation=EQ, operand=0),
        ]
    ),
]
