import aiohttp
import asyncio
from typing import Dict, Optional

class CTMSConnector:
    def __init__(self, base_url: str = "https://ctms-api.example.com"):
        self.base_url = base_url
        self.session: Optional[aiohttp.ClientSession] = None
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def get_narrative_metrics(self, ritual_id: str = "default") -> Dict:
        """Fetch narrative coherence metrics from CTMS"""
        if not self.session:
            raise RuntimeError("Connector not initialized")
            
        try:
            async with self.session.get(
                f"{self.base_url}/narrative/{ritual_id}/coherence"
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return {
                        "coherence_score": data.get("coherence", 0.5),
                        "sentiment_balance": data.get("sentiment", 0.5),
                        "topic_relevance": data.get("relevance", 0.5)
                    }
                else:
                    return {"coherence_score": 0.5, "error": "CTMS unreachable"}
                    
        except Exception as e:
            return {"coherence_score": 0.5, "error": str(e)}
    
    async def get_ritual_health(self, ritual_id: str) -> Dict:
        """Fetch overall ritual health metrics"""
        # Implementation for ritual-specific metrics
        return {
            "participation_rate": 0.8,
            "completion_ratio": 0.75,
            "energy_intensity": 0.6
        }