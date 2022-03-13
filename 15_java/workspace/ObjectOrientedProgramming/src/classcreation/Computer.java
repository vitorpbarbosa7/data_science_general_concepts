package classcreation;
import static java.lang.System.*;

public class Computer {

    private String aliasName;
    private int year;
    // public String name;
    // public String processor;

    // Constructor (__init__ in python?)
    public Computer(String aliasName, int year) {
        this.aliasName = aliasName;
        this.year = year;
    }

    public void boot() {
        out.println("Booting the " + this.aliasName + " from the year of " + 
        this.year + "\n");
    }

    // getter in python ?
    public int getYear() {
        return this.year;
    }

    // setter
    public void setAge(int year) {
        this.year = year;
    }
}