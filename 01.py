#! /usr/bin/env python

from math import floor


class Module(object):
    def __init__(self, mass):
        self.mass = mass

    def _calculate_fuel(self, mass):
        return floor(mass/3)-2

    @property
    def fuel(self):
        m_part = self._calculate_fuel(self.mass)
        m_total = 0
        while m_part > 0:
            m_total += m_part
            m_part = self._calculate_fuel(m_part)
        return m_total

total_fuel = 0

with open('input', 'r') as input:
    for line in input:
        module = Module(int(line))
        total_fuel += module.fuel

print(total_fuel)
