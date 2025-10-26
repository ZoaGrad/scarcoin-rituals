import pytest
from oracle.scarindex_service import compute_scarindex, ScarIndexMetrics

class TestScarIndexCore:
    def test_scarindex_computation_basic(self):
        """Test basic ScarIndex computation"""
        metrics = ScarIndexMetrics(
            Narrative=0.8,
            Social=0.7,
            Economic=0.6,
            Technical=0.9
        )
        
        result = compute_scarindex(metrics)
        expected = 0.4*0.8 + 0.3*0.7 + 0.2*0.6 + 0.1*0.9
        
        assert result == pytest.approx(expected)
        assert 0 <= result <= 1
        
    def test_scarindex_boundary_conditions(self):
        """Test edge cases for ScarIndex computation"""
        # Minimum values
        min_metrics = ScarIndexMetrics(
            Narrative=0.0,
            Social=0.0,
            Economic=0.0, 
            Technical=0.0
        )
        assert compute_scarindex(min_metrics) == 0.0
        
        # Maximum values  
        max_metrics = ScarIndexMetrics(
            Narrative=1.0,
            Social=1.0,
            Economic=1.0,
            Technical=1.0
        )
        assert compute_scarindex(max_metrics) == 1.0
        
    def test_f4_crisis_detection(self):
        """Test F4 crisis trigger conditions"""
        crisis_metrics = ScarIndexMetrics(
            Narrative=0.2,  # Critical narrative failure
            Social=0.25,
            Economic=0.3,
            Technical=0.4
        )
        
        scar_index = compute_scarindex(crisis_metrics)
        assert scar_index < 0.3  # Should trigger F4 protocol
        
        healthy_metrics = ScarIndexMetrics(
            Narrative=0.8,
            Social=0.7, 
            Economic=0.6,
            Technical=0.9
        )
        
        healthy_index = compute_scarindex(healthy_metrics)
        assert healthy_index > 0.6  # Should be healthy