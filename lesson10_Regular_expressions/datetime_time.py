import time

# print("BEFORE")
# time.sleep(3)
# print("AFTER")

#t1 = time.clock() DON"T USE

#print("perf_counter")
# t1 = time.perf_counter()
# print(t1)
# time.sleep(3)
# t2 = time.perf_counter()
# print(f"{t2-t1}")


# print("proc_time")
# t1 = time.process_time()
# #time.sleep(3)
# input("")
# t2 = time.process_time()
# print(f"{t2-t1}")

# print(time.monotonic())
# print(time.time())

# print(time.localtime())
# print(time.gmtime())

# ####################################################################################################################
from datetime import timedelta, datetime, date

t1 = timedelta(days=1)
print(f't1 {t1}')
t2 = timedelta(hours=12)
print(f't2 {t2}')
t3 = t1 + t2
print(f't3 {t3}')
year = timedelta(days=1) * 365
print(f'year {year}')

now = datetime.now()
print(f'now {now}')
print(f'now + year {now+year}')

t333= datetime.fromtimestamp(1)
print(f't333 {t333}')

print(datetime.now() - t333)

print(now.strftime("%Y %H:%M"))
print(f'now {now: %d %b %Y} 19:15')
print(f'{:>now}.fo  {now: %d %b %Y} 19:15')
