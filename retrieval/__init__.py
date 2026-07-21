"""
retrieval/__init__.py

Top-level retrieval package exporting loaders and chunkers.
"""

from retrieval.loaders import IngestedCorpusLoader, LoadedDocument, TextBlock
from retrieval.chunkers import BaseChunker, LegalChunk, LegalChunker, RecursiveChunker
from retrieval.legal_question_router import LegalQuestionRouter, RoutePlan

__all__ = [
    "IngestedCorpusLoader",
    "LoadedDocument",
    "TextBlock",
    "BaseChunker",
    "LegalChunk",
    "LegalChunker",
    "RecursiveChunker",
    "LegalQuestionRouter",
    "RoutePlan",
]
