import numpy as np
import matplotlib.pyplot as plt
import qiskit
import qiskit.tools.jupyter

def hilbertSpace():
    # create a Hilbert space with 2 qubits
    q = QuantumRegister(2)
    c = ClassicalRegister(2)
    qc = QuantumCircuit(q, c)
    # apply Hadamard to the first qubit
    qc.h(q[0])
    # apply CNOT with the first qubit as control and the second as target
    qc.cx(q[0], q[1])
    # measure the two qubits
    qc.measure(q, c)
    # draw the circuit
    qc.draw(output='mpl')
    # execute the circuit
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result()
    # plot the histogram
    plot_histogram(result.get_counts(qc))
def main():
    hilbertSpace()
main()