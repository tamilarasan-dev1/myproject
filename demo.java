public final class Demo {
    private static final int ITERATION_COUNT = 10;

    private Demo() {
        // Prevent instantiation of this utility class.
    }

    public static void main(String[] args) {
        for (int i = 0; i < ITERATION_COUNT; i++) {
            System.out.println("Iteration: " + i);
        }
    }
}
