"""
Google Antigravity Plugins Installer CLI
Enables one-command installation of any or all plugins into workspace or global Antigravity configurations.
"""

import os
import sys
import shutil
import json
import argparse

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PLUGINS_DIR = os.path.join(ROOT_DIR, 'plugins')
GLOBAL_CONFIG_DIR = os.path.expanduser(os.path.join('~', '.gemini', 'config', 'plugins'))
WORKSPACE_CONFIG_DIR = os.path.join(os.getcwd(), '.agents', 'plugins')

def list_plugins():
    mp_file = os.path.join(ROOT_DIR, 'marketplace.json')
    if not os.path.exists(mp_file):
        print("Marketplace catalog not found.")
        return
    with open(mp_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\nAvailable Google Antigravity Plugins ({len(data['plugins'])} total):\n")
    print(f"{'Plugin Name':<32} | {'Version':<8} | {'Description'}")
    print("-" * 80)
    for p in data['plugins']:
        desc = p['description'][:65] + '...' if len(p['description']) > 65 else p['description']
        print(f"{p['name']:<32} | {p['version']:<8} | {desc}")
    print("\nInstall with: python scripts/install.py <plugin-name> [--scope global|project]")

def list_mcp_servers():
    mp_file = os.path.join(ROOT_DIR, 'marketplace.json')
    if not os.path.exists(mp_file):
        print("Marketplace catalog not found.")
        return
    with open(mp_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("\nGoogle Antigravity Plugins with MCP Servers:\n")
    print(f"{'Plugin Name':<20} | {'Transport':<12} | {'Server Info / Command'}")
    print("-" * 80)
    for p in data['plugins']:
        if p.get('capabilities', {}).get('hasMcp'):
            mcp_path = os.path.join(PLUGINS_DIR, p['name'], 'mcp_config.json')
            info = "Configured"
            mcp_type = "Stdio/HTTP"
            if os.path.exists(mcp_path):
                try:
                    with open(mcp_path, 'r', encoding='utf-8') as mf:
                        mcp_data = json.load(mf).get('mcpServers', {})
                        for s_name, s_cfg in mcp_data.items():
                            if 'url' in s_cfg:
                                mcp_type = "HTTP"
                                info = s_cfg['url']
                            elif 'command' in s_cfg:
                                mcp_type = "Stdio"
                                info = f"{s_cfg['command']} {' '.join(s_cfg.get('args', []))}"
                except Exception:
                    pass
            print(f"{p['name']:<20} | {mcp_type:<12} | {info[:45]}")
    print("\n")

def update_global_config(plugin_name: str, version: str = "1.0.0"):
    try:
        config_path = os.path.expanduser(os.path.join('~', '.gemini', 'config', 'config.json'))
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            plugins = data.setdefault('plugins', {})
            if plugin_name not in plugins:
                plugins[plugin_name] = {
                    "enabled": True,
                    "installedFrom": {
                        "id": f"antigravity-plugins-official/plugin/{plugin_name}",
                        "marketplace": "antigravity-plugins-official",
                        "version": version
                    }
                }
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
    except Exception as e:
        print(f"  (Note: could not update config.json automatically: {e})")

def install_plugin(name: str, scope: str = 'project'):
    src_plugin = os.path.join(PLUGINS_DIR, name)
    if not os.path.exists(src_plugin):
        print(f"Error: Plugin '{name}' does not exist in {PLUGINS_DIR}")
        return False
        
    dest_base = GLOBAL_CONFIG_DIR if scope == 'global' else WORKSPACE_CONFIG_DIR
    os.makedirs(dest_base, exist_ok=True)
    dest_plugin = os.path.join(dest_base, name)
    
    if os.path.exists(dest_plugin):
        shutil.rmtree(dest_plugin)
    shutil.copytree(src_plugin, dest_plugin)

    if scope == 'global':
        version = "1.0.0"
        pj = os.path.join(src_plugin, 'plugin.json')
        if os.path.exists(pj):
            try:
                with open(pj, 'r', encoding='utf-8') as f:
                    version = json.load(f).get('version', '1.0.0')
            except Exception:
                pass
        update_global_config(name, version)

    print(f"✓ Installed '{name}' into {dest_plugin}")
    return True

def install_all(scope: str = 'project'):
    plugins = [p for p in os.listdir(PLUGINS_DIR) if os.path.isdir(os.path.join(PLUGINS_DIR, p))]
    print(f"Installing all {len(plugins)} plugins to scope: {scope}...")
    success = 0
    for p in plugins:
        if install_plugin(p, scope):
            success += 1
    print(f"\n✓ Successfully installed {success}/{len(plugins)} plugins!")
    print(f"Destination: {GLOBAL_CONFIG_DIR if scope == 'global' else WORKSPACE_CONFIG_DIR}")
    print("Restart your Antigravity session to discover new plugins.")

def main():
    parser = argparse.ArgumentParser(description="Google Antigravity Plugins Installer")
    parser.add_argument('plugin', nargs='?', help='Name of plugin to install (or omit to list/use flags)')
    parser.add_argument('--all', action='store_true', help='Install all 57 plugins')
    parser.add_argument('--list', action='store_true', help='List all available plugins')
    parser.add_argument('--mcp', action='store_true', help='List all plugins featuring MCP servers')
    parser.add_argument('--scope', choices=['project', 'global'], default='project', help='Install scope (default: project)')

    args = parser.parse_args()

    if args.list:
        list_plugins()
    elif args.mcp:
        list_mcp_servers()
    elif args.all:
        install_all(args.scope)
    elif args.plugin:
        install_plugin(args.plugin, args.scope)
    else:
        list_plugins()

if __name__ == '__main__':
    main()
