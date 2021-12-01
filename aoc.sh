#!/usr/bin/env bash

source .config

usage() {
  cat << EOF
usage: $ aoc.sh <command> [<args>]

Commands:
  help - display this help
  $ aoc.sh help

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
EOF
}

show_leaderboard() {
  leaderboard="$1"
  if [[ -z "$leaderboard" ]]; then
    leaderboard="$AOC_DEFAULT_LEADERBOARD"
  fi
  year="$2"
  if [[ -z "$year" ]]; then
    year="$(date +%Y)"
  fi

  leaderboard_url="https://adventofcode.com/${year}/leaderboard/private/view/${leaderboard}.json"
  leaderboard_file="${AOC_DIR}/${year}-${leaderboard}.json"

  mkdir -p "$AOC_DIR"

  if [ ! -f "$leaderboard_file" ]; then
    curl --cookie "session=${AOC_COOKIE}" -s "$leaderboard_url" > "$leaderboard_file"
  else
    last_updated="$(($(date +%s) - $(date -r $leaderboard_file +%s)))"
    if [[ "$last_updated" -gt "$AOC_CACHE_TIME" ]]; then
      curl --cookie "session=${AOC_COOKIE}" -s "$leaderboard_url" > "$leaderboard_file"
    fi
  fi

  jq -r '["SCORE", "STARS", "NAME"],
    ([
      .members[]]
      | sort_by(.local_score)
      | reverse[]
      | [
        .local_score,
        .stars,
        if .name then .name else ("(anonymous user #" + .id + ")") end
        ]
      )
    | @tsv' "$leaderboard_file"
}

generate() {
  file=$(mktemp)

  if [[ -z "$1" ]]; then
    >&2 echo "error: no argument specified."
    >&2 usage
    exit
  fi

  if [[ "$1" == "auto" ]]; then
    if [[ "$(date +%m)" == "12" ]]; then
      year=$(date +%Y)
      day=$(date +%-d)
      if [[ "$(date +%m)" -gt "25" ]]; then
        >&2 echo "error: cannot use auto when it is after 25th december"
        exit
      fi
    else
      >&2 echo "error: cannot use auto when it isn't december"
      exit
    fi
  else
    year="$1"
    day="$2"

    if [[ -z "$day" ]]; then
      >&2 echo "error: day specified, but no year"
      >&2 usage
      exit
    fi
  fi


  day_fmt=$(printf "%02d" "${day}")
  challenge_url="https://adventofcode.com/${year}/day/${day}"
  input_url="${URL}/input"

  input_dir="./inputs/${year}"
  sol_dir="./solutions/${year}"

  input_file="./${input_dir}/${day_fmt}-input"
  sol_file="./${sol_dir}/day_${day_fmt}.py"

  curl -s "${challenge_url}" > "${file}"
  title=$(grep day-desc "${file}" | sed -r 's/.+--- (Day [0-9]+: .+) ---.+/\1/g')

  if [ -z "${title}" ]; then
    >&2 echo "error: challenge at URL ${url} not found"
  fi

  if [ -z "$AOC_COOKIE" ]; then
    >&2 echo "no AOC_COOKIE set. cannot download input automatically"
  else
    mkdir -p "${input_dir}"
    curl -s --cookie "session=${AOC_COOKIE}" "${input_url}" > "${input_file}"

  fi

  if test -f "$sol_file"; then
    >&2 echo "error: file ${sol_file} already exists. i won't override it"
    exit
  fi

  mkdir -p "${sol_dir}"
  cat << EOF > "${sol_file}"
#!/usr/bin/env python

"""
Puzzle Title:     AoC ${year} ${title}
Puzzle Link:      ${challenge_url}
Solution Author:  ${AOC_AUTHOR}
Solution License: MIT
"""

import fileinput


def parse_input():
    data = []
    for line in fileinput.input():
        if line.strip().isnumeric():
            data.append(int(line))
    return data

def solve_part1(data):
  ...


def solve_part2(data):
  ...


def main():
    data = parse_input()

    part1_ans = solve_part1(data)
    print(f"Part 1: {part1_ans}")

    part2_ans = solve_part2(data)
    print(f"Part 2: {part2_ans}")

if __name__ == "__main__":
    main()
EOF

  chmod +x "${sol_file}"
}

cmd="$1"

if [[ -z "$cmd" ]];
  >&2 echo "error: no command specified"
  >&2 usage
  exit
fi

shift
case "$cmd" in
  "help")
    usage
    exit
    ;;
  "lb")
    show_leaderboard $@
    ;;
  "gen")
    generate $@
    ;;
  *)
    >&2 echo "error: invalid command ${cmd}"
    >&2 usage
    exit
    ;;
esac
