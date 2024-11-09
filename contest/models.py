from django.db import models
import datetime
# Create your models here.
class Contest(models.Model):
    join_deadline = models.DateTimeField()
    joining_closed = models.BooleanField(default=False)

    def isOpen() -> bool:
        c = Contest.objects.first()
        closed = c.joining_closed
        deadline = c.join_deadline
        d = str(deadline)
        year = int(d[0:4])
        month =int(d[5:7])
        day = int(d[8:10])
        hour = int(d[11:13])
        minute = int(d[14:16])
        second = int(d[17:19])
        deadline = datetime.datetime(year, month, day, hour, minute, second)
        now = datetime.datetime.now()
        return not closed and now < deadline