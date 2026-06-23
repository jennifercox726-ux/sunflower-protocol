# Sunflower Protocol: Ephemeral State Routing (ESR)

**Hardened, non-static routing for resilient decentralized infrastructure.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Sunflower CI](https://github.com/jennifercox726-ux/sunflower-protocol/actions/workflows/ci.yml/badge.svg)](https://github.com/jennifercox726-ux/sunflower-protocol/actions/workflows/ci.yml)

## Overview

The Sunflower Protocol implements **Ephemeral State Routing (ESR)** — a dynamic routing system that eliminates permanent attack surfaces by making routes time-bound, sharded, and adaptive. Designed for sovereign resilience in energy grids, DePIN networks, and high-stakes decentralized infrastructure.

## Core Features
- **Node Persistence**: Time-bound sessions that expire automatically.
- **State Sharding**: Distributed fragmentation for privacy and fault tolerance.
- **Traffic Pathing**: Dynamic heuristic routing prioritizing uptime and trust.
- **OTA Injection**: Seamless protocol upgrades with zero downtime.

## Quick Start

```bash
git clone https://github.com/jennifercox726-ux/sunflower-protocol.git
cd sunflower-protocol
pip install -r requirements.txt
python sunflower_shield.py
python gateway.py
