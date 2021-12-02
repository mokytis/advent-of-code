# AoC

my solutions for [advent of code](https://adventofcode.com/).

| Year | Days Solved |
| -    | -           |
| 2021 | 1, 2        |
| 2020 | 1, 2, 3     |

## file structure

 - `./solutions/$year/` directory of solutions
 - `./inputs/$year/` directory of  inputs
 - `./aoc.sh` a script to download input and generate solution boilerplate

## aoc.sh

`aoc.sh` let's you generate boilerplate for your solutions, download input, and
view private leaderboards. to download input create the file `.config` with
content:

### config

    AOC_COOKIE="COOKIE FOR adventofcode.com"
    AOC_CACHE_TIME=900
    AOC_DEFAULT_LEADERBOARD="1234567"
    AOC_DIR="/tmp/aoc"
    AOC_AUTHOR="Joe Bloggs <joe@example.com>"

or make a copy of `.config_example`

    cp .config_example .config

### usage

    Usage: $ aoc.sh <command> [<args>]

    Commands:
      gen - fetch input and generate boilerplate
      $ aoc.sh gen [YEAR] [DAY]

        if no YEAR or DAY are specified then today is used
        $ aoc.sh gen

        to fetch input and generate boilerplate for a specific challenge run:
        $ aoc.sh [YEAR] [DAY]

        for example, day 4 of 2020
        $ aoc.sh 2020 4

      lb - display a leaderboard
      $ aoc.sh lb [LEADERBOARD] [YEAR]

        show leaderboard DEFAULT_LEADERBOARD from .config or
        $ aoc.sh lb

        show a specfic leaderboard
        $ aoc.sh lb 1234567

        show a specfic leaderboard for a specific year
        $ aoc.sh lb 1234567 2021

        by default the current year is used

## running

scripts take inputs as cli arguments of as stdin. all of these will work:

    $ ./solutions/2020/day_01.py ./inputs/2020/01-input
    $ ./solutions/2020/day_01.py < ./inputs/2020/01-input
    $ python solutions/2020/day_01.py < ./inputs/2020/01-input
