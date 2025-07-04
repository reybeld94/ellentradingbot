"""Utility functions for symbol conversions."""

from typing import Dict

# Mapping from TradingView format to Alpaca format
_SYMBOL_MAP: Dict[str, str] = {
    'BTCUSD': 'BTC/USD',
    'ETHUSD': 'ETH/USD',
}


def map_symbol_to_alpaca(symbol: str) -> str:
    """Map TradingView symbols to Alpaca symbols."""
    return _SYMBOL_MAP.get(symbol, symbol)
