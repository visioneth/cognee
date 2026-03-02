<div align="center">

# V33X Memory Engine

### Persistent AI Memory for Autonomous Trading Agents

Built on [Cognee](https://github.com/topoteretes/cognee) | Customized by [@Vision33X](https://github.com/visioneth)

[![GitHub stars](https://img.shields.io/github/stars/visioneth/cognee.svg?style=social&label=Star)](https://GitHub.com/visioneth/cognee/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/visioneth/cognee.svg?style=social&label=Fork)](https://GitHub.com/visioneth/cognee/network/)

</div>

---

## What This Is

An AI memory engine that **never forgets**. Feed it market data, trade history, whale movements, funding rates, news — it builds a living knowledge graph that connects everything and gets smarter over time.

This isn't RAG. This is a **knowledge engine** that understands relationships between data points, tracks how they change, and gives you answers that basic vector search can't.

## Why I Forked This

Every AI trading system I've built loses context when sessions end. Memory compaction destroys nuance. Important patterns vanish. This solves that problem permanently.

**My Use Cases:**
- Store every trade signal, execution, and outcome — learn what actually works
- Track whale wallet movements across chains and connect them to price action
- Build persistent memory for autonomous trading agents (DQN + Transformer)
- Cross-reference funding rates, liquidation data, and kill zone timing
- Never lose context between AI sessions again

## Quick Start

```python
import cognee
import asyncio

async def main():
    # Feed it your data
    await cognee.add("BTC RSI hit 92 at 3PM ET kill zone. Shorted 20x. Hit TP in 4 minutes.")

    # Build the knowledge graph
    await cognee.cognify()

    # Query it later — it remembers everything
    results = await cognee.search("What happens when RSI > 90 during kill zones?")
    print(results)

asyncio.run(main())
```

## The Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| **AI Memory** | Cognee (this repo) | Knowledge graphs + vector search |
| **LLM** | Claude / GPT-4o / Local (LM Studio) | Entity extraction + reasoning |
| **Graph DB** | Kuzu (local) / Neo4j | Relationship storage |
| **Vector DB** | LanceDB (local) | Semantic search |
| **Hardware** | RTX 5090 + 192GB RAM | Local inference + ML training |

## What It Supports

- **30+ data sources** — PDFs, text, images (OCR), audio (transcription), URLs, code files
- **13 search modes** — graph traversal, RAG, chain-of-thought, temporal, Cypher queries
- **8 LLM providers** — OpenAI, Claude, Gemini, Ollama, Mistral, Bedrock, Groq, custom
- **Multiple databases** — Kuzu, Neo4j, LanceDB, ChromaDB, PGVector, PostgreSQL
- **Multi-tenant** — isolated knowledge bases per project/strategy
- **MCP Server** — direct integration with Claude Code and other MCP clients
- **Runs local** — Ollama + Kuzu + LanceDB = zero API costs on your own hardware

## Installation

```bash
pip install cognee
```

Set your LLM key:
```bash
export LLM_API_KEY="your_key_here"
```

For local-only (no API costs):
```bash
export LLM_PROVIDER=ollama
export LLM_MODEL=llama3.1:8b
export LLM_ENDPOINT=http://localhost:11434/v1
```

## Architecture

```
Raw Data (market feeds, trade logs, research, news)
    ↓
ADD — Ingest & classify documents
    ↓
COGNIFY — Extract entities, build knowledge graph
    ↓
SEARCH — Query with 13 retrieval strategies
    ↓
MEMIFY — Enrich with rules and context
    ↓
Living Knowledge Graph (grows smarter every cycle)
```

## Currently Building

- **V33X Autonomous Learner** — DQN + Transformer that trades 24/7 and learns from its own results
- **V33X Signal Engine** — CoinGlass funding + RSI extremes + kill zone timing
- **Whale Intelligence System** — Track smart money across chains in real-time
- **BloFin Copy Trading** — Revenue from copiers seeing consistent green

## Other V33X Projects

| Repo | Description |
|------|-------------|
| [V33X-Autonomous-Learner](https://github.com/visioneth/V33X-Autonomous-Learner) | Self-learning trading AI (PyTorch + DQN) |
| [V33X-RSI-Scanner](https://github.com/visioneth/V33X-RSI-Scanner) | Multi-exchange RSI extreme scanner |
| [V33X-Pine-Scripts](https://github.com/visioneth/V33X-Pine-Scripts) | TradingView indicators |
| [V33X-Whale-Shield](https://github.com/visioneth/V33X-Whale-Shield) | Whale movement tracker |
| [crypto-kill-zones](https://github.com/visioneth/crypto-kill-zones) | Kill zone timing analysis |

---

<div align="center">

**Built during a bear market. Building for the next bull.**

[Follow @Vision33X](https://github.com/visioneth) | [BloFin Partner](https://partner.blofin.com/d/Vision33X)

</div>

---

*Based on [Cognee](https://github.com/topoteretes/cognee) by Topoteretes — Apache 2.0 License. Original documentation and full feature set available in their repo.*
