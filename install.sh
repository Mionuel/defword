BINARY_NAME="defword"
INSTALL_DIR="/usr/local/bin"

# Aborts the script immediately if an error occured
set -euo pipefail

echo "Granting the execution permission to the binary..."
chmod +x "./$BINARY_NAME"

echo "Moving the binary to $INSTALL_DIR"
sudo mv "./$BINARY_NAME" "$INSTALL_DIR/$BINARY_NAME"

echo "Installation completed!"
echo "Run $BINARY_NAME --help to verify!"