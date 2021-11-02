package aulapratica01;

public class PessoaApp {
//    public: access anywhere
//    static: can be executed without the need to call it
//    does not return any type
//    main: name
//    String: All code we give to JVM is a string
//    args :name of the string array
    public static void main(String[] args){
        Pessoa pessoa01 = new Pessoa(1, "Vitor");
        Pessoa pessoa02 = new Pessoa(1, "Gabriela");

//        Print
        System.out.println("O nome do objeto pessoa01 eh"+pessoa01.getNome());
        System.out.println("O codigo do objeto pessoa01 eh"+pessoa01.getCodigo());
    }
}
