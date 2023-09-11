import streamlit as st


st.title("GKE Autopilot Cost Calculator")


compute_type, instance_type = st.columns(2)

with compute_type:
    st.radio(
        "Compute Type",
        ["General Purpose", "Scale-Out: ARM", "Scale-Out: x86"],
    )

with instance_type:
    st.radio(
        "Instance Type",
        ["Regular", "Spot"],
    )


compute_type2, instance_type2 = st.columns(2)

with compute_type2:
    st.radio(
        "Compute Type",
        ["foo"],
    )

with instance_type2:
    st.radio(
        "Instance Type",
        ["bar"],
    )
