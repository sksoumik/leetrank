// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

// You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

// Evaluate the expression. Return an integer that represents the value of the expression.

//  Note that:

// The valid operators are '+', '-', '*', and '/'.
// Each operand may be an integer or another expression.
// The division between two integers always truncates toward zero.
// There will not be any division by zero.
// The input represents a valid arithmetic expression in a reverse polish notation.
// The answer and all the intermediate calculations can be represented in a 32-bit integer.  

struct Solution;

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();

        for token in &tokens {
            match token.as_str() {
                "+" | "-" | "*" | "/" => {
                    let operand2 = stack.pop().unwrap();
                    let operand1 = stack.pop().unwrap();
                    let result = match token.as_str() {
                        "+" => operand1 + operand2,
                        "-" => operand1 - operand2,
                        "*" => operand1 * operand2,
                        "/" => operand1 / operand2,
                        _ => unreachable!(),
                    };
                    stack.push(result);
                }
                _ => stack.push(token.parse().unwrap()),
            }
        }

        stack.pop().unwrap()
    }
}


fn main() {
    // Test cases
    let tokens1 = vec!["2".to_string(), "1".to_string(), "+".to_string(), "3".to_string(), "*".to_string()];
    let tokens2 = vec!["4".to_string(), "13".to_string(), "5".to_string(), "/".to_string(), "+".to_string()];
    let tokens3 = vec![
        "10".to_string(), "6".to_string(), "9".to_string(), "3".to_string(), "+".to_string(), "-11".to_string(),
        "*".to_string(), "/".to_string(), "*".to_string(), "17".to_string(), "+".to_string(), "5".to_string(), "+".to_string(),
    ];

    assert_eq!(Solution::eval_rpn(tokens1), 9);
    assert_eq!(Solution::eval_rpn(tokens2), 6);
    assert_eq!(Solution::eval_rpn(tokens3), 22);

    println!("All test cases passed!");
}

