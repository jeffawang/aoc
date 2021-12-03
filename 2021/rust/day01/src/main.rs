use std::fs;

fn main() {
    let s = fs::read_to_string("../../inputs/day01").expect("omg");
    let mut lines = s.lines();

    let mut ups: i32 = 0;
    let mut prev = lines.next().unwrap().parse().unwrap();
    for line in lines {
        let i: i32 = line.parse().unwrap();
        if i > prev {
            ups += 1;
        }
        prev = i;
    }
    println!("ups: {}", ups)
}
