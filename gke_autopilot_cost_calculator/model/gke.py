from pydantic import BaseModel

# """
# Ref: https://cloud.google.com/kubernetes-engine/pricing
# Unit: USD
# Price: per hour
# Region: asia-southeast1
# """


class GKEPriceCluster(BaseModel):
    autopilot: float = 0.10


class GKEPodGeneralPurpose(BaseModel):
    cpu_regular: float = 0.0549
    memory_regular: float = 0.0060729
    cpu_spot: float = 0.0165
    memory_spot: float = 0.0018219
    cpu_one_year_commitment: float = 0.04392
    memory_one_year_commitment: float = 0.0048583
    cpu_three_year_commitment: float = 0.030195
    memory_three_year_commitment: float = 0.0033401


class GKEPodScaleOutARM(BaseModel):
    cpu_regular: float = 0.0439
    memory_regular: float = 0.0048583
    cpu_spot: float = 0.0132
    memory_spot: float = 0.0014575
    cpu_one_year_commitment: float = 0.03512
    memory_one_year_commitment: float = 0.0038866
    cpu_three_year_commitment: float = 0.024145
    memory_three_year_commitment: float = 0.0026721


class GKEPodScaleOutX86(BaseModel):
    cpu_regular: float = 0.0692
    memory_regular: float = 0.0076518
    cpu_spot: float = 0.0208
    memory_spot: float = 0.0022956
    cpu_one_year_commitment: float = 0.05536
    memory_one_year_commitment: float = 0.00612144
    cpu_three_year_commitment: float = 0.03806
    memory_three_year_commitment: float = 0.0042085
