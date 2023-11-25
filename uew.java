package mt;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        char[] s = str.toCharArray();
        // 遍历子串的长度
        int length = str.length();
        int sum = 0;
        int[][] dp = new int[s.length + 1][2];
        for (int i = 2; i <= length; i++) {
            int beginIndex = 0;
            int endIndex = beginIndex + i - 1;
            while (endIndex < length) {
                sum += getValue(dp,s, beginIndex, endIndex);
                beginIndex++;
                endIndex = beginIndex + i - 1;
            }
        }
        System.out.println(sum);
    }
    public static int getValue(int[][] dp,char[] s, int beginIndex, int endIndex) {
        // 1. 定义状态:当前评估哪一位的数字?
        // 2. 定义选择:是否将当前这一位元素变为0或者变为1
        // dp数组含义:表示对于[beginIndex,i]的这几位元素,如果最后一位是[0]/[1]时的最小权值
        // base-case:对于前0个字符,无论怎么处理权值都时0
        int n = endIndex;
        dp[beginIndex][0] = 0;dp[beginIndex][1] = 0;
        for (int i = beginIndex+1; i <= n+1; i++) {
            // 选择:是否将当前字符变为0/1
            if (s[i - 1] == '0') {
                // 保持原状和前面为1的情况组成一堆
                dp[i][0] = dp[i - 1][1];
                // 主动改变自己
                dp[i][1] = dp[i - 1][0] + 1;
            } else if (s[i - 1] == '1') {
                // 保持原状和前面为0组成一对
                dp[i][1] = dp[i - 1][0];
                // 主动改变自己
                dp[i][0] = dp[i - 1][1] + 1;
            }
        }
        return Math.min(dp[n+1][0], dp[n+1][1]);
    }

}
