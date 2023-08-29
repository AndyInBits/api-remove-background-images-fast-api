#!/bin/sh

cd /app

pytest
uvicorn main:app --port 5000 --reload --host 0.0.0.0