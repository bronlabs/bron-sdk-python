from __future__ import annotations
from typing import Any, Dict, List, Optional, TypedDict

class address_book_records(TypedDict, total=False):
    records: List[address_book_record]
