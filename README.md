# Stochastly MCP

<!-- mcp-name: com.stochastly/desktop -->

This small public launcher connects an MCP client to the server shipped with the Stochastly desktop app. The app must be installed, running, and licensed for Atelier or Portfolio. The package contains no Stochastly engine code.

Install with `pip install stochastly-mcp` or run with `uvx stochastly-mcp`. To try the unpublished source, install this directory with `pip install .`.

Configure a local stdio server with command `stochastly-mcp` and no arguments:

- Claude Desktop: add `"stochastly": {"command": "stochastly-mcp"}` under `mcpServers` in `claude_desktop_config.json`.
- Cursor: add the same entry under `mcpServers` in `.cursor/mcp.json`.
- VS Code: add `"stochastly": {"type": "stdio", "command": "stochastly-mcp"}` under `servers` in `.vscode/mcp.json`.

The installed app exposes `node_catalog`, `diagnostics_catalog`, `diagnostic_explain`, `red_flag_check`, `compose_graph`, `backtest_graph`, and other tools. It enforces the licence on every tool call. Without the app, `app_info` explains installation and links to [pricing](https://stochastly.com/pricing).

For a nonstandard installation, set `STOCHASTLY_MCP_SCRIPT` to the installed app's `stochastly_mcp.py`. This is a local path, not a network endpoint.
