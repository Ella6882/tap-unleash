"""Stream type classes for tap-unleash."""

from __future__ import annotations
from typing import List
from pathlib import Path
from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_unleash.client import UnleashStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class GenericStream(UnleashStream):
    """Common class leveraging conventions to reduce boilerplate"""
    @property
    def schema_filepath(self) -> str:
        return SCHEMAS_DIR / f"{self.name}.json"

class EventsStream(GenericStream):
    """Define custom stream."""
    name = "events"
    path = "admin/events/"
    primary_keys = ["eventsId"] #need to update this
    replication_key = None

# add all streams that have been defined and 
# should be discovered 
DISCOVER_STREAMS : List[UnleashStream] = [
    EventsStream
]