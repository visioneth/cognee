"""
V33X Ingest
-----------
Functions to load crypto trading intelligence into Cognee's knowledge graph.

Each function:
  1. Formats raw data as descriptive text (cognee works on natural language)
  2. Calls cognee.add() to stage the data
  3. Calls cognee.cognify() to process it into the knowledge graph

After ingestion, query with v33x.query functions.
"""

import json
import logging
from datetime import datetime, timezone
from typing import Optional

import cognee

from .config import (
    WALLET_LIST_PATH,
    DATASET_WHALES,
    DATASET_SIGNALS,
    DATASET_TRADES,
    DATASET_PRICES,
)

logger = logging.getLogger(__name__)


async def ingest_whale_wallets(wallet_list: Optional[list] = None) -> int:
    """
    Ingest whale wallet data into the knowledge graph.

    Args:
        wallet_list: List of dicts with keys: address, chain, label (optional),
                     last_action (optional), amount_usd (optional).
                     If None, loads from WALLET_LIST_PATH.

    Returns:
        Number of wallets ingested.
    """
    if wallet_list is None:
        try:
            with open(WALLET_LIST_PATH, "r", encoding="utf-8") as f:
                wallet_list = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            logger.error("Failed to load wallet list from %s: %s", WALLET_LIST_PATH, e)
            return 0

    ingested = 0
    for wallet in wallet_list:
        address = wallet.get("address", "unknown")
        chain = wallet.get("chain", "unknown")
        label = wallet.get("label", "unlabeled whale")
        amount = wallet.get("amount_usd", "unknown")
        action = wallet.get("last_action", "holding")
        ts = wallet.get("timestamp", datetime.now(timezone.utc).isoformat())

        text = (
            f"Whale wallet {address} on {chain} ({label}). "
            f"Last action: {action}. "
            f"Amount moved: ${amount}. "
            f"Timestamp: {ts}."
        )
        try:
            await cognee.add(text, dataset_name=DATASET_WHALES)
            ingested += 1
        except Exception as e:
            logger.warning("Failed to add wallet %s: %s", address, e)

    if ingested > 0:
        try:
            await cognee.cognify(datasets=[DATASET_WHALES])
            logger.info("Ingested %d whale wallets into knowledge graph.", ingested)
        except Exception as e:
            logger.error("cognify failed for whales dataset: %s", e)

    return ingested


async def ingest_trading_signals(signals: list) -> int:
    """
    Ingest trading signals into the knowledge graph.

    Args:
        signals: List of dicts with keys: coin, signal_type, direction,
                 score, source, timestamp (optional).

    Returns:
        Number of signals ingested.
    """
    ingested = 0
    for signal in signals:
        coin = signal.get("coin", "unknown")
        sig_type = signal.get("signal_type", "unknown")
        direction = signal.get("direction", "unknown")
        score = signal.get("score", 0)
        source = signal.get("source", "unknown")
        ts = signal.get("timestamp", datetime.now(timezone.utc).isoformat())

        text = (
            f"Trading signal for {coin}: {sig_type} — {direction}. "
            f"Signal score: {score}/10. "
            f"Source: {source}. "
            f"Timestamp: {ts}."
        )
        try:
            await cognee.add(text, dataset_name=DATASET_SIGNALS)
            ingested += 1
        except Exception as e:
            logger.warning("Failed to add signal for %s: %s", coin, e)

    if ingested > 0:
        try:
            await cognee.cognify(datasets=[DATASET_SIGNALS])
            logger.info("Ingested %d trading signals into knowledge graph.", ingested)
        except Exception as e:
            logger.error("cognify failed for signals dataset: %s", e)

    return ingested


async def ingest_trade_history(trades: list) -> int:
    """
    Ingest trade history as episodic memory into the knowledge graph.

    Args:
        trades: List of dicts with keys: coin, direction, entry_price,
                exit_price, pnl_pct, result (win/loss), reason, timestamp.

    Returns:
        Number of trades ingested.
    """
    ingested = 0
    for trade in trades:
        coin = trade.get("coin", "unknown")
        direction = trade.get("direction", "unknown")
        entry = trade.get("entry_price", 0)
        exit_p = trade.get("exit_price", 0)
        pnl = trade.get("pnl_pct", 0)
        result = trade.get("result", "unknown")
        reason = trade.get("reason", "no reason recorded")
        ts = trade.get("timestamp", datetime.now(timezone.utc).isoformat())

        text = (
            f"Trade on {coin}: {direction}. "
            f"Entry: ${entry}, Exit: ${exit_p}. "
            f"P&L: {pnl:+.2f}%. Result: {result}. "
            f"Reason: {reason}. "
            f"Timestamp: {ts}."
        )
        try:
            await cognee.add(text, dataset_name=DATASET_TRADES)
            ingested += 1
        except Exception as e:
            logger.warning("Failed to add trade for %s: %s", coin, e)

    if ingested > 0:
        try:
            await cognee.cognify(datasets=[DATASET_TRADES])
            logger.info("Ingested %d trades into knowledge graph.", ingested)
        except Exception as e:
            logger.error("cognify failed for trades dataset: %s", e)

    return ingested


async def ingest_live_price_data(prices: list) -> int:
    """
    Ingest live price snapshots as context into the knowledge graph.

    Args:
        prices: List of dicts with keys: symbol, price, change_24h_pct,
                volume_24h (optional), timestamp (optional).

    Returns:
        Number of price entries ingested.
    """
    ingested = 0
    ts = datetime.now(timezone.utc).isoformat()

    for price in prices:
        symbol = price.get("symbol", "unknown")
        value = price.get("price", 0)
        change = price.get("change_24h_pct", 0)
        volume = price.get("volume_24h", "unknown")
        entry_ts = price.get("timestamp", ts)

        text = (
            f"{symbol} price: ${value:,}. "
            f"24h change: {change:+.2f}%. "
            f"24h volume: ${volume}. "
            f"Snapshot: {entry_ts}."
        )
        try:
            await cognee.add(text, dataset_name=DATASET_PRICES)
            ingested += 1
        except Exception as e:
            logger.warning("Failed to add price for %s: %s", symbol, e)

    if ingested > 0:
        try:
            await cognee.cognify(datasets=[DATASET_PRICES])
            logger.info("Ingested %d price entries into knowledge graph.", ingested)
        except Exception as e:
            logger.error("cognify failed for prices dataset: %s", e)

    return ingested
