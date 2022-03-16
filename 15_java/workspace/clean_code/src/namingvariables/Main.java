package namingvariables;

public class Main {

        public static void main(String[] args){

        char candidate = 'h';
        int count = 2;  
        
        GuessStatisticsMessage guessedStatistics = new GuessStatisticsMessage();
        
        System.out.println(guessedStatistics.make(candidate,count));
    }
}