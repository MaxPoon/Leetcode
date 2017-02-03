/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
public class Solution {
	public int maxPoints(Point[] points) {
		if(points.length==0) return 0;
		if(points.length==1) return 1;
		int result = 1;
		for(int i=0; i<points.length-1; i++){
			HashMap<Double, Integer> map=new HashMap<Double, Integer>();
			int same=0, vline=0, currentMax = 0;
			for(int j=i+1;j<points.length; j++){
				if(points[i].x==points[j].x){
					if(points[i].y==points[j].y) same++;
					else{
						vline++;
					}
					continue;
				}
				double slope = (double)(points[j].y-points[i].y)/(double)(points[j].x-points[i].x);
				if(slope==-0.0) slope=0.0;
				System.out.println(slope);
				if(map.containsKey(slope)) map.put(slope, map.get(slope)+1);
				else map.put(slope, 1);
				currentMax = Math.max(map.get(slope), currentMax);
			}
			result = Math.max(result, currentMax+same+1);
			result = Math.max(result, vline+same+1);
		}
		return result;
	}
}