from .model import gke


def calculate_spark_job_regular_spot_price(
    cpu: float, memory: float, executors: int, job_duration_seconds: int
) -> float:
    price_per_node_in_hour = (gke.GKEPodGeneralPurpose().cpu_spot * cpu) + (
        gke.GKEPodGeneralPurpose().memory_spot * memory
    )
    price_per_node_in_minute = price_per_node_in_hour / 60 * job_duration_seconds

    return price_per_node_in_minute * (1 + executors)  # need to also add driver node


def calculate_spark_job_scale_out_arm_spot_price(
    cpu: float, memory: float, executors: int, job_duration_seconds: int
) -> float:
    price_per_node_in_hour = (gke.GKEPodScaleOutARM().cpu_spot * cpu) + (
        gke.GKEPodScaleOutARM().memory_spot * memory
    )
    price_per_node_in_minute = price_per_node_in_hour / 60 * job_duration_seconds

    return price_per_node_in_minute * (1 + executors)  # need to also add driver node
