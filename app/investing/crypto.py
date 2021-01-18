import os
import json
import dateutil.parser
import datetime

from pydantic import BaseModel
import cbpro

coinbase_client = cbpro.AuthenticatedClient(
    os.environ['COINBASE_API_KEY'],
    os.environ['COINBASE_API_SECRET'],
    os.environ['COINBASE_API_PASSPHRASE'])


class Portfolio(BaseModel):
    price: str
    current_value: str
    usd_invested: str
    roi: str


def get_fills():
    fills_gen = coinbase_client.get_fills('BTC-USD')

    fills_parsed = list()
    for fill in list(fills_gen):
        fills_parsed.append({
            "created_at": dateutil.parser.parse(fill['created_at']),
            'trade_id': fill['trade_id'],
            'product_id': fill['product_id'],
            'order_id': fill['order_id'],
            'user_id': fill['user_id'],
            'profile_id': fill['profile_id'],
            'liquidity': fill['liquidity'],
            'price': float(fill['price']),
            'size': float(fill['size']),
            'side': fill['side'],
            'settled': fill['settled'],
            'usd_volume': float(fill['usd_volume'])
        })

    return fills_parsed


def get_invested():
    fills = get_fills()
    fills_sorted = sorted(fills, key=lambda x: x['created_at'])
    beginning = dateutil.parser.parse("2020-11-01T19:34:06.919Z")
    usd_sum = 0
    btc_size = 0
    for fill in fills_sorted:
        if fill['created_at'] > beginning:
            usd_sum += fill['usd_volume']
            btc_size += fill['size']
    return {
        'usd': usd_sum,
        'btc': btc_size
    }


def get_price():
    public_client = cbpro.PublicClient()
    ticker = public_client.get_product_ticker(product_id='BTC-USD')
    return float(ticker['bid'])


def get_crypto_portfolio():
    sums = get_invested()
    usd_invested = sums['usd']
    price = get_price()
    value = sums['btc'] * price
    return {
        'price': f"{price:.2f}",
        'current_value': f"{value:.2f}",
        'usd_invested': f"{usd_invested:.2f}",
        'roi': f"{100.0 * value / usd_invested - 100:.2f}"
    }
