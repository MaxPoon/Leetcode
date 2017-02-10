import java.util.*;

public class Solution {
	public List<List<String>> groupAnagrams(String[] strs) {
		List<List<String>> result = new LinkedList<List<String>>();
		HashMap<String, List> map = new HashMap<String, List>();
		for(String str: strs){
			char[] chars = str.toCharArray();
			Arrays.sort(chars);
			String sorted = new String(chars);
			if(map.containsKey(sorted)){
				map.get(sorted).add(str);
			}else{
				List<String> list = new LinkedList<String>();
				list.add(str);
				map.put(sorted, list);
			}
		}
		for(String key: map.keySet()){
			result.add(map.get(key));
		}
		return result;
	}
}