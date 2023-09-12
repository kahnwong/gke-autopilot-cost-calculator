import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .model import gke

sns.set()  # noqa


def create_dataframe(cpu: float, memory: float) -> pd.DataFrame:
    df = pd.DataFrame(
        [
            # ---------------------------- General Purpose ---------------------------- #
            {
                "Compute Type": "General Purpose",
                "Pricing": "Regular",
                "Price/Hour": (gke.GKEPodGeneralPurpose().cpu_regular * cpu)
                + (gke.GKEPodGeneralPurpose().memory_regular * memory),
            },
            {
                "Compute Type": "General Purpose",
                "Pricing": "Spot",
                "Price/Hour": (gke.GKEPodGeneralPurpose().cpu_spot * cpu)
                + (gke.GKEPodGeneralPurpose().memory_spot * memory),
            },
            {
                "Compute Type": "General Purpose",
                "Pricing": "1 Year Commitment",
                "Price/Hour": (gke.GKEPodGeneralPurpose().cpu_one_year_commitment * cpu)
                + (gke.GKEPodGeneralPurpose().memory_one_year_commitment * memory),
            },
            {
                "Compute Type": "General Purpose",
                "Pricing": "3 Year Commitment",
                "Price/Hour": (
                    gke.GKEPodGeneralPurpose().cpu_three_year_commitment * cpu
                )
                + (gke.GKEPodGeneralPurpose().memory_three_year_commitment * memory),
            },
            # ---------------------------- Scale-Out: ARM ---------------------------- #
            {
                "Compute Type": "Scale-Out: ARM",
                "Pricing": "Regular",
                "Price/Hour": (gke.GKEPodScaleOutARM().cpu_regular * cpu)
                + (gke.GKEPodScaleOutARM().memory_regular * memory),
            },
            {
                "Compute Type": "Scale-Out: ARM",
                "Pricing": "Spot",
                "Price/Hour": (gke.GKEPodScaleOutARM().cpu_spot * cpu)
                + (gke.GKEPodScaleOutARM().memory_spot * memory),
            },
            {
                "Compute Type": "Scale-Out: ARM",
                "Pricing": "1 Year Commitment",
                "Price/Hour": (gke.GKEPodScaleOutARM().cpu_one_year_commitment * cpu)
                + (gke.GKEPodScaleOutARM().memory_one_year_commitment * memory),
            },
            {
                "Compute Type": "Scale-Out: ARM",
                "Pricing": "3 Year Commitment",
                "Price/Hour": (gke.GKEPodScaleOutARM().cpu_three_year_commitment * cpu)
                + (gke.GKEPodScaleOutARM().memory_three_year_commitment * memory),
            },
            # ---------------------------- Scale-Out: x86 ---------------------------- #
            {
                "Compute Type": "Scale-Out: x86",
                "Pricing": "Regular",
                "Price/Hour": (gke.GKEPodScaleOutX86().cpu_regular * cpu)
                + (gke.GKEPodScaleOutX86().memory_regular * memory),
            },
            {
                "Compute Type": "Scale-Out: x86",
                "Pricing": "Spot",
                "Price/Hour": (gke.GKEPodScaleOutX86().cpu_spot * cpu)
                + (gke.GKEPodScaleOutX86().memory_spot * memory),
            },
            {
                "Compute Type": "Scale-Out: x86",
                "Pricing": "1 Year Commitment",
                "Price/Hour": (gke.GKEPodScaleOutX86().cpu_one_year_commitment * cpu)
                + (gke.GKEPodScaleOutX86().memory_one_year_commitment * memory),
            },
            {
                "Compute Type": "Scale-Out: x86",
                "Pricing": "3 Year Commitment",
                "Price/Hour": (gke.GKEPodScaleOutX86().cpu_three_year_commitment * cpu)
                + (gke.GKEPodScaleOutX86().memory_three_year_commitment * memory),
            },
        ]
    )

    df["Price/Month"] = df["Price/Hour"] * 24 * 30

    return df


def create_chart(df: pd.DataFrame) -> plt.figure:
    fig = plt.figure(figsize=(10, 6))

    sns.barplot(
        x="Compute Type",
        y="Price/Month",
        hue="Pricing",
        # hue_order=["should block", "isp", "can block", "ignore"],
        data=df,
    )

    plt.xticks(rotation=90)

    return fig
