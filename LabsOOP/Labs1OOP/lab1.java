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
    private boolean CanTransfer;

    public BankAccount(String _Name, float _Balance, String _AccountNumber) {
        this.Balance = _Balance;
        this.OwnerName = _Name;
        this.AccountNumber = _AccountNumber;
    }

    public void transferFunds(BankAccount reciever, float amount) {
        float current = getBalance();
        if (current >= amount && reciever.getCanTransfer()) {
            reciever.deposit(amount);
            this.withdraw(amount);
        }
        else if(current<amount){
            System.err.println("Not enough funds.");
        }
        else if(!reciever.getCanTransfer()){
            System.err.println("Reciever cannot recieve transfers.");
        }
    }

    public void deposit(float amount) {
        float current = getBalance();
        setBalance(current + amount);
    }

    public void withdraw(float amount) {
        float current = getBalance();
        if (current >= amount) {
            setBalance(current - amount);
        } else
            System.out.println("Not enough funds");
    }

    public void showBalance() {
        System.out.println("Current balance: " + getBalance());
    }

    public void showOwnerName() {
        System.out.println("Owner name: " + getOwnerName());
    }

    public float getBalance() {
        return this.Balance;
    }

    public String getAccountNumber() {
        return this.AccountNumber;
    }

    public String getOwnerName() {
        return this.OwnerName;
    }

    public String getOwnerPhoneNumber() {
        return this.OwnerPhoneNumber;
    }

    public void setAccountNumber(String accountNumber) {
        this.AccountNumber = accountNumber;
    }

    public void setBalance(float balance) {
        this.Balance = balance;
    }

    public void setOwnerName(String ownerName) {
        this.OwnerName = ownerName;
    }

    public void setCanTransfer(boolean canTransfer) {
        this.CanTransfer = canTransfer;
    }

    public boolean getCanTransfer() {
        return this.CanTransfer;
    }

    public void setOwnerPhoneNumber(String ownerPhoneNumber) {
        this.OwnerPhoneNumber = ownerPhoneNumber;
    }
}