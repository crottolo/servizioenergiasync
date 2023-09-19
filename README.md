# servizioenergiasync
creazione del servizio gunicorn
sudo nano /etc/systemd/system/servizioenergia.service

```
[Unit]
Description=Servizio Energia FASTAPI
After=network.target

[Service]
User=crotti
Group=crotti
WorkingDirectory=/home/crotti/servizioenergiasync
Environment="PATH=/home/crotti/servizioenergiasync/.venv/bin"
ExecStart=/home/crotti/servizioenergiasync/.venv/bin/gunicorn -c /home/crotti/servizioenergiasync/gunicorn_conf.py main:app
ExecReload=/bin/kill -s HUP $MAINPID
KillMode=mixed
TimeoutStopSec=5
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```
sudo systemctl daemon-reload
sudo systemctl enable servizioenergia.service
sudo systemctl start servizioenergia.service
