#!/bin/bash

echo Starting Gunicorn.
exec gunicorn app:create_app --bind 0.0.0.0:$PORT --workers 3