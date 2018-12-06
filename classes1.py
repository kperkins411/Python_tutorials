import datetime

class Logger(object):
    def log(self, message):
        print (message)

class TimestampLogger(Logger):
    def log(self, message):
        message = "{ts} {msg}".format(ts=datetime.datetime.now().isoformat(),
                                      msg=message)
        super().log(message)


l = Logger()
l.log('hi!')
t = TimestampLogger()
t.log('hi!')