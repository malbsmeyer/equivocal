"""
Equivocal: Semantic audio understanding without rendering.

This package enables compositional audio understanding - teaching models
to think about sound conceptually rather than acoustically.
"""

__version__ = "0.1.0"
__author__ = "Max Albsmeyer"

from .engine import SceneAudioEngine
from .extractor import CleanAudioExtractor

__all__ = ["SceneAudioEngine", "CleanAudioExtractor"]