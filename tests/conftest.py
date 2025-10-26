import pytest
import asyncio
from fastapi.testclient import TestClient

@pytest.fixture
def test_client():
    from oracle.scarindex_service import app
    return TestClient(app)

@pytest.fixture
def sample_metrics():
    return {
        "Narrative": 0.75,
        "Social": 0.65, 
        "Economic": 0.55,
        "Technical": 0.85
    }