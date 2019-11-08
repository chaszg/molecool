import pytest

import molecool

def test_molecular_mass(test_molecule):
    symbols = ['C', 'H', 'H', 'H', 'H']
    
    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = molecool.atom_data.atom_weights['C'] + molecool.atom_data.atom_weights['H'] +\
         molecool.atom_data.atom_weights['H'] + molecool.atom_data.atom_weights['H']
    
    assert actual_mass == calculated_mass