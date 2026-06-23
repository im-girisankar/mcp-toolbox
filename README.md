# mcp-toolbox

> **Product/PM angle:** A plug-and-play MCP tool server — add capabilities to any MCP-compatible agent (Claude Desktop, etc.) by registering pure-Python tools with zero boilerplate.

An MCP (Model Context Protocol) server exposing a growing library of agent tools: file search, reliability scoring, and prompt injection detection.

## Status — milestone roadmap

| Tag | Milestone | Status |
|-----|-----------|--------|
| m1  | Package scaffold, tool registry, `repo_search` tool, core tests | Done |
| m2  | `reliability_score` + `redteam_scan` tools, full test suite | Done |
| m3  | Config system, CLI (`mcptb list/dump/serve`), README, packaging | Done |
| m4  | Demo script, edge-case tests, manifest dump | Done |

## Installation

```bash
pip install -e ".[dev]"          # dev + tests
pip install -e ".[server]"       # includes mcp SDK + pyyaml
```

## Usage

```bash
mcptb list          # list registered tools
mcptb dump          # JSON manifest of all tools
mcptb serve         # start MCP server (requires [server] extra)
```

## Use from Claude Desktop

> **Requires the `[server]` extra** — install it first:
> ```bash
> pip install -e ".[server]"
> ```
> This pulls in the `mcp` SDK (the stdio transport) and `pyyaml`.

Add to your Claude Desktop `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "mcp-toolbox": {
      "command": "python",
      "args": ["-m", "mcp_toolbox.cli", "serve"],
      "env": {}
    }
  }
}
```

The server uses **stdio transport** (as required by the MCP spec) and
registers every tool in the registry automatically.  The `mcp` package is
lazy-imported inside `serve()`, so the rest of the CLI (`mcptb list`,
`mcptb dump`) works without the `[server]` extra installed.

## Tools

### `repo_search(directory, keyword, file_pattern="*.py")`
Keyword search over a directory tree. Returns `[{file, line_no, line}]`.

### `reliability_score(answer, context)`
Heuristic faithfulness score (0-1) for an answer vs. its context. Returns `{score, details}`.

### `redteam_scan(text)`
Detects prompt injection / jailbreak patterns. Returns `{risk_level, flags, score}`.
