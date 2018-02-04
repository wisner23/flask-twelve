#!/bin/bash

echo Starting Gunicorn.
exec gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 3