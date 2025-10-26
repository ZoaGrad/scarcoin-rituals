import pytest
from core.config import Settings

class TestConfig:
    def test_settings_defaults(self):
        """Test that settings have proper defaults"""
        settings = Settings()
        assert settings.api_host == "0.0.0.0"
        assert settings.api_port == 8000
        assert settings.debug is False
        assert settings.f4_activation_threshold == 0.3
        assert settings.emergency_omega_base == 7.5
        assert settings.ctms_base_url == "https://ctms-api.example.com"
        assert settings.starknet_rpc_url == "https://starknet-mainnet.infura.io/v3/your_project_id"
        assert settings.polygon_rpc_url == "https://polygon-mainnet.infura.io/v3/your_project_id"
        assert settings.ctms_api_key is None

    def test_settings_env_override(self, monkeypatch):
        """Test environment variable overrides"""
        monkeypatch.setenv("API_PORT", "9000")
        monkeypatch.setenv("DEBUG", "true")
        monkeypatch.setenv("CTMS_API_KEY", "test-key")
        monkeypatch.setenv("F4_ACTIVATION_THRESHOLD", "0.4")
        
        settings = Settings()
        assert settings.api_port == 9000
        assert settings.debug is True
        assert settings.ctms_api_key == "test-key"
        assert settings.f4_activation_threshold == 0.4