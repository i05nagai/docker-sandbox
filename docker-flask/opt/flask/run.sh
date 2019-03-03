#!/bin/bash

# FLASK_ENV=production
# FLASK_APP=app.sample
gunicorn \
  -w 4 \
  --access-logfile - \
  --error-logfile - \
  --log-file - \
  --log-level info \
  --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' \
  -b 0.0.0.0:5000 \
  app.sample:app
