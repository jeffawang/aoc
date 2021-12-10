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

fn main() {
    let f = fs::read_to_string("../../inputs/day02").expect("oops");
    let p1 = part1(f.as_str());
    println!("Part 1: {}", p1)
}
