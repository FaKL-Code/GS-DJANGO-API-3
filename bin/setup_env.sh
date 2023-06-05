python3 -m venv .venv
activate() {
    .venv/bin/activate
    echo "instalando requirements.txt"
    pip install -r requirements.txt
}
activate