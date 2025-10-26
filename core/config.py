import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API Settings
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = False
    
    # CTMS Integration
    ctms_base_url: str = "https://ctms-api.example.com"
    ctms_api_key: Optional[str] = None
    
    # Blockchain Integration
    starknet_rpc_url: str = "https://starknet-mainnet.infura.io/v3/your_project_id"
    polygon_rpc_url: str = "https://polygon-mainnet.infura.io/v3/your_project_id"
    
    # Crisis Thresholds
    f4_activation_threshold: float = 0.3
    emergency_omega_base: float = 7.5
    
    model_config = {
        "env_file": ".env"
    }

settings = Settings()