from __future__ import annotations

import pathlib
from dataclasses import dataclass, field


@dataclass
class ToolboxConfig:
    enabled_tools: list[str] = field(default_factory=list)
    host: str = "0.0.0.0"
    port: int = 8000


def load_config(path: str | None = None) -> ToolboxConfig:
    """Load config from a YAML file or return defaults. YAML is lazy-imported."""
    if path is None:
        return ToolboxConfig()
    try:
        import yaml  # noqa: PLC0415
    except ImportError as e:
        raise ImportError(
            "Install pyyaml to use config files: pip install pyyaml"
        ) from e
    data = yaml.safe_load(pathlib.Path(path).read_text(encoding="utf-8")) or {}
    return ToolboxConfig(
        enabled_tools=data.get("enabled_tools", []),
        host=data.get("host", "0.0.0.0"),
        port=data.get("port", 8000),
    )
