# AoC

my solutions for [advent of code](https://adventofcode.com/).

## aoc.sh

`aoc.sh` let's you setup template files for your solutions, and optionally
download input. to download input create the file `.cookie` with content:

```
AOC_COOKIE="adventofcode.com session cookie here"
```

to download the input for today and setup a template file run `./aoc.sh auto`.
for any other day use `./aoc.sh <year> <day>` for example `./aoc.sh 2019 3`.

## file structure

solutions are stored in `./solutions/<year>/` with the respective inputs in
`./inputs/<year>`.

## running

scripts take inputs as cli arguments of as stdin so you can either
`./solutions/2020/day_01.py ./inputs/2020/01-input` or
`./solutions/2020/day_01.py < ./inputs/2020/01-input`.
