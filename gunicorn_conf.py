from multiprocessing import cpu_count

bind = "0.0.0.0:8000"

# # Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'
# accesslog = '-'
# # Logging Options
# loglevel = 'debug'
forwarded_allow_ips = '*'
accesslog = './log/access.log'
errorlog =  './log/error.log'
# capture_output = True
# reload = True
# reload_engine = "auto"
# errorlog = '-'
loglevel = 'info'
# accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# gunicorn main:app -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 --access-logfile - --error-logfile -  --log-level debug --forwarded-allow-ips=*