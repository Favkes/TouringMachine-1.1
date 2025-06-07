import touringmachine


""" This file contains the parser class used for deconstructing the .tmc file and generating the Touring machine structure. """


class Parser:
    filename: str
    params: dict[str, ...] # type: ignore
    states: list[touringmachine.TouringMachine.State]

    
    def __init__(self, filename: str = 'tape_example.txt'):
        self.filename = filename
        self.params = {}
    
    def load(self) -> None:
        params = {'directives': []}
        with open(self.filename, 'r+') as f:
            lines = f.readlines()

            for line in lines:
                # Comments and empty lines
                if line == '\n' or line.startswith('#'):
                    continue

                # Directives
                content = line.split(":")
                if len(content) == 1:
                    if line.startswith('s'):
                        params['directives'].append(line.replace('\n', '').lstrip().split(' '))
                    continue
                
                # Rest of the parameters
                (key, val) = content

                # Excluding the transitions key cuz it's aesthetical
                if key == 'transitions':
                    continue
                params[key] = val.replace('\n', '').lstrip().split(' ')
        
        self.params = params
    
    def parse(self, params: dict = None) -> None:
        if params is not None: self.params = params

        self.params['blank'] = self.params['blank'][0]
        self.params['start'] = int(self.params['start'][0][1:])
        self.params['tape']  = self.params['tape'][0]

        directives: dict[int, 
                         dict[str, 
                              tuple[str, str, int]
                              ]
                        ] = {}
        # directives[state_id][current_value] = (dir, new_value, next_state_id)

        for directive in self.params['directives']:
            state, key, dir, new_val, next_state = directive

            print(state, key, dir, new_val, next_state)

            id = int(state[1:])
            next_state_id = int(next_state[1:])

            dir = dir.replace('-', '')
            if dir == '>':
                dir = 'R'
            else:
                dir = 'L'

            if id not in directives:
                directives[id] = {}
            directives[id][key] = (dir, new_val, next_state_id)
        
        states = []
        for id, values in directives.items():
            new = touringmachine.TouringMachine.State(id, values)
            states.append(new)
        
        self.states = states

    
    def __str__(self):
        return "Parser class object of Keys: " + str(list(self.params.keys()))

