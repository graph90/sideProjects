
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def create_bell_circuit(basis="Z"):
    basis = basis.upper()

    if basis not in {"X", "Y", "Z"}:
        raise ValueError("Basis must be X, Y, or Z")

    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)

    if basis == "X":
        qc.h(0)
        qc.h(1)
    elif basis == "Y":
        qc.sdg(0)
        qc.sdg(1)
        qc.h(0)
        qc.h(1)

    qc.measure([0, 1], [0, 1])
    return qc


def simulate_circuit(qc, shots=1024, seed=42):
    if not isinstance(shots, int) or isinstance(shots, bool) or shots <= 0:
        raise ValueError("Shots must be a positive integer")

    backend = AerSimulator(seed_simulator=seed)
    compiled = transpile(qc, backend, seed_transpiler=seed)
    result = backend.run(compiled, shots=shots).result()

    return result.get_counts()


def analyze_results(counts, shots):
    equal = counts.get("00", 0) + counts.get("11", 0)
    unequal = counts.get("01", 0) + counts.get("10", 0)

    return {
        "shots": shots,
        "counts": counts,
        "probabilities": {
            state: count / shots
            for state, count in sorted(counts.items())
        },
        "same_bit_fraction": equal / shots,
        "different_bit_fraction": unequal / shots,
        "correlation": (equal - unequal) / shots,
    }


def hilbert_space(basis="Z", shots=1024, seed=42, show_circuit=True, show_plot=True):
    qc = create_bell_circuit(basis)

    if show_circuit:
        print(qc.draw(output="text"))

    counts = simulate_circuit(qc, shots, seed)
    analysis = analyze_results(counts, shots)

    print(f"\nBasis: {basis.upper()}")
    print(f"Shots: {analysis['shots']}")
    print(f"Counts: {analysis['counts']}")
    print(f"Probabilities: {analysis['probabilities']}")
    print(f"Same-bit fraction: {analysis['same_bit_fraction']:.4f}")
    print(f"Different-bit fraction: {analysis['different_bit_fraction']:.4f}")
    print(f"Correlation: {analysis['correlation']:.4f}")

    if show_plot:
        plot_histogram(counts, title=f"Bell State Measurement — {basis.upper()} Basis")
        plt.tight_layout()
        plt.show()

    return qc, analysis


def run_all_bases(shots=1024, seed=42, show_plots=True):
    results = {}

    for index, basis in enumerate(("X", "Y", "Z")):
        _, analysis = hilbert_space(
            basis=basis,
            shots=shots,
            seed=seed + index,
            show_circuit=(index == 0),
            show_plot=show_plots,
        )
        results[basis] = analysis

    return results


def main():
    run_all_bases(shots=1024, seed=42)


if __name__ == "__main__":
    main()
