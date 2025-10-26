import pytest
from fastapi.testclient import TestClient

class TestAPIEndpoints:
    @pytest.fixture
    def client(self):
        from oracle.scarindex_service import app
        return TestClient(app)
    
    def test_health_endpoint(self, client):
        """Test health check endpoint"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "ScarIndex Oracle"
        
    def test_compute_scarindex_endpoint(self, client):
        """Test ScarIndex computation endpoint"""
        response = client.post("/compute-scarindex")
        assert response.status_code == 200
        
        data = response.json()
        assert "scar_index" in data
        assert "components" in data
        assert "timestamp" in data
        assert "signature" in data
        
        # Validate response structure
        assert 0 <= data["scar_index"] <= 1
        assert all(comp in data["components"] for comp in ["Narrative", "Social", "Economic", "Technical"])
        
    def test_f4_trigger_check(self, client):
        """Test F4 trigger check endpoint"""
        response = client.get("/f4-trigger-check")
        assert response.status_code == 200
        
        data = response.json()
        assert "scar_index" in data
        assert "f4_activation_required" in data
        assert isinstance(data["f4_activation_required"], bool)