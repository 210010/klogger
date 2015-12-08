from datetime import datetime
import time
import inspect

def __getPathInfo():
    for item in inspect.stack():
        if item and __file__ not in item:
            return item[1]

    return __file__

def log(jobName, func, to_file=False):
    file = __getPathInfo()
    slog = "Working on {}...".format(jobName)

    print(slog)
    with open("{}.log".format(file), "w+") as f:
        f.write("[{}] In {}: {}\n".format(datetime.now(), file, slog))

    t = datetime.now()
    r = func()

    elog = "{} took {} seconds.".format(jobName.capitalize(), (datetime.now() - t).total_seconds())

    print(elog)

    if (to_file):
        with open("{}.log".format(file), "a") as f:
            f.write("[{}] In {}: {}\n".format(datetime.now(), file, elog))

    return r

def main():
    log("testing", lambda: time.sleep(1))

if __name__ == "__main__":
    main()