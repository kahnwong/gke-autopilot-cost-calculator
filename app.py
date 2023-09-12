import streamlit as st

from gke_autopilot_cost_calculator.main import create_chart
from gke_autopilot_cost_calculator.main import create_dataframe


st.title("GKE Autopilot Cost Calculator")


# compute_type, instance_type = st.columns(2)

# with compute_type:
#     st.radio(
#         "Compute Type",
#         ["General Purpose", "Scale-Out: ARM", "Scale-Out: x86"],
#     )

# with instance_type:
#     st.radio(
#         "Instance Type",
#         ["Regular", "Spot"],
#     )


with st.sidebar:
    cpu = st.slider(label="cpu", min_value=0.25, max_value=8.0, step=0.25)
    memory = st.slider(label="memory", min_value=64, max_value=8 * 1024, step=64)

st.write("Region: asia-southeast1")
st.write("Unit: USD")

df = create_dataframe(cpu=cpu, memory=memory)
st.dataframe(df)
st.pyplot(create_chart(df))
