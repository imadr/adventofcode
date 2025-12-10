fn part1(input: &str) -> u64 {
    let mut password = 0;
    for range in input.split(",") {
        let range_vec = range.split("-").collect::<Vec<&str>>();
        let first: u64 = range_vec[0].parse().expect("invalid int");
        let second: u64 = range_vec[1].parse().expect("invalid int");

        for i_ in first..=second {
            let i = i_.to_string();
            let half_len = i.len() / 2;
            for chunk_size in 1..=half_len {
                if i.len().rem_euclid(chunk_size) == 0 {
                    let chunks: Vec<String> = i
                        .chars()
                        .collect::<Vec<char>>()
                        .chunks(chunk_size)
                        .map(|slice| slice.iter().collect::<String>())
                        .collect();

                    if chunks.iter().skip(1).all(|x| x == &chunks[0]) {
                        password += i_;
                        break;
                    }
                }
            }
        }
    }

    return password;
}

fn main() {
    let input = "10327-17387,74025-113072,79725385-79874177,964628-1052240,148-297,3-16,126979-227778,1601-2998,784-1207,831289-917268,55603410-55624466,317-692,602197-750430,17-32,38-58,362012-455626,3622441-3647505,883848601-883920224,62-105,766880-804855,9184965756-9185005415,490073-570277,2929273115-2929318135,23251-48475,9696863768-9697013088,229453-357173,29283366-29304416,4526-8370,3095-4389,4400617-4493438";

    println!("{}", part1(input))
}
