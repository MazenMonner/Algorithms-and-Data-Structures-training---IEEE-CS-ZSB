
public class Main
{
	public static void main(String[] args) {
		scanner in = new scanner (System.in);
		int a [][] = new int [5][5];
		int c = 0;
		for (int i = 0 ; i<5;i++)
		{
		    for (int j = 0; j<5 ;j++ )
		    {
		        a[i][j]=in.nextint();
		        if(a[i][j]==1)
		        {
		            c+=Math.abs(i-2)+Math.abs[j-2];
		            break; 
		        }
		    }
		}
		System.out.println(c);
	}
}
