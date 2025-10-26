import pytest
from httpx import AsyncClient, ASGITransport
import pytest_asyncio
from typing import AsyncGenerator, Generator

class TestAPIEndpoints:
    @pytest_asyncio.fixture
    async def client(self) -> AsyncGenerator:
        from oracle.scarindex_service import app
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
            yield ac
    
    @pytest.mark.asyncio
    async def test_health_endpoint(self, client):
        """Test health check endpoint"""
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "ScarIndex Oracle"
        
    @pytest.mark.asyncio
    async def test_compute_scarindex_endpoint(self, client):
        """Test ScarIndex computation endpoint"""
        response = await client.post("/compute-scarindex")
        assert response.status_code == 200
        
        data = response.json()
        assert "scar_index" in data
        assert "components" in data
        assert "timestamp" in data
        assert "signature" in data
        
        # Validate response structure
        assert 0 <= data["scar_index"] <= 1
        assert all(comp in data["components"] for comp in ["Narrative", "Social", "Economic", "Technical"])
        
    @pytest.mark.asyncio
    async def test_f4_trigger_check(self, client):
        """Test F4 trigger check endpoint"""
        response = await client.get("/f4-trigger-check")
        assert response.status_code == 200
        
        data = response.json()
        assert "scar_index" in data
        assert "f4_activation_required" in data
        assert isinstance(data["f4_activation_required"], bool)