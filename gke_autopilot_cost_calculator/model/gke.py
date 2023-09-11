from pydantic import BaseModel

# """
# Ref: https://cloud.google.com/kubernetes-engine/pricing
# Unit: USD
# Price: per hour
# Region: asia-southeast1
# """


class GKEPriceCluster(BaseModel):
    autopilot: float = 0.10


class GKEPodGeneralPurposeRegular(BaseModel):
    cpu: float = 0.0549
    memory: float = 0.0060729


class GKEPodGeneralPurposeSpot(BaseModel):
    cpu: float = 0.0165
    memory: float = 0.0018219


class GKEPodScaleOutARMRegular(BaseModel):
    cpu: float = 0.0439
    memory: float = 0.0048583


class GKEPodScaleOutX86Regular(BaseModel):
    cpu: float = 0.0692
    memory: float = 0.0076518
