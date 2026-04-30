BINARY_NAME="defword"
INSTALL_DIR="/usr/local/bin"

DATA_DIR="$HOME/.local/share/defword"

# Aborts the script immediately if an error occured
set -euo pipefail

echo "Deleting the tool's history and cache directory.. ($DATA_DIR)"
sudo rm -rf "$DATA_DIR"

echo "Deleting the tool itself.. ($INSTALL_DIR/$BINARY_NAME)"
sudo rm "$INSTALL_DIR/$BINARY_NAME"

echo "Defword unistalled! See ya!"