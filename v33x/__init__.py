"""
V33X Extension for Cognee
--------------------------
Persistent AI memory for autonomous crypto trading.

Ingests whale wallet activity, trading signals, kill zone alerts,
and trade history into Cognee's knowledge graph. Query with natural
language to understand what smart money is doing in real time.

Usage:
    from v33x.ingest import ingest_whale_wallets, ingest_trading_signals
    from v33x.query import query_whale_activity, query_kill_zone_status

    await ingest_whale_wallets(wallets)
    results = await query_whale_activity()
"""

from .ingest import (
    ingest_whale_wallets,
    ingest_trading_signals,
    ingest_trade_history,
    ingest_live_price_data,
)
from .query import (
    query_whale_activity,
    query_trading_signals,
    query_kill_zone_status,
    query_weekly_trades,
)

__all__ = [
    "ingest_whale_wallets",
    "ingest_trading_signals",
    "ingest_trade_history",
    "ingest_live_price_data",
    "query_whale_activity",
    "query_trading_signals",
    "query_kill_zone_status",
    "query_weekly_trades",
]
