public class lab1 {
    public static void main(String[] args) {
        BankAccount ba = new BankAccount("Vaniusha", 10, "694201337");
        ba.deposit(100);
        ba.showBalance();
    }
}

class BankAccount {
    private float Balance;
    private String AccountNumber;
    private String OwnerName;
    private String OwnerPhoneNumber;

    public BankAccount(String _Name, float _Balance, String _AccountNumber) {
        this.Balance = _Balance;
        this.OwnerName = _Name;
        this.AccountNumber = _AccountNumber;
    }

    public void deposit(float amount) {
        float current = getBalance();
        setBalance(current + amount);
    }

    public void withdraw(float amount) {
        float current = getBalance();
        if (current >= amount) {
            setBalance(current - amount);
        }
        else System.out.println("Not enough funds");
    }

    public void showBalance(){
        System.out.println("Current balance: "+getBalance());
    }
    
    public void showOwnerName(){
        System.out.println("Owner name: "+getOwnerName());
    }


    public float getBalance() {
        return Balance;
    }

    public String getAccountNumber() {
        return AccountNumber;
    }

    public String getOwnerName() {
        return OwnerName;
    }

    public String getOwnerPhoneNumber() {
        return OwnerPhoneNumber;
    }

    public void setAccountNumber(String accountNumber) {
        AccountNumber = accountNumber;
    }

    public void setBalance(float balance) {
        Balance = balance;
    }

    public void setOwnerName(String ownerName) {
        OwnerName = ownerName;
    }

    public void setOwnerPhoneNumber(String ownerPhoneNumber) {
        OwnerPhoneNumber = ownerPhoneNumber;
    }
}