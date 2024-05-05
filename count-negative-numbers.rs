impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;
        for row in grid {
            for num in row {
                if(num < 0){
                    ans += 1;
                }
            }
        }

        return ans;
    }
}