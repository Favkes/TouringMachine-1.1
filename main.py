import turingmachine
import fileparser


def main():
    parser = fileparser.Parser(filename="check_if_mail.txt")
    parser.load()
    parser.parse()
    print(parser)

    machine = turingmachine.TuringMachine(
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

