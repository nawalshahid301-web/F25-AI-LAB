# Lab 2 - Task 3: stateful classroom agent (remembers the previous target mode)
# Same thresholds and same priority (empty room first) as the reflex agent.

class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"

        send_command = target != self.previous_mode
        old_mode = self.previous_mode
        self.previous_mode = target
        return old_mode, target, send_command


agent = StatefulClassroomAgent()
percepts = [(29, True), (29, True), (20, True),
            (26, True), (19, True), (29, False)]

for step, percept in enumerate(percepts, 1):
    previous, target, send = agent.act(*percept)
    outcome = "send command" if send else "no command"
    print(f"{step} | previous={previous} | percept={percept} | target={target} | {outcome}")