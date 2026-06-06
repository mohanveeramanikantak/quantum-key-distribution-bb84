# 🔐 Quantum Key Distribution (BB84 Protocol)

A beginner-friendly implementation of the **BB84 Quantum Key Distribution (QKD) Protocol** using **Qiskit** and **Streamlit** to demonstrate secure quantum communication and eavesdropper detection.

---

## 📌 Project Overview

BB84 is the world's first Quantum Key Distribution protocol, proposed by Charles Bennett and Gilles Brassard in 1984.

This project simulates:

* Alice sending quantum bits
* Bob receiving and measuring qubits
* Secret key generation
* Eve (attacker) attempting to intercept communication
* Detection of eavesdropping using quantum mechanics

---

## 🚀 Features

* BB84 Quantum Key Distribution Simulation
* Alice & Bob Secure Communication
* Random Bit Generation
* Random Basis Selection
* Secret Key Extraction
* Eve (Attacker) Simulation
* Eavesdropper Detection
* Error Rate Analysis
* Interactive Streamlit Dashboard

---

## 🧠 Quantum Concepts Used

### Qubits

The fundamental unit of quantum information.

### Superposition

Allows qubits to exist in multiple states simultaneously.

### Quantum Measurement

Observation collapses a qubit into a classical state.

### Quantum Bases

* Z Basis (+)
* X Basis (×)

### Quantum Key Distribution (QKD)

Securely exchange encryption keys using quantum mechanics.

---

## 🔒 BB84 Workflow

```text
Alice
│
├── Random Bits
├── Random Bases
│
▼
Quantum Channel
│
▼
Bob
├── Random Bases
├── Measurement
│
▼
Basis Comparison
│
▼
Secret Key Generation
```

---

## 👨‍💻 Technologies Used

* Python
* Qiskit
* Qiskit Aer
* Streamlit
* Pandas

---

## 📂 Project Structure

```text
quantum-key-distribution-bb84/
│
├── app.py
├── bb84.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── screenshots/
│
└── docs/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/mohanveeramanikantak/quantum-key-distribution-bb84.git
cd quantum-key-distribution-bb84
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📊 Sample Output

```text
Matched Bases : 10

Errors : 0

Error Rate : 0%

Alice Key : 1010011010

Bob Key : 1010011010

Secure Key Generated Successfully
```

---

## 🚨 Eve Attacker Simulation

When Eve intercepts quantum communication:

* Quantum states are disturbed
* Error rate increases
* Alice and Bob detect the attack

Example:

```text
Error Rate : 35%

⚠️ Eve Detected!
Quantum Channel Compromised
```

---

## 🎓 Learning Outcomes

* Quantum Computing Fundamentals
* Quantum Cryptography
* Quantum Key Distribution
* Qubits and Superposition
* Quantum Measurement
* Eavesdropper Detection
* Qiskit Development
* Streamlit Dashboard Development

---

## 💼 Resume Point

Implemented the BB84 Quantum Key Distribution protocol using Qiskit, demonstrating secure quantum key exchange, eavesdropper detection, and quantum cryptography principles through an interactive Streamlit application.

---

## 🚀 Future Improvements

* Quantum Network Visualization
* Quantum Channel Animation
* Advanced Eavesdropping Attacks
* Quantum Secure Messaging
* Multi-User Quantum Communication
* Quantum Internet Simulation

---

## 👤 Author

**Mohan Veera Manikanta**

AI Engineer | Full Stack Developer | Product Builder

GitHub:
https://github.com/mohanveeramanikantak

LinkedIn:
https://www.linkedin.com/in/kalepu-mohan-veera-manikanta

---

## ⭐ Support

If you found this project useful, please consider giving it a star and sharing it with others interested in Quantum Computing and Quantum Cryptography.

Happy Quantum Coding! ⚛️🔐
