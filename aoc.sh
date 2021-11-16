#!/usr/bin/env bash

FILE=$(mktemp)

source .cookie

if [[ "$1" == "auto" ]]; then
  if [[ "$(date +%m)" == "12" ]]; then
    YEAR=$(date +%Y)
    DAY=$(date +%-d)
    if [[ "$(date +%m)" -gt "25" ]]; then
      >&2 echo "error: cannot use auto when it is after 25th december"
      exit
    fi
  else
    >&2 echo "error: cannot use auto when it isn't december"
    exit
  fi
else
  YEAR="$1"
  DAY="$2"
fi


DAY_FMT=$(printf "%02d" "${DAY}")
URL="https://adventofcode.com/${YEAR}/day/${DAY}"
INPUT_URL="${URL}/input"

INPUT_DIR="./inputs/${YEAR}"
SOL_DIR="./solutions/${YEAR}"

INPUT_FILE="./${INPUT_DIR}/${DAY_FMT}-input"
SOL_FILE="./${SOL_DIR}/day_${DAY_FMT}.py"

curl -s "${URL}" > "${FILE}"
TITLE=$(grep day-desc "${FILE}" | sed -r 's/.+--- (Day [0-9]+: .+) ---.+/\1/g')

if [ -z "${TITLE}" ]; then
  >&2 echo "error: challenge at URL ${URL} not found"
fi

if [ -z "$AOC_COOKIE" ]; then
  >&2 echo "no AOC_COOKIE set. cannot download input automatically"
else
  mkdir -p "${INPUT_DIR}"
  curl -s --cookie "session=${AOC_COOKIE}" "${INPUT_URL}" > "${INPUT_FILE}"

fi

if test -f "$SOL_FILE"; then
  >&2 echo "error: file ${SOL_FILE} already exists. i won't override it"
  exit
fi

mkdir -p "${SOL_DIR}"
cat << EOF > "${SOL_FILE}"
#!/usr/bin/env python

"""
Puzzle Title:     AoC ${YEAR} ${TITLE}
Puzzle Link:      ${URL}
Solution Author:  Luke Spademan <info@lukespademan.com>
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

chmod +x "${SOL_FILE}"
