# Lab 2 - edge case: noisy readings around 26 C
# A stateful agent that only remembers the last mode does NOT give hysteresis.

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
noisy = [25.9, 26.1, 25.9, 26.1, 25.9, 26.1]

for step, temp in enumerate(noisy, 1):
    previous, target, send = agent.act(temp, True)
    outcome = "send command" if send else "no command"
    print(f"{step} | previous={previous} | temp={temp} | target={target} | {outcome}")