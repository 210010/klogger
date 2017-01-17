# klogger: Another Logger for Python #

A task-oriented logger that supports many common features of all other loggers
with additional features of

* multi-threaded logging
* progress logging
* decorator-based logging
* task-trace logging

## Installation ##

`klogger` has no package requirements. ``klogger` can be installed from
pypi repository:

    pip install klogger

## Sample Usages ##

### Basic ###

The basic way of logging is to call `klogger.log`:

    from klogger import log

    log("Hello, this is a log.")

Then the following line of log will be produced:

    I [2017-01-17T13:06:06.202758] (main|d00) <> Hello, this is a log.

This does not seem much different from the standard python logger, except that
now the logger tracks and displays thread and call stack info.

### Function Logging ###

One thing great about klogger is that `log` function also accepts another
function as input:

    from klogger import log

    def do_some_stuff():
        # some stuff
        pass

    log("doing some stuff", do_some_stuff)

Then the logger will run the function for you and report some basic info on
the run.

    I [2017-01-17T13:26:26.114946] (main|d01) <> Now working on 'doing some stuff'...
    I [2017-01-17T13:26:26.114946] (main|d01) <> 'doing some stuff' finished in 0.000s.

Of course, the logger will handle cases where the function could return some
values or accept some parameters:

    from klogger import log

    def add(a, b):
        return a + b

    c = log("adding", add, fargs=(3, 5))
    log("the result is {}".format(c))

Above code could be even more concise if the function supplied is a lambda:

    from klogger import log

    c = log("adding", lambda a, b: a + b, fargs=(3, 5))
    log("the result is {}".format(c))

### Writing to Disks ###

Logs can be written to disk via `set_log_path` function.

    from klogger import log, set_log_path

    set_log_path("logs.txt")
    log("Hello, this is a log.")

### Priority Control ###

The level of priority of the log can be controlled via `t` parameter:

    from klogger import log, WARNING

    log("Hello, this is a warning.", t=WARNING)

### Verbosity Control ###

Which its visibility can be controlled via `set_verbosity` function.

    from klogger import log, WARNING, ERROR, set_visibility

    # Any logs with lower priority than this will be omitted.
    set_visibility(ERROR)

    # This will not be displayed.
    log("Hello, this is a warning.", t=WARNING)

### Decorators ###

Another thing great thing about klogger is that function logging can be
achieved via decorators:

    from klogger import task

    @task
    def add(a, b):
        return a + b

    c = add(3, 5)
    log("the result is {}".format(c))

The logger supports different levels of priorities for decorators:

    from klogger import warning

    @warning
    def add(a, b):
        return a + b

## Future Works ##

`klogger` is still in its development stage. We intend to add more useful and
productive features in the future, so stay alerted!