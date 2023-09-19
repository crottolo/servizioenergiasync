uvicorn main:app --reload --log-level debug --host=0.0.0.0 --proxy-headers --forwarded-allow-ips='*'
