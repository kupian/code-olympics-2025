# Imagine you have a mystical clock that can fast forward or rewind time by a given number of minutes.
# Your challenge is to write a function that, given the current time and a number of minutes to move
# forward or backward, returns the new time in HH:MM (24-hour format)

class Time:
    hour = 0
    minute = 0
    
    def __init__(self, h, m):
        self.hour = int(h)
        self.minute = int(m)
    
    def add_minutes(self, m):
        while m > 0:
            self.minute += 1
            m -= 1
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
        
        self.hour = self.hour%24
        
    def remove_minutes(self, m):
        while m > 0:
            self.minute -= 1
            m -= 1
            if self.minute == -1:
                self.hour -= 1
                self.minute = 59
        
        self.hour = self.hour%24
        
    def time(self):
        if len(str(self.hour)) == 1:
            hour = f"0{self.hour}"
        else:
            hour = self.hour
        
        if len(str(self.minute)) == 1:
            min = f"0{self.minute}"
        
        else:
            min = self.minute
            
        return f"{hour}:{min}"

current_time = input().split(":")
time = Time(current_time[0], current_time[1])
minutes_to_move = int(input())

if minutes_to_move > 0:
    time.add_minutes(minutes_to_move)
else:
    time.remove_minutes(-minutes_to_move)

print(time.time())