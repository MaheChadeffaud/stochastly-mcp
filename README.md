# Stochastly MCP

<!-- mcp-name: com.stochastly/desktop -->

This small public launcher connects an MCP client to the server shipped with the Stochastly desktop app. The app must be installed, running, and licensed for Atelier or Portfolio. The package contains no Stochastly engine code.

Install with `pip install stochastly-mcp` or run with `uvx stochastly-mcp`. To try the unpublished source, install this directory with `pip install .`.

Configure a local stdio server with command `stochastly-mcp` and no arguments:

- Claude Desktop: add `"stochastly": {"command": "stochastly-mcp"}` under `mcpServers` in `claude_desktop_config.json`.
- Cursor: add the same entry under `mcpServers` in `.cursor/mcp.json`.
- VS Code: add `"stochastly": {"type": "stdio", "command": "stochastly-mcp"}` under `servers` in `.vscode/mcp.json`.

The server exposes 29 tools, among them `node_catalog`, `compose_graph`, `backtest_graph`, `red_flag_check`, `adversarial_check`, `portfolio_combine` and `export_paper`. The installed app runs them and checks the licence on every call: `portfolio_combine` needs Portfolio, every other tool Atelier or Portfolio.

Without the app, the launcher lists the same 29 tools (names, descriptions, input schemas and annotations from `stochastly_mcp_data/tools_manifest.json`, generated from the app's server), so a client can see what the server offers. Each description then starts with a note that the desktop app is required, and every call returns a structured answer with `ok: false`, the edition needed and a link to [pricing](https://stochastly.com/pricing). The manifest is metadata only.

For a nonstandard installation, set `STOCHASTLY_MCP_SCRIPT` to the installed app's `stochastly_mcp.py`. This is a local path, not a network endpoint.
