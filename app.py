import streamlit as st
import pandas as pd
from bb84 import simulate_bb84

st.set_page_config(
    page_title="BB84 Quantum Key Distribution",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 BB84 Quantum Key Distribution Simulator")

st.write("Simulate secure key exchange using the BB84 quantum cryptography protocol.")

length = st.slider("Number of Qubits", 8, 64, 16)

eve_present = st.checkbox("Enable Eve Attacker")

if st.button("Run Simulation"):
    result = simulate_bb84(length, eve_present)

    col1, col2, col3 = st.columns(3)

    col1.metric("Matched Bases", len(result["matched_indexes"]))
    col2.metric("Errors", result["errors"])
    col3.metric("Error Rate", f"{result['error_rate']}%")

    st.subheader("Secret Keys")

    st.write("Alice Key")
    st.code("".join(map(str, result["alice_key"])))

    st.write("Bob Key")
    st.code("".join(map(str, result["bob_key"])))

    if eve_present and result["eve_detected"]:
        st.error("Eve detected! Quantum channel is not secure.")
    elif eve_present:
        st.warning("Eve not clearly detected. Try increasing qubits.")
    else:
        st.success("Secure key generated successfully.")

    data = []

    for i in range(length):
        data.append({
            "Index": i,
            "Alice Bit": result["alice_bits"][i],
            "Alice Basis": result["alice_bases"][i],
            "Bob Basis": result["bob_bases"][i],
            "Bob Result": result["bob_results"][i],
            "Basis Match": i in result["matched_indexes"]
        })

    df = pd.DataFrame(data)

    st.subheader("Simulation Table")
    st.dataframe(df, use_container_width=True)