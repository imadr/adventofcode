fn part1(input: &str) -> u64 {
    let input: Vec<Vec<u8>> = input
        .lines()
        .map(|line| {
            line.chars()
                .map(|x| x.to_digit(10).expect("not a number") as u8)
                .collect()
        })
        .collect();
    let mut jolt: u64 = 0;
    for line in &input {
        let mut max = 0;
        for (i, &num_i) in line.iter().enumerate() {
            for (j, &num_j) in line.iter().enumerate().skip(i + 1) {
                if i == j {
                    continue;
                }
                let n: u64 = (num_i.to_string() + &num_j.to_string())
                    .parse()
                    .expect("not a number");

                if n > max {
                    max = n;
                }
            }
        }
        jolt += max;
    }
    return jolt;
}

fn part2(input: &str) -> u64 {
    let input: Vec<Vec<u8>> = input
        .lines()
        .map(|line| {
            line.chars()
                .map(|x| x.to_digit(10).expect("not a number") as u8)
                .collect()
        })
        .collect();
    let mut jolt: u64 = 0;
    for line in &input {
        let mut max = 0;
        for (i, &num_i) in line.iter().enumerate() {
            for (j, &num_j) in line.iter().enumerate().skip(i + 1) {
                if i == j {
                    continue;
                }
                let n: u64 = (num_i.to_string() + &num_j.to_string())
                    .parse()
                    .expect("not a number");

                if n > max {
                    max = n;
                }
            }
        }
        jolt += max;
    }
    return jolt;
}

fn main() {
    let input = "987654321111111
811111111111119
234234234234278
818181911112111";

    println!("{}", part2(input));
}
