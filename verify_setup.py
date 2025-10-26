#!/usr/bin/env python3
"""Quick verification that all components are working"""

import sys
import subprocess
from pathlib import Path

def check_file_exists(filepath):
    """Check if a file exists"""
    path = Path(filepath)
    if path.exists():
        print(f"✅ {filepath}")
        return True
    else:
        print(f"❌ {filepath} - MISSING")
        return False

def main():
    print("🔍 Verifying ScarCoin Workspace Setup...")
    
    # Check essential files
    essential_files = [
        "requirements.txt",
        "Dockerfile", 
        ".github/workflows/ci.yml",
        "oracle/scarindex_service.py",
        "integration/ctms_connector.py",
        "tests/__init__.py",
        "tests/test_scarindex_core.py",
        "tests/test_api_endpoints.py",
        "core/config.py",
        ".env.example"
    ]
    
    all_files_exist = all(check_file_exists(f) for f in essential_files)
    
    print("\n📊 Summary:")
    if all_files_exist:
        print("✅ All essential files present!")
        print("🚀 Ready to commit and push to trigger CI/CD")
    else:
        print("❌ Some files are missing - please check above")
        sys.exit(1)

if __name__ == "__main__":
    main()