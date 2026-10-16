class Solution {
    public boolean isAnagram(String s, String t) {
      if (s == null || t == null || s.length() != t.length()) {
        return false;
      }

      Map<Character, Integer> sFrequencyMap = new HashMap<>();
      Map<Character, Integer> tFrequencyMap = new HashMap<>();
      
      for (char c: s.toCharArray()) {
        sFrequencyMap.put(c, sFrequencyMap.getOrDefault(c, 0) + 1);
      }

      for (char c: t.toCharArray()) {
        tFrequencyMap.put(c, tFrequencyMap.getOrDefault(c, 0) + 1);
      }

      return sFrequencyMap.equals(tFrequencyMap);

    }
}
