import random
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def random_bits(length):
    return [random.randint(0, 1) for _ in range(length)]


def random_bases(length):
    return [random.choice(["Z", "X"]) for _ in range(length)]


def prepare_qubit(bit, basis):
    qc = QuantumCircuit(1, 1)

    if bit == 1:
        qc.x(0)

    if basis == "X":
        qc.h(0)

    return qc


def measure_qubit(qc, basis):
    if basis == "X":
        qc.h(0)

    qc.measure(0, 0)

    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts()

    return int(list(counts.keys())[0])


def simulate_bb84(length=16, eve_present=False):
    alice_bits = random_bits(length)
    alice_bases = random_bases(length)
    bob_bases = random_bases(length)

    bob_results = []

    for i in range(length):
        qc = prepare_qubit(alice_bits[i], alice_bases[i])

        if eve_present:
            eve_basis = random.choice(["Z", "X"])
            eve_bit = measure_qubit(qc, eve_basis)
            qc = prepare_qubit(eve_bit, eve_basis)

        bob_bit = measure_qubit(qc, bob_bases[i])
        bob_results.append(bob_bit)

    matched_indexes = [
        i for i in range(length)
        if alice_bases[i] == bob_bases[i]
    ]

    alice_key = [alice_bits[i] for i in matched_indexes]
    bob_key = [bob_results[i] for i in matched_indexes]

    errors = sum(1 for a, b in zip(alice_key, bob_key) if a != b)

    error_rate = 0
    if len(alice_key) > 0:
        error_rate = (errors / len(alice_key)) * 100

    eve_detected = error_rate > 20

    return {
        "alice_bits": alice_bits,
        "alice_bases": alice_bases,
        "bob_bases": bob_bases,
        "bob_results": bob_results,
        "matched_indexes": matched_indexes,
        "alice_key": alice_key,
        "bob_key": bob_key,
        "errors": errors,
        "error_rate": round(error_rate, 2),
        "eve_detected": eve_detected,
    }