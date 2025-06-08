import turingmachine
import fileparser


""" This code serves as an example on how to use this package. """

def main():
    parser = fileparser.Parser(filename="is_that_mail.tmc")
    parser.load()
    parser.parse()
    print(parser)

    machine = turingmachine.TuringMachine(
        start=parser.params['index'],
        tape=parser.params['tape'],
        states=parser.states,
        outputs=parser.params['end'],
        max_steps=int(1e2),
        detailed=True
    )
    print(machine.states)
    machine.run(show_feedback=True)


if __name__=="__main__":
    main()

