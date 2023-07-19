"""Stream type classes for tap-unleash."""

from __future__ import annotations
from typing import List
from pathlib import Path
from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_unleash.client import UnleashStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class GenericPersonnelStream(UnleashStream):
    """Common class leveraging conventions to reduce boilerplate"""
    @property
    def schema_filepath(self) -> str:
        return SCHEMAS_DIR / f"{self.name}.json"

class EventsFeatureToggleStream(GenericPersonnelStream):
    """Define custom stream."""
    name = "events_feature_toggle"
    path = "admin/events/"
    primary_keys = ["featureName"]
    replication_key = None

# add all streams that have been defined and 
# should be discovered 
DISCOVER_STREAMS : List[UnleashStream] = [
    EventsFeatureToggleStream
]