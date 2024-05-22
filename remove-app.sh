#!/bin/bash

# Prihlásenie do Render
echo "Prihlásenie do Render"
render login

# Získanie ID služieb
WEB_SERVICE_ID=$(render services list | grep my-flask-app | awk '{print $1}')
DB_SERVICE_ID=$(render services list | grep mongodb | awk '{print $1}')

# Odstránenie webovej služby
if [ -n "$WEB_SERVICE_ID" ]; then
    echo "Odstraňujem webovú službu..."
    render services delete $WEB_SERVICE_ID --yes
else
    echo "Webová služba nebola nájdená."
fi

# Odstránenie databázovej služby
if [ -n "$DB_SERVICE_ID" ]; then
    echo "Odstraňujem databázovú službu..."
    render services delete $DB_SERVICE_ID --yes
else
    echo "Databázová služba nebola nájdená."
fi

echo "Aplikácia bola úspešne odstránená."
