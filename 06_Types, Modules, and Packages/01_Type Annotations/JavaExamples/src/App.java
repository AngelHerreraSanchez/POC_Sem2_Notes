public class App {
    public static void main(String[] args) throws Exception {

        int number1 = 5;
        int number2 = 3;
        System.out.println(min(number1, number2));
        number2 = "String";

    }

    private static int min(int a, int b) {
        if (a < b) {
            return a;
        } else {
            return b;
        }
    }

    private static void printMin(int a, int b) {
        if (a < b) {
            System.out.println(a);
        } else {
            System.out.println(b);
        }
    }
}
