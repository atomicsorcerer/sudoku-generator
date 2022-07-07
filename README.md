![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
# Sudoku Generator
A demonstration and use case for the wave function collapse algorithm
## Description
The wave function collapse algorithm is a newer idea generally implemented in games. It can be used to develop random or infinite patterns that all follow a set of restrictions. This can get quite complicated and very specific. One of the simplest ways to represent this algorithm is with a sudoku board. For this implementation, each tile on the board is initialized with all possible values--the values 1 through 9. In quantum mechanics, the inspiration for this algorithm, one data point can contain multiple values. The algorithm goes through and randomly picks tiles to collapse to their lowest entropy (1). Every time this happens, all other tiles in the same group, column, and row loose that new value from their own array of values. This implements the restrictions that make sudoku work. This sudoku generator is a perfect way to represent the capabilities of the wave function collapse algorithm, and to make a few sudoku boards on the side.
## Dependencies
None! This project is built in 100% vanilla python to add transparency to the algorithm. The only included dependency is the `random` module which is built in to the language.
## Usage
For now, there is not much customization possible at run time, so usage is quite simple. The `show_process` option will print out each iteration of the board while it is generating. This is helpful for studying the algorithm and debugging.
```commandline
python main.py <show_process>
```
You can also run the following command to test the program. The first parameter sets how many boards you want generated. It is set to 1000 automatically. None of the boards will be printed to the console.
```commandline
python test.py <iterations_to_run: int>
```
## Authors
This project was created and is maintained [@atomicsorcerer](https://github.com/atomicsorcerer).