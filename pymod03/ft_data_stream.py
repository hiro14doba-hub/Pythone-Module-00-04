import random
from typing import Generator
def gen_event()->Generator[tuple,None,None]:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'release', 'use']
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player,action)

def consume_event(event_list: list)->Generator[tuple,None,None]:
    while len(event_list)>0:
        idx = random.randrange(len(event_list))
        yield event_list.pop(idx)

def main()->None:
    print("=== Game Data Stream Processor ===")
    event_stream = gen_event()
    for i in range(1000):
        event = next(event_stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    ten_events = [next(event_stream) for _ in range(10)]
    print(f"Builtlist of 10 events: {ten_events}")
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")

if __name__ == "__main__":
    main()

