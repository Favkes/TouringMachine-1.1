

""" This file contains the TuringMachine class that executes .tmc files after parsing via the fileparser module. """


class TuringMachine:
    class State:
        id: int
        cases: dict[str, tuple]
        
        def __init__(self, id: int, cases: dict[str, tuple[str, str, int]]):
            # cases[current_value] = (dir, new_value, new_state_id)
            self.id = id
            self.cases = cases
        
        def __str__(self):
            body = f"s{self.id}:\n"
            for key, values in self.cases.items():
                direction, new_val, next_state_id = values
                body += f"|   {key}: <{new_val}, {direction}, s{next_state_id}>\n"
            return body

        def __repr__(self):
            body = f"s{self.id}"
            for key, values in self.cases.items():
                dir, new_val, next_state_id = values
                body += f" | {key}: <{new_val}, {dir}, s{next_state_id}>"
            return body

    pos: int
    state_id: int
    tape: list[str] | str
    states: tuple[State]
    step_count: int
    max_steps: int
    detailed: bool
    outputs: list[str]
    output: str
    halted: bool

    def __init__(self, start: int = 0, tape: list[str] = [None], states: tuple[State] = None,
                 outputs: list[str] = [None], max_steps: int = 10, detailed: bool = False):
        self.pos = start
        self.state_id = 0
        self.tape = tape if isinstance(tape, list) else list(tape)
        self.states = states
        self.step_count = 0
        self.max_steps = max_steps
        self.detailed = detailed
        self.outputs = outputs
        self.output = None
        self.halted = False
    
    def __str__(self) -> str:
        tapebody = "-"*5 + "[..., "
        lenb4 = 0
        visible_margin = 2
        for i in range(
                max(self.pos - visible_margin, 0),
                min(self.pos + visible_margin + 1, len(self.tape))):
            chunk = str(self.tape[i]) + ", "
            tapebody += chunk

            if i == self.pos:
                lenb4 = len(tapebody) - len(chunk)//2 - 2
        tapebody += "...]" + "-"*5 + "\n"
        arrowbody = " "*lenb4 + "^"

        statebody = ''
        if self.detailed:
            statebody = '\n' + str(self.states[self.state_id])
        else:
            statebody = '\n' + " "*(lenb4-1) + f"s{self.state_id}"

        body =  "Turing Machine class object:\n" + tapebody + arrowbody + statebody #+ statelist
        return body

    def step(self, show_feedback: bool = True) -> bool:
        if self.halted:
            print(
                f"[EXECUTION TERMINATED] The machine is already halted with value {self.output}."
            )
            return False
        if self.step_count >= self.max_steps:
            if show_feedback:
                print(
                    f"[EXECUTION TERMINATED] The machine has reached the max_step limit of {self.max_steps}."
                )
            return False
        self.step_count += 1

        focused = self.tape[self.pos]
        state = self.states[self.state_id]

        assert focused in state.cases, f"No matching action determined for: \n{state}\n{self}"

        dir:            str
        new_val:        str
        next_state_id:  int
        dir, new_val, next_state_id = state.cases[focused]

        # Halting (terminating)
        if new_val in self.outputs:
            self.halted = True
            self.output = new_val
            return False

        # Otherwise executing the instruction
        self.tape[self.pos] = new_val
        
        if dir == 'L':
            self.pos -= 1
        elif dir == 'R':
            self.pos += 1
        
        self.state_id = next_state_id

        if show_feedback:
            print(self, '\n')

        return True

    def run(self, show_feedback: bool = False) -> None:
        while self.step(show_feedback=show_feedback):
            pass
        if self.halted:
            print(
                f"[MACHINE HALTED] With output value: {self.output}."
            )
