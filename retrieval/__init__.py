"""
retrieval/__init__.py

Top-level retrieval package exporting loaders and chunkers.
"""

from retrieval.loaders import IngestedCorpusLoader, LoadedDocument, TextBlock
from retrieval.chunkers import BaseChunker, LegalChunk, LegalChunker, RecursiveChunker
from retrieval.legal_question_router import LegalQuestionRouter, RoutePlan
from retrieval.turbopuffer_store import TurbopufferStore
from retrieval.index import HybridIndexer, InMemoryVectorStore

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
    "TurbopufferStore",
    "HybridIndexer",
    "InMemoryVectorStore",
]
