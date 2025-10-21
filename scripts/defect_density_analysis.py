"""
Calculate approximate stacking fault densities from XRD peak broadening or TEM image analysis.
"""
import numpy as np

def sf_density(fault_spacing_nm):
    """Return stacking-fault density per nm."""
    return 1 / fault_spacing_nm

if __name__ == "__main__":
    print("Example: 1 fault every 6 layers (~1.2 nm)")
    print("Density =", sf_density(1.2), "faults/nm")
