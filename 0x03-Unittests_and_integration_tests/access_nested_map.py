#!/usr/bin/env python3
"""
Module: access_nested_map.py

This module accesses a neste map
"""


def access_nested_map(nested_map, path):
    """
    This module accesses a nested map using a given path
    """
    current = nested_map
    for key in path:
        current = current[key]
    return current
