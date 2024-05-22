#!/bin/bash

# Kontrola, či je nainštalovaný Render CLI
if ! command -v render &> /dev/null
then
    echo "Render CLI nie je nainštalovaný. Inštalujem..."
    curl -fsSL https://cli.render.com/install.sh | bash
fi

# Prihlásenie do Render
echo "Prihlásenie do Render"
render login

# Nasadenie aplikácie
echo "Nasadzujem aplikáciu..."
render services sync

echo "Aplikácia bola úspešne nasadená."
