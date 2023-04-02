function digitSum(n: number): number {
  let answer = 0;
  while (n > 0) {
    answer += n % 10;
    n = Math.floor(n / 10);
  }
  return answer;
}

function countLargestGroup(n: number): number {
  let maxSize = 0;
  let ans = 0;

  const groups: number[] = [];
  for (let i = 0; i <= 9 * 4; i++) {
    groups.push(0);
  }

  for (let i = 1; i <= n; i++) {
    groups[digitSum(i)] += 1;
    maxSize = maxSize > groups[digitSum(i)] ? maxSize : groups[digitSum(i)];
  }

  for (let i = 0; i <= 9 * 4; i++) {
    ans += groups[i] == maxSize ? 1 : 0;
  }

  return ans;
}
