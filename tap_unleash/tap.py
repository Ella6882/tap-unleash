"""Unleash tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_unleash.client import UnleashStream
from tap_unleash.streams import DISCOVER_STREAMS

class TapUnleash(Tap):
    """Unleash tap class."""
    name = "tap-unleash"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "api_url",
            th.StringType,
            required=True,
            secret=True,
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[UnleashStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [_cls(self) for _cls in DISCOVER_STREAMS]

if __name__ == "__main__":
    TapUnleash.cli()