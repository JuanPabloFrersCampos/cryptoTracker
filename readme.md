wsl -> en bashrc se levanta redis automaticamente

celery -A cryptotracker worker -P solo --loglevel=info

celery -A cryptotracker beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler

Celery: Framework de background tasks
Beat: Scheduleo de background tasks, es un plugin de celery
Redis: Broker de mensajes, en este caso se usa en memoria