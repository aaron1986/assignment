
RIGHT = 1
LEFT = -1
STAY = 0
MAX_STEPS = 100

def run_TM(tm:dict, tape:list, debug:bool) -> list:
    """Run Turing machine `tm` on `tape` and return the resulting output.

    The machine runs from state 'start' until it halts or has done MAX_STEPS.
    The output is the tape's content from the head onwards.
    If debug is True, print each configuration.

    Preconditions:
    - tm maps (state, symbol) pairs to (symbol, movement, state) triples
        - states are represented by strings
        - symbols are of any hashable type
        - movement is one of RIGHT, LEFT, STAY
    - tape is a non-empty list of symbols
        - the blank symbol is represented as None
    """
    head = 0
    symbol = tape[head]
    state = 'start'
    step = 0
    if debug:
        print(step, state, tape[:head], symbol, tape[head+1:])
    while step < MAX_STEPS and (state, symbol) in tm:
        actions = tm[(state, symbol)]
        tape[head] = actions[0]     # write symbol (may be the same)
        head = head + actions[1]    # move left, right or stay
        state = actions[2]          # next state (may be the same)
        step = step + 1

        if head < 0:
            print('Moved left past the start of the tape')
            head = 0
            step = MAX_STEPS        # force loop to finish
        elif head == len(tape):
            tape.append(None)       # extend tape when needed

        symbol = tape[head]
        if debug:
            print(step, state, tape[:head], symbol, tape[head+1:])
    return tape[head:]