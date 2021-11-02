package aulapratica01;

public class Pessoa {
    //    Atributos da classe privados
//    mas publicos dos metods de get dos objetos instaciados atraves da classe

    private int codigo;
    private String nome;
    // Metodo construtor
    public Pessoa(int codigo, String nome){
        this.nome = nome;
        this.codigo = codigo;
    }
//    para acessar o atributo
    public String getNome(){
        return nome;
    }
    public int getCodigo(){
        return codigo;
    }
}
