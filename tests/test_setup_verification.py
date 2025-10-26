import pytest
from pathlib import Path
import sys
import importlib.util

class TestSetupVerification:
    def test_essential_files_exist(self):
        """Test that all essential project files exist"""
        essential_files = [
            "requirements.txt",
            "Dockerfile",
            "oracle/scarindex_service.py",
            "integration/ctms_connector.py",
            "tests/__init__.py",
            "core/config.py",
            "README.md"
        ]
        
        for file_path in essential_files:
            assert Path(file_path).exists(), f"Missing essential file: {file_path}"
    
    def test_directory_structure(self):
        """Test that project directory structure is correct"""
        expected_dirs = [
            "core",
            "governance", 
            "integration",
            "oracle",
            "tests"
        ]
        
        for dir_path in expected_dirs:
            assert Path(dir_path).exists(), f"Missing directory: {dir_path}"
            
    def test_python_imports(self):
        """Test that all Python modules can be imported"""
        modules_to_test = [
            "core.config",
            "integration.ctms_connector",
            "oracle.scarindex_service"
        ]
        
        for module_path in modules_to_test:
            try:
                importlib.import_module(module_path)
            except ImportError as e:
                pytest.fail(f"Failed to import {module_path}: {str(e)}")
                
    def test_requirements_format(self):
        """Test that requirements.txt is properly formatted"""
        req_file = Path("requirements.txt")
        assert req_file.exists(), "requirements.txt is missing"
        
        with open(req_file, 'r') as f:
            requirements = f.readlines()
        
        for line in requirements:
            line = line.strip()
            if line and not line.startswith('#'):
                # Check if requirement has version specifier
                assert '==' in line or '>=' in line or line.startswith('-e'), \
                    f"Requirement {line} should specify version"