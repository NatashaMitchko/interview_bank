# Integer Replacement

Given an integer, replace all the `0` digits with `5`s.

## Examples

```
Input:  120
Output: 125

Input:  1
Output: 1

Input:  1001
Output: 1551
```

## Clarifying Questions

- Can the integer be negative? **Yes**
- Can the integeger have leading zeros? **Yes**
- What's the largest integer that can be passed to the function? **MAXINT**

## Solutions

### Stringify and Replace

Using language built-ins or functions from the standard library, the integer is converted to a string, all `"0"`s are replaced with `"5"`s. The adjusted string is converted back to an integer.

### Removing Digits and Rebuilding the Integer

The trick to this problem is to use the mod operator `%` to "pop" the last number and check for `0`'s until we've gone through the full number and then remember to reverse it at the end.

## Follow-Ups

- How would your solution have to change if we wanted to replace all the `5`s with `0`s? or `2`s with `1`s?