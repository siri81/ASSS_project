// insecure_deserialization.java
import java.io.*;

public class InsecureDeserialization {
    public static void main(String[] args) {
        try {
            ObjectInputStream in = new ObjectInputStream(new FileInputStream("data.ser"));
            Object obj = in.readObject(); // Potentially malicious object
            System.out.println("Object read: " + obj);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
