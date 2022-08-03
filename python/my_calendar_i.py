# TODO: segment tree approach

from collections import namedtuple


Event = namedtuple("Event", ["start", "end"])


class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        new_event = Event(start, end)
        for event in self.events:
            if event.start < new_event.end and new_event.start < event.end:
                return False
        self.events.append(new_event)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
