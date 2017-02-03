class Solution {
public:
	int maxPoints(vector<Point> &points) {
		int maxPts = 0;
		for(int i=0; i<points.size(); i++) {
			int nMax = 0, nSame = 0, nInf = 0;
			unordered_map<float,int> comSlopes;
			
			for(int j=i+1; j<points.size(); j++) {
				if(points[j].x==points[i].x) {
					if(points[j].y==points[i].y)
						nSame++;
					else
						nInf++;
					continue;
				}
				float slope = (float)(points[j].y-points[i].y)/(float)(points[j].x-points[i].x);
				comSlopes[slope]++;
				nMax = max(nMax, comSlopes[slope]);
			}
			
			nMax = max(nMax, nInf)+nSame+1;
			maxPts = max(maxPts,nMax);
		}
		return maxPts;
	}
};