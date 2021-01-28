
python3 stock_code.py &
compteur=$((1))

while ps $! >/dev/null 2>&1; do

if [ $compteur -le 10 ]; then
sleep 1
compteur=$((compteur+1))
else
kill -SIGKILL $! >/dev/null 2>&1
COMMANDE_INTERROMPUE=true
break
fi

done

if $COMMANDE_INTERROMPUE; then
echo "La commande a été interrompue"
else
echo "La commande n'a pas été interrompue"
fi