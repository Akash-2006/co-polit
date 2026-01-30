"""Pytest configuration: add project root to path so `src` is importable."""
import sys
from pathlib import Path

# Add project root so "from src.agent import ..." works when running pytest directly
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
