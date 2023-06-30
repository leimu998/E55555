
public class Solution
{
    static string[] board = { "abcde", "fghij", "klmno", "pqrst", "uvwxy", "z" };
    static (int, int)[] dirs = { (1, 0), (-1, 0), (0, -1), (0, 1) };
    public string AlphabetBoardPath(string target)
    {
        int n = board.Length;
        Queue<(int, int, string)> q = new();
        q.Enqueue((0, 0, ""));
        int i = 0;
        while (q.Count > 0)
        {
            var cur = q.Dequeue();
            if (board[cur.Item1][cur.Item2] == target[i])
            {
                while (i<target.Length&&board[cur.Item1][cur.Item2] == target[i])
                {
                    cur.Item3 += "!";
                    i++;
                }

                if (i == target.Length)
                {
                    return cur.Item3;
                }
                q.Clear();
            }
            for (int j = 0; j < dirs.Length; j++)
            {
                int nx = cur.Item1 + dirs[j].Item1;
                int ny = cur.Item2 + dirs[j].Item2;
                if (nx >= n || nx < 0 || 0 > ny || ny >= board[nx].Length) continue;
                q.Enqueue((nx, ny, cur.Item3 + GetDirString(j)));
            }
        }
        return "";
    }
    private string GetDirString(int x)
    {
        switch (x)
        {
            case 0:
                 return "D";
            case 1:
                return "U";
            case 2:
                return "L";
            case 3:
                return "R";
        }
        return "";
    }
}
