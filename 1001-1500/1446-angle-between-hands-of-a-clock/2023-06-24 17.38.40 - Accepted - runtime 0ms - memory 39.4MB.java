class Solution {
    public double angleClock(int hour, int minutes) {
        return Math.min(Math.abs((hour % 12) * 30 - minutes * 5.5), 360 - Math.abs((hour % 12) * 30 - minutes * 5.5));
        // min(abs((hour%12)*30-minutes*5.5),360-abs((hour%12)*30-minutes*5.5));
    }
}