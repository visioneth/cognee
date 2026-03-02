"""
V33X Configuration
------------------
Set these via environment variables or a .env file.
Never hardcode API keys in source code.
"""

import os

# --- Exchange APIs ---
BLOFIN_API_KEY = os.getenv("BLOFIN_API_KEY", "")
BLOFIN_SECRET = os.getenv("BLOFIN_SECRET", "")
BLOFIN_PASSPHRASE = os.getenv("BLOFIN_PASSPHRASE", "")

# --- Data Source APIs ---
COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY", "")
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY", "")
COINMARKETCAP_API_KEY = os.getenv("COINMARKETCAP_API_KEY", "")
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY", "")        # Solana on-chain
CRYPTOQUANT_API_KEY = os.getenv("CRYPTOQUANT_API_KEY", "")

# --- Wallet Tracking ---
WALLET_LIST_PATH = os.getenv(
    "V33X_WALLET_LIST_PATH",
    "v33x/data/whale_wallets.json"
)

# --- Cognee Dataset Names ---
DATASET_WHALES = "v33x_whales"
DATASET_SIGNALS = "v33x_signals"
DATASET_TRADES = "v33x_trades"
DATASET_PRICES = "v33x_prices"

# --- Signal Thresholds ---
FUNDING_EXTREME_SHORT = -100   # % annualized — extreme negative = potential long
FUNDING_EXTREME_LONG = 100     # % annualized — extreme positive = potential short
RSI_OVERSOLD = 10              # RSI below this = long signal
RSI_OVERBOUGHT = 90            # RSI above this = short signal

# --- Kill Zones (UTC hours) ---
KILL_ZONE_20_UTC = 20          # 98.4% SHORT WR (65 trades)
KILL_ZONE_10_UTC = 10          # 88.9% SHORT WR (54 trades)
