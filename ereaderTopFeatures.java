package topkfrequent;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.Collections;

class ereaderTopFeatures {
	public static ArrayList<String> popularNFeatures(
			int numFeatures, 
			int topFeatures, 
			List<String> possibleFeatures,
			int numFeatureRequests, 
			List<String> featureRequests) 
	{

		    ArrayList list = new ArrayList();
			Map<String, Integer> map = new HashMap<String, Integer>();
			for (String feature : possibleFeatures) {
				map.put(feature, 0);
			}
			
			for (int i = 0; i < featureRequests.size(); i++) {
				
				String input = featureRequests.get(i);
				String[] inputStr = input.split(" "); // TODO Research multiple delimiters, such as "-"
				
				for (int j = 0; j < inputStr.length; j++) {
					for (String feature : possibleFeatures) {
						if (feature.toLowerCase().contains(inputStr[j].toLowerCase())) {
							if (map.containsKey(inputStr[j])) {
								Integer count = map.get(inputStr[j]);
								map.put(inputStr[j], count + 1);
							} // if
						} // if
					} // for
				} // for
			} // for
			
			for (Map.Entry<String, Integer> e : map.entrySet()) {
				if (e.getValue() == Collections.max(map.values())) {
					list.add(e.getKey());
				}
			}
			return list;
	}	

	public static void main(String[] args) {
		int nf=6;  // numFeatures
		int tf=2;  // topFeatures
		int nfr=1; // numFeatureRequests
		
		// possibleFeatures
		List<String> possf = List.of( "storage", "battery", "hover", "alexa", "waterproof", "solar", "linux", "color");
		
		// featureRequests
		// TODO Need to match featureRequests to possibleFeatures case-insensitive
		List<String> featr = List.of( "I wish my ereader had even more storage",
				"I wish the battery life on my ereader lasted 2 years", "I read in the bath and would enjoy a waterproof ereader",
				"I want to take my ereader into the hover. Waterproof please waterproof!", "It would be neat if my ereader would hover on my desk when not in use",
				"How cool would it be if my ereader charged in the sun via solar power?", "I wish my ereader ran LINUX", "I wish my ereader had a color screen", 
				"When will it support Linux?", "I want more case color options!");
		
		ereaderTopFeatures pnf = new ereaderTopFeatures();
		
		System.out.println(pnf.popularNFeatures(nf,tf, possf, nfr, featr));}
} // class ereaderTopFeatures
