use std::{collections::HashMap, fs, hash::Hash};

type position = (usize, usize);

fn charMap(current: position, direction: &str, amount: usize) -> position {
    match direction {
        "forward" => (current.0 + amount, current.1),
        "down" => (current.0, current.1 + amount),
        "up" => (current.0, current.1 - amount),
        _ => current,
    }
}

fn main() {
    let f = fs::read_to_string("../../inputs/day02").expect("oops");
    let mut p: position = (0, 0);
    for line in f.lines() {
        let mut x = line.split_whitespace();
        let direction = x.next().unwrap();
        let amount: usize = x.next().unwrap().parse().unwrap();
        p = charMap(p, direction, amount);
    }
    println!("{}", p.0 * p.1)
}
