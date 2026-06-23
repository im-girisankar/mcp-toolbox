# mcp-toolbox working notes

## Architecture
- `src/mcp_toolbox/registry.py` — central tool registry (dict + decorator)
- `src/mcp_toolbox/tools/` — individual tool modules, auto-register on import
- `src/mcp_toolbox/server.py` — MCP stdio server; lazy-imports `mcp.server.fastmcp.FastMCP`; requires `[server]` extra (`pip install 'mcp-toolbox[server]'`)
- `src/mcp_toolbox/config.py` — ToolboxConfig dataclass + YAML loader
- `src/mcp_toolbox/cli.py` — argparse CLI: serve / list / dump

## Dev workflow
```bash
pip install -e ".[dev]"
ruff check src tests
pytest -q
```

## Adding a new tool
1. Create `src/mcp_toolbox/tools/my_tool.py`
2. Decorate with `@register("my_tool")`
3. Import in `src/mcp_toolbox/tools/__init__.py`
