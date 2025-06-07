import touringmachine
import fileparser


""" This code serves as an example on how to use this package. """

def main():
    parser = fileparser.Parser(filename="check_if_mail.tmc")
    parser.load()
    parser.parse()
    print(parser)

    machine = touringmachine.TouringMachine(
        start=0,
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

