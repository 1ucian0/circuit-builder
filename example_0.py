import numpy as np

from circuitbuilder.types import Qubit
from circuitbuilder import circuit


@circuit
def H(qubit: Qubit):
    circuit.Ry(np.pi/2) | qubit
    circuit.Rz(np.pi) | qubit


@circuit
def bell_state() -> qi.Array[bool]:
    qubits = circuit.qreg(2)
    H() | qubits[0]
    circuit.CX() | qubits[0:1]
    regs = circuit.measure(qubits, regs=[0, 1, 2, 3])
    return regs


print(bell_state)
