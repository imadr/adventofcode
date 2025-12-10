fn part1(input: &str) -> i32 {
    let mut dial = 50;
    let mut password = 0;

    for line in input.lines() {
        let rest = line
            .chars()
            .skip(1)
            .collect::<String>()
            .parse::<i32>()
            .expect("Not a valid number");

        if line.chars().nth(0) == Some('R') {
            dial += rest;
        } else {
            dial -= rest;
        }

        dial %= 100;

        if dial == 0 {
            password += 1;
        }
    }
    return password;
}

fn part2(input: &str) -> i32 {
    let mut dial = 50;
    let mut password = 0;

    for line in input.lines() {
        let rest = line
            .chars()
            .skip(1)
            .collect::<String>()
            .parse::<i32>()
            .expect("Not a valid number");

        let start = dial;
        if line.starts_with('R') {
            dial += rest;
            password += (start + rest) / 100;
        } else {
            dial -= rest;
            password += (rest + start) / 100;
        }

        dial = dial.rem_euclid(100);
    }
    return password;
}

fn main() {
    let input = "L68
L30
R48
L5
R60
L55
L1
L99
R14
L82";

    println!("{}", part2(input))
}
