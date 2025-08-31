# import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_histogram
qc = QuantumCircuit(2,2)

#apply a Hadamard gate to both qubits
qc.h(0)
qc.h(1)

#measure both qubits
qc.measure()

