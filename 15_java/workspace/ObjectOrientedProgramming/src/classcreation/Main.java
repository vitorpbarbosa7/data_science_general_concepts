package classcreation;
import static java.lang.System.*;

public class Main {
    
    public static void main(String[] args) { 

    String macbookAliasName = "Macbook Air M1";
    int macbookYear = 2020;
    Computer macbook = new Computer(macbookAliasName, macbookYear);

    String asusRogAliasName = "AsusRog";
    int asusRogYear = 2019;
    Computer asusRog = new Computer(asusRogAliasName, asusRogYear);
    
    macbook.boot();
    out.println(macbook.getYear());
    macbook.setAge(2021);
    out.println(macbook.getYear());

    asusRog.boot();
    out.println(asusRog.getYear());
    asusRog.setAge(2022);
    out.println(asusRog.getYear());
    }
}
