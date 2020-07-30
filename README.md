# daemon_thread_logging_sketch
This sketch shows how you can log exceptions of functions running in daemon threads

If you are running a daemon thread on you program and that thread raises an exception, you might not get it in your log file. I made this sketch to find out how to fix that.

Call this script with:
```
python sketch_thread_log.py > thread_log.txt
```

(Yeah, I'm making my own logging statements with prints and redirecting the output to a
file...)

Hope it helps!
