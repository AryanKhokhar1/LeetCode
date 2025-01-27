class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        int n = s.length();
        int[] shiftArray = new int[n + 1]; // To handle shifts easily using prefix sum

        // Accumulate the shifts
        for (int[] shift : shifts) {
            int start = shift[0];
            int end = shift[1];
            int direction = shift[2] == 1 ? 1 : -1;
            shiftArray[start] += direction;
            shiftArray[end + 1] -= direction;
        }

        // Compute the prefix sum to get net shifts at each index
        int netShift = 0;
        StringBuilder result = new StringBuilder(s);
        for (int i = 0; i < n; i++) {
            netShift += shiftArray[i];
            int originalChar = s.charAt(i) - 'a'; // Convert char to 0-25 range
            int newChar = (originalChar + netShift) % 26;
            if (newChar < 0) newChar += 26; // Handle negative shifts
            result.setCharAt(i, (char) ('a' + newChar)); // Convert back to char
        }

        return result.toString();
    }
}
