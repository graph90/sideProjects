import numpy as np
import matplotlib.pyplot as plt
import qiskit
import qiskit.tools.jupyter

def hilbertSpace():
    q = QuantumRegister(2)
    c = ClassicalRegister(2)
    qc = QuantumCircuit(q, c)
    qc.h(q[0])
    qc.cx(q[0], q[1])
    qc.measure(q, c)
    qc.draw(output='mpl')
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result()
    plot_histogram(result.get_counts(qc))
def main():
    hilbertSpace()
main()
