package Lab_Credit;

import java.util.InputMismatchException;
import java.util.Scanner;

import Lab_Credit.Credits.*;

public class MenuBank extends WriteOutput {

    private Output output;
    private Scanner data;
    private double amount, percentage_to_pay,interest_rate, termDouble;
    private int term;

    public MenuBank(){
        output = new Output();
        data = new Scanner(System.in);
    }

    public void menu(){
        int Option = 0;
        do{
            try {
                output.clear();
                this.printDebug(" ", this.getGREEN() + "\n\t.: MENU :.\n"+ this.getRESET() 
                + this.getBLUE() + "\n1)" + this.getRESET() + " Credito Personal."
                + this.getBLUE() + "\n2)" + this.getRESET() + " Credito Empresarial."
                + this.getBLUE() + "\n3)" + this.getRESET() + " Credito Especial."
                + this.getBLUE() + "\n4)" + this.getRESET() + " exit.\n");
                this.printDebug("OK", "Opcion :> ","");
                Option = data.nextInt();
                this.handler_options(Option);
            } catch (InputMismatchException n){
                this.printDebug("ERROR","Ingrese un numero entero valido.");
                data.next();
                output.sleep(1500);
            }
        } while (Option != 4);
        data.close();
    }

    private void handler_options(int number){
        switch (number) {
            case 1:
                output.clear();
                this.printDebug(" ", this.getGREEN() + "\t.: CREDITO PERSONAL :.\n" + this.getRESET());
                amount = this.inputDataNumbers("Monto: $");
                percentage_to_pay = this.inputDataNumbers("Porcentage de interes: ");
                termDouble = this.inputDataNumbers("Plazo: ");
                term = (int) termDouble;
                CreditPersonal creditPersonal = new CreditPersonal(amount, percentage_to_pay, term);
                try {
                    double installmentValue = creditPersonal.calcInstallment();
                    this.printDebug("OK","Valor Cuota: $" + String.format("%.3f", installmentValue));
                } catch (Exception e){
                    this.printDebug("FAILED","Fallo al calcular la cuota; " + e.getMessage());
                }
                data.nextLine();
                this.printDebug(" ",this.getGREEN() + "\nPresiona <ENTER> para continuar" + this.getRESET());
                data.nextLine();
                break;
            case 2:
                output.clear();
                this.printDebug(" ", this.getGREEN() + "\t.: CREDITO EMPRESARIAL :.\n" + this.getRESET());
                amount = this.inputDataNumbers("Monto: $");
                interest_rate = this.inputDataNumbers("Valor de interes negociado: ");
                termDouble = this.inputDataNumbers("Plazo: ");
                term = (int) termDouble;
                CreditEnterprice enterprice = new CreditEnterprice(interest_rate, amount, 0, term); 
                try {
                    double installmentValue = enterprice.calcInstallment();
                    this.printDebug("OK","Valor Cuota: $" + String.format("%.3f", installmentValue));
                } catch (Exception e){
                    this.printDebug("FAILED","Fallo al calcular la cuota; " + e.getMessage());
                }
                data.nextLine();
                this.printDebug(" ",this.getGREEN() + "\nPresiona <ENTER> para continuar" + this.getRESET());
                data.nextLine();
                break;
            case 3:
                output.clear();
                this.printDebug(" ", this.getGREEN() + "\t.: CREDITO ESPECIAL :.\n"+ this.getRESET() );
                amount = this.inputDataNumbers("Monto: $");
                termDouble = this.inputDataNumbers("Plazo: ");
                term = (int) termDouble;
                CreditSpecial special = new CreditSpecial(amount, 0, term); 
                try{
                    double installmentValue = special.calcInstallment();
                    this.printDebug("OK", "Valor Cuota: $" + String.format("%.3f", installmentValue));
                } catch (Exception e){
                    this.printDebug("FAILED", "Fallo al calcular la cuota; " + e.getMessage());
                }
                data.nextLine();
                this.printDebug(" ",this.getGREEN() + "\nPresiona <ENTER> para continuar" + this.getRESET());
                data.nextLine();
                break;
            case 4:
                this.printDebug(" ", "\n...Saliendo del programa...\n");
                data.close();
                break;
            default:
                this.printDebug("WARNING", "Seleccione una opción correcta.");
                output.sleep(1500);
                break;
        }
    }

    private Double inputDataNumbers(String message) {
        while (true) {
            try{
                this.printDebug("OK",message, "");
                return data.nextDouble();
            } catch (InputMismatchException n){
                this.printDebug("ERROR","Ingrese un numero double valido.");
                data.next();
                output.sleep(1000);
            }
        }
    }
}