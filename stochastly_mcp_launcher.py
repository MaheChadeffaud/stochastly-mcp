"""Public launcher; the desktop application's MCP implementation stays in its installer."""

from __future__ import annotations

import os
from pathlib import Path
import runpy
import sys


def installed_script() -> Path:
    override = os.environ.get("STOCHASTLY_MCP_SCRIPT")
    if override:
        return Path(override).expanduser()
    if sys.platform == "win32":
        return Path(os.environ.get("LOCALAPPDATA", "")) / "Stochastly" / "mcp" / "stochastly_mcp.py"
    if sys.platform == "darwin":
        return Path("/Applications/Stochastly.app/Contents/Resources/mcp/stochastly_mcp.py")
    return Path("/opt/stochastly/mcp/stochastly_mcp.py")


def main() -> None:
    script = installed_script()
    if script.is_file():
        # Execute the installed client. Its existing server owns all tools, the loopback
        # connection, and the fail-closed licence gate. The public wheel contains none of it.
        sys.argv = [str(script)]
        runpy.run_path(str(script), run_name="__main__")
        return

    from mcp.server.fastmcp import FastMCP

    server = FastMCP("stochastly")

    @server.tool()
    def app_info() -> dict:
        """Explain how to install and license Stochastly before using its MCP tools."""
        return {
            "ok": False,
            "error": "Stochastly desktop app is not installed. Install and open the app, then activate an Atelier or Portfolio licence.",
            "pricing": "https://stochastly.com/pricing",
        }

    server.run()


if __name__ == "__main__":
    main()
