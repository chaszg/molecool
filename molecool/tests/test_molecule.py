"""
Test for the molecule module
"""
import pytest

import molecool

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H']
    
    calculated_mass = molecool.molecule.calculate_molecular_mass(symbols)

    actual_mass = molecool.atom_data.atomic_weights['C'] + molecool.atom_data.atomic_weights['H'] +\
         molecool.atom_data.atomic_weights['H'] + molecool.atom_data.atomic_weights['H']
    
    assert actual_mass == calculated_mass