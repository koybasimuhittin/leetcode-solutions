impl Solution {
    pub fn count_segments(s: String) -> i32 {
        let mut cnt: i32 = 0;
        let mut flag = false;
        for c in s.chars(){
            if(c == ' ' && flag){
                flag = false;
            }
            else if(c != ' ' && !flag){
                flag = true;
                cnt += 1;
            }
        }
        return cnt;
    }
}