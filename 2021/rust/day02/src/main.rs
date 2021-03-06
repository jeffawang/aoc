use std::fs;

fn part1(input: &str) -> usize {
    let mut x = 0;
    let mut z = 0;
    for line in input.lines() {
        let tokens: Vec<&str> = line.split(" ").collect();
        let i = tokens[1].parse::<usize>().unwrap();
        match tokens[0] {
            "forward" => x += i,
            "down" => z += i,
            "up" => z -= i,
            _ => {}
        }
    }
    x * z
}

fn part2(input: &str) -> usize {
    let mut x = 0;
    let mut z = 0;
    let mut aim = 0;
    for line in input.lines() {
        let tokens: Vec<&str> = line.split(" ").collect();
        let i: usize = tokens[1].parse::<usize>().unwrap();
        match tokens[0] {
            "forward" => {
                x += i;
                z += aim * i;
            }
            "down" => aim += i,
            "up" => aim -= i,
            _ => {}
        }
    }
    x * z
}

fn main() {
    let f = fs::read_to_string("../../inputs/day02").expect("oops");
    println!("Part 1: {}", part1(f.as_str()));
    println!("Part 2: {}", part2(f.as_str()));
}
