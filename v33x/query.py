"""
V33X Query
----------
Natural language queries against the V33X knowledge graph.

All functions return cognee search results — lists of graph nodes,
insights, or summaries depending on SearchType used.

Requires data to be ingested first via v33x.ingest.
"""

import logging
from typing import Optional

import cognee
from cognee import SearchType

logger = logging.getLogger(__name__)


async def query_whale_activity(query: Optional[str] = None) -> list:
    """
    Query the knowledge graph for whale wallet activity.

    Args:
        query: Custom query string. Defaults to general whale activity.

    Returns:
        List of knowledge graph results.
    """
    q = query or "Which whale wallets are accumulating or moving large amounts?"
    try:
        results = await cognee.search(SearchType.INSIGHTS, q)
        return results
    except Exception as e:
        logger.error("query_whale_activity failed: %s", e)
        return []


async def query_trading_signals(hours: int = 4, query: Optional[str] = None) -> list:
    """
    Query recent trading signals from the knowledge graph.

    Args:
        hours: Look-back window hint in the query string.
        query: Custom query string override.

    Returns:
        List of knowledge graph results.
    """
    q = query or f"What trading signals fired in the last {hours} hours? Include RSI extremes, funding rate spikes, and kill zone alerts."
    try:
        results = await cognee.search(SearchType.INSIGHTS, q)
        return results
    except Exception as e:
        logger.error("query_trading_signals failed: %s", e)
        return []


async def query_kill_zone_status(query: Optional[str] = None) -> list:
    """
    Query kill zone alert status from the knowledge graph.

    Kill zones are high-probability time-based short entries:
    - 20:00 UTC: 98.4% SHORT win rate (65 trades)
    - 10:00 UTC: 88.9% SHORT win rate (54 trades)

    Returns:
        List of knowledge graph results.
    """
    q = query or "What is the current kill zone status? Are we in a 20:00 UTC or 10:00 UTC short window?"
    try:
        results = await cognee.search(SearchType.INSIGHTS, q)
        return results
    except Exception as e:
        logger.error("query_kill_zone_status failed: %s", e)
        return []


async def query_weekly_trades(query: Optional[str] = None) -> list:
    """
    Query trade history for this week from the knowledge graph.

    Returns:
        List of knowledge graph results with trade details.
    """
    q = query or "What trades were taken this week? Include entry, exit, P&L, and the reason for each trade."
    try:
        results = await cognee.search(SearchType.INSIGHTS, q)
        return results
    except Exception as e:
        logger.error("query_weekly_trades failed: %s", e)
        return []


async def query_market_context(query: Optional[str] = None) -> list:
    """
    Query current market price context from the knowledge graph.

    Returns:
        List of knowledge graph results with recent price data.
    """
    q = query or "What are the current prices of BTC, ETH, and SOL? What is the recent trend?"
    try:
        results = await cognee.search(SearchType.INSIGHTS, q)
        return results
    except Exception as e:
        logger.error("query_market_context failed: %s", e)
        return []


async def query_edge(question: str) -> list:
    """
    Ask any question about the V33X trading edge.

    This is the catch-all query — ask anything the knowledge graph
    has been fed. Works best after running all ingest functions.

    Args:
        question: Free-form natural language question.

    Returns:
        List of knowledge graph results.
    """
    try:
        results = await cognee.search(SearchType.INSIGHTS, question)
        return results
    except Exception as e:
        logger.error("query_edge failed for '%s': %s", question, e)
        return []
