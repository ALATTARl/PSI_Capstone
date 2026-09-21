import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from analytics import analyze_traffic
from network import fetch_uuid


def test_fetch_uuid():
    uuid_val = fetch_uuid()
    assert uuid_val is None or isinstance(uuid_val, str)


def test_analyze_traffic_missing_file():
    result = analyze_traffic("non_existent_file.csv")
    assert result is None