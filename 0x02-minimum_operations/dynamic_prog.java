import java.util.HashMap;

class Source {

    public static int fib_rec(int n){
        if(n == 0 || n == 1) return n;
        return fib_rec(n-1) + fib_rec(n-2);
    }

    public static int fib(int n){
        return fib(n, new HashMap<Integer, Integer>());
    }
    public static int fib(int n, HashMap<Integer, Integer> memo){
        if(n == 0 || n == 1) return n;
        if(memo.containsKey(n)) return memo.get(n);
        memo.put(n, fib(n-1, memo) + fib(n-2, memo));
        return memo.get(n);
    }

    public static void main(String[] args) {
        int memoMethod = fib(10);
        int recMethod = fib_rec(10);
        System.out.println("Memoization method: " + memoMethod);
        System.out.println("Recursive method: " + recMethod);
        assert memoMethod == recMethod: "Memoization method and recursive method should return the same result";
    }
}
