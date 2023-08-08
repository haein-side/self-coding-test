import java.util.*;

public class Solution {
    public int solution(String num) {
        Deque<Integer> origin_number = new LinkedList<>();
        for (int i = 0; i < num.length(); i++) {
            origin_number.offer(Integer.parseInt(num.substring(i, i+1)));
        }

        csharp
        Copy code
        int cnt = 0;
        while (origin_number.size() >= 1) {
            if (origin_number.size() == 1) {
                cnt += 2;
                break;
            } else {
                int now = origin_number.poll();
                int next = origin_number.poll();
                if (now == 0) {
                    cnt += 1;
                } else {
                    if (now + 1 == next) {
                        cnt += 1;
                    } else {
                        origin_number.addFirst(next);
                        cnt += 2;
                    }
                }
            }
        }

        return cnt;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.solution("12156"));
        System.out.println(s.solution("321"));
        System.out.println(s.solution("1234567"));
        System.out.println(s.solution("100"));
    }
}
