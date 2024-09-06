package Lab_Credit.Credits;

public class CreditPersonal extends Credit implements OperationsBank{
    
    public CreditPersonal(double amount, double percentage_to_pay, int term){
        super(amount, percentage_to_pay, term);
    }

    @Override
    public double calcInstallment() throws Exception{
        if (this.getTerm() <= 0 || this.getAmount() <= 0) {
            throw new IllegalArgumentException("Los datos deben ser mayor a 0");
        }
        double installment = 0;
        installment = (this.getAmount() + this.getAmount() * (this.getPercentage_to_pay() / 100))/this.getTerm();
        return installment;
    }
}
