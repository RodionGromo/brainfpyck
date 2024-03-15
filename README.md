# brainfpyck
Python compiler from pseudocode to Brainfuck

# How to use?
1. Write pseudocode in `code.bpf` (abbriviated from brainpyck, read as brainpuck)
2. Edit build.py, set `debug` argument where needed, and run it
3. ???
4. Profit!

# What are those files?
- `bfComp.py` is Brainfuck interpreter I made for this project (maybe has error, maybe unoptimised)
- `code2bf.py` is pseudocode to Brainfuck compiler, the flesh and meat of this project
- `code.bpf` is where you write pseudocode
- `code.bf` is created by `code2bf.py` on successful compilation
- `build.py` is shortcut file, to simplify usage, run it and it will compile pseudocode with `code2bf.py` and run it with `bfComp.py`

## Currently there are no bug catching measures, doublecheck your code!