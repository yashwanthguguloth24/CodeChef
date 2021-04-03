import java.util.*;
import java.lang.*;
import java.io.*;

class Test3
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s1 = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s1[0]);
            int k = Integer.parseInt(s1[1]);
            String str = br.readLine();
            int ans=0;
            for(int i=0;i<n;i++)
            {
                if(str.charAt(i)=='*')
                {
                    int j=i+1;
                    int len=1;
                    while(j<n && str.charAt(j)=='*')
                    {
                        len++;
                        j++;
                    }
                    i=j;
                    ans=Math.max(ans, len);
                }
            }      
            System.out.println(ans>=k?"YES":"NO");
        }
    }
}
