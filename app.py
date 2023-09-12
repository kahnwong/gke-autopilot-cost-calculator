import streamlit as st

from gke_autopilot_cost_calculator.workload_application import create_chart
from gke_autopilot_cost_calculator.workload_application import create_dataframe
from gke_autopilot_cost_calculator.workload_spark_job import (
    calculate_spark_job_regular_spot_price,
)
from gke_autopilot_cost_calculator.workload_spark_job import (
    calculate_spark_job_scale_out_arm_spot_price,
)

st.set_page_config(
    page_title="GKE Autopilot Cost Calculator",
    page_icon="⎈",
)


st.title("GKE Autopilot Cost Calculator")


with st.sidebar:
    # ---------- Application ---------- #
    cpu = st.number_input(label="cpu", min_value=0.25, max_value=200.0, step=0.25)
    memory = st.number_input(label="memory", min_value=0.5, max_value=200.0, step=0.5)

    # ---------- Spark Job ---------- #
    workload_type = st.radio(
        "Workload Type",
        ["Application", "Spark Jobs"],
    )
    if workload_type == "Spark Jobs":
        executors = st.number_input(
            label="Executors", min_value=1, max_value=100, step=1
        )
        job_duration_seconds = st.number_input(
            label="Job Duration (Minute)", min_value=1, step=1
        )

st.write("Region: asia-southeast1")
st.write("Unit: USD")

# ---------- Application ---------- #
if workload_type == "Application":
    df = create_dataframe(cpu=cpu, memory=memory)
    st.dataframe(df)
    st.pyplot(create_chart(df))
# ---------- Spark Job ---------- #
elif workload_type == "Spark Jobs":
    st.divider()

    regular_spot_price = calculate_spark_job_regular_spot_price(
        cpu=cpu,
        memory=memory,
        executors=executors,
        job_duration_seconds=job_duration_seconds,
    )
    st.write(f"Regular Spot Price: {regular_spot_price:.20f}")

    scale_out_arm_spot_price = calculate_spark_job_scale_out_arm_spot_price(
        cpu=cpu,
        memory=memory,
        executors=executors,
        job_duration_seconds=job_duration_seconds,
    )
    st.write(f"Scale-Out ARM Spot Price: {scale_out_arm_spot_price:.20f}")
