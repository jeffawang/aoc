use std::collections::HashSet;
use std::fs;

fn fold(dots: HashSet<[i32; 2]>, axis: usize, coord: i32) -> HashSet<[i32; 2]> {
    dots.iter()
        .map(|t| match (t[axis] > coord, axis) {
            (true, 0) => [coord - (t[0] - coord), t[1]],
            (true, 1) => [t[0], coord - (t[1] - coord)],
            _ => *t,
        })
        .collect()
}

fn parse_dot(input: &str) -> [i32; 2] {
    let s: Vec<&str> = input.split(",").collect();
    [s[0].parse().unwrap(), s[1].parse().unwrap()]
}

fn parse_fold(input: &str) -> (usize, i32) {
    let s: Vec<&str> = input
        .split_whitespace()
        .collect::<Vec<&str>>()
        .last()
        .unwrap()
        .split("=")
        .collect();
    (if s[0] == "x" { 0 } else { 1 }, s[1].parse().unwrap())
}

fn main() {
    let f = fs::read_to_string("../../inputs/day13").expect("failed to read file");
    let mut dots: HashSet<[i32; 2]> = f
        .lines()
        .filter(|i| i.contains(","))
        .map(parse_dot)
        .collect();
    let folds: Vec<(usize, i32)> = f
        .lines()
        .filter(|i| i.contains("fold"))
        .map(parse_fold)
        .collect();

    for i in 0..folds.len() {
        let f = folds[i];
        dots = fold(dots, f.0, f.1);
        if i == 0 {
            println!("Part 1: {}", dots.len())
        }
    }
    println!("Part 2:");
    print_dots(&dots);
}

fn print_dots(d: &HashSet<[i32; 2]>) {
    let max_x = d.iter().map(|d| d[0]).max().unwrap();
    let max_y = d.iter().map(|d| d[1]).max().unwrap();
    for j in 0..=max_y {
        for i in 0..=max_x {
            print!("{}", if d.contains(&[i, j]) { "##" } else { "  " });
        }
        println!("");
    }
}
