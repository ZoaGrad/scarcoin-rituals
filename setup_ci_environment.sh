#!/bin/bash
# setup_ci_environment.sh

echo "🔧 Setting up CI test environment..."

# Create test directory structure
mkdir -p tests/core tests/governance tests/integration

# Create basic __init__.py files
touch tests/__init__.py
touch tests/core/__init__.py
touch tests/governance/__init__.py  
touch tests/integration/__init__.py

# Copy the test files we created
echo "📁 Created test directory structure"

# Install dev dependencies
pip install -r requirements.txt

# Run initial tests to verify setup
echo "🚀 Running initial test suite..."
pytest tests/ -v

echo "✅ CI environment setup complete!"
echo "📊 Next: Push to GitHub to trigger CI workflow"