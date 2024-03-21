import java.util.function.BiFunction;

public class App {
    public static void main(String[] args) throws Exception {
        
        BiFunction<Double, Double, Double> product = (a, b) -> {
            System.out.println(a * b);
            return a * b;
        };
        product.apply(15.0, 13.0);
        

    }
}
