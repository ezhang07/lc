class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();

        for (char c: s.toCharArray()) {
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else if (stack.isEmpty() || c != stack.pop()) {
                return false;
            }
        }

        return stack.isEmpty();


    }
}

/*
stack approach

opening brackets go onto stack
as soon as we see a closing bracket, check top of stack see if corresponding opening
if it isn't (different type of opening, empty): return false

*/