package Lab_Credit.Credits;

public class CreditEnterprice extends Credit implements OperationsBank{

    private double interest_rate;
    
    public CreditEnterprice(double interest_rate, double amount,int percentage_to_pay, int term){
        super(amount, percentage_to_pay, term);
        this.setInterest_rate(interest_rate);
    }

    public double getInterest_rate(){
        return this.interest_rate;
    }

    public void setInterest_rate(double interest_rate){
        this.interest_rate = interest_rate;
    }

    @Override
    public double calcInstallment() throws Exception{
        if (this.getTerm() <= 0 || this.getAmount() <= 0) {
            throw new IllegalArgumentException("Los datos deben ser mayor a 0");
        }
        double installment = 0;
        installment = (this.getAmount() + this.getInterest_rate() / this.getTerm());
        return installment;
    }
}
