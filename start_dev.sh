ROOT_DIR="$(pwd)"
VENV_DIR="$ROOT_DIR/.venv"

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating .venv directory..."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists."
fi

echo "Activating venv..."
source "$VENV_DIR/bin/activate"

echo "Installing depedendencies.."
pip install -q -r requirements.txt

echo "Creating a one-time alias to src/main.py.."
alias defword="python $ROOT_DIR/src/main.py"

echo "Done! Now simply type defword during this terminal session to test things out!"
echo "Warning: The changes will be reset after reloading the terminal"