import java.util.Deque;
import java.util.ArrayDeque;

public class Solution {
    public static int solution(String num) {
        Deque<Integer> originNumber = new ArrayDeque<>();
        for (int i = 0; i < num.length(); i++) {
            originNumber.add(Integer.parseInt(num.substring(i, i + 1)));
        }

        int cnt = 0;
        while (originNumber.size() >= 1) {
            if (originNumber.size() == 1) {
                cnt += 2;
                break;
            } else {
                int now = originNumber.pollFirst();
                int next = originNumber.pollFirst();
                if (now == 0) {
                    cnt += 1;
                } else {
                    if (now + 1 == next) {
                        cnt += 1;
                    } else {
                        originNumber.addFirst(next);
                        cnt += 2;
                    }
                }
            }
        }
        System.out.println(originNumber);

        return cnt;
    }

    public static void main(String[] args) {
        System.out.println(solution("12156"));
        System.out.println(solution("321"));
        System.out.println(solution("1234567"));
        System.out.println(solution("100"));
    }
}
