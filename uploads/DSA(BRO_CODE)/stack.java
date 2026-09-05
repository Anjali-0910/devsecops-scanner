import java.util.Stack;

public class stack{

    public static void main(String[] args){

        Stack<String> stack=new Stack<String>();
        
        stack.push("Bibha");
        stack.push("Anni");
        //System.out.println(stack.isEmpty());

       // System.out.println(stack.peek());
        System.out.println(stack.pop("Anni"));
    }
    
}