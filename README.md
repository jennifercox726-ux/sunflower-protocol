# Sunflower Protocol: Ephemeral State Routing (ESR)

**A hardened, non-static routing layer for resilient decentralized infrastructure.**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) 
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

## Overview

The Sunflower Protocol implements **Ephemeral State Routing (ESR)** — a dynamic routing paradigm that eliminates permanent attack surfaces in decentralized networks. Traditional static routing (BGP, mesh protocols) creates persistent vulnerabilities: fixed IPs, predictable paths, and centralized chokepoints. ESR makes routes **time-bound, sharded, and heuristically adaptive**, delivering sovereign resilience for high-stakes use cases like energy grids, DePIN networks, institutional comms, and censorship-resistant infrastructure.

Built for the **next billion users** in a sovereign world.

## Problem

- Static infrastructure = massive attack surface (DDoS, surveillance, single points of failure).
- Centralized routing fails under resilience stress (outages, geopolitical interference).
- Privacy leakage through persistent state and predictable paths.

## Solution: Ephemeral State Routing (ESR)

Sunflower Shield turns routing into an ephemeral, living system:

- **Node Persistence**: Time-bound session layers with automatic expiration.
- **State Sharding**: Distributed fragmentation across nodes for maximum privacy and fault tolerance.
- **Traffic Pathing**: Dynamic heuristic routing prioritizing uptime, latency, and trust metrics (target: 99.9%+ resilience).
- **OTA Injection**: Seamless, zero-downtime protocol upgrades without restarting the network.

### Core Mechanics (High-Level)
```python
# Example from sunflower_shield.py
route_id = hashlib.sha256(data_packet + timestamp).hexdigest()
# Routes evaporate and reform based on current state