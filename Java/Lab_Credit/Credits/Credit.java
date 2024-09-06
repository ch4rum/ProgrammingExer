package Lab_Credit.Credits;

public class Credit {
    private double amount, percentage_to_pay;
    private int term;

    public Credit(double amount, double percentage_to_pay, int term) {
        this.setAmount(amount);
        this.setPercentage_to_pay(percentage_to_pay);
        this.setTerm(term);
    }
    
    public double getAmount(){
        return this.amount;
    }

    public void setAmount(Double amount){
        this.amount = amount;
    }

    public double getPercentage_to_pay(){
        return this.percentage_to_pay;
    }

    public void setPercentage_to_pay(double percentage_to_pay){
        this.percentage_to_pay = percentage_to_pay;
    }

    public int getTerm(){
        return this.term;
    }

    public void setTerm(int term){
        this.term = term;
    }
}
