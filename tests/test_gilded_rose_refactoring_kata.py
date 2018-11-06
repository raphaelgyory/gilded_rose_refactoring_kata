#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `gilded_rose_refactoring_kata` package."""

import pytest

from click.testing import CliRunner

from gilded_rose_refactoring_kata import gilded_rose
from gilded_rose_refactoring_kata import cli
from tests import fixtures


def compare_results_attrs(items1, items2):
    assert len(items1) == len(items2)
    for i in range(len(items1)):
        assert items1[i].name == items2[i].name
        assert items1[i].sell_in == items2[i].sell_in
        assert items1[i].quality == items2[i].quality


@pytest.fixture
def manager():
    """ Loads gilded roses with fixtures. """
    return gilded_rose.GildedRose(fixtures.FIXTURES[0], fixtures.RULES)


def test_legacy_items_at_day_0(manager):
    """ Make sure legacy data keeps working. """
    compare_results_attrs(manager.items, fixtures.FIXTURES[0])


def test_legacy_items_at_day_1(manager):
    """ Make sure legacy data keeps working. """
    manager.update()
    compare_results_attrs(manager.items, fixtures.FIXTURES[1])


def test_day_11(manager):
    manager.update(days=10)
    compare_results_attrs(manager.items, fixtures.FIXTURES[11])


def test_limits(manager):
    """ Makes sure 0 < quality < 50  """
    manager.update(days=40)
    compare_results_attrs(manager.items, fixtures.FIXTURES[51])


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'gilded_rose_refactoring_kata.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
