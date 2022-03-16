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

    String acerAspireAliasName = "Acer Aspire";
    int acerAspireYear = 2022;
    int batteryAcerAspire = 80;

    Notebook acerAspire = new Notebook(acerAspireAliasName, 
                                        acerAspireYear, 
                                        batteryAcerAspire);

    acerAspire.discharge();
    acerAspire.boot();
    out.println(acerAspire.getYear());
    acerAspire.setAge(2025);
    out.println(acerAspire.getYear());
    
    macbook.boot();
    out.println(macbook.getYear());
    macbook.setAge(2030);
    out.println(macbook.getYear());

    asusRog.boot();
    out.println(asusRog.getYear());
    asusRog.setAge(2030);
    out.println(asusRog.getYear());
    }
}
