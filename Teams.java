import java.util.Scanner;

public class Teams  {

    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        int choice;
    

        do {
            System.out.println("Select 1 for SC");
            System.out.println("Select 2 for Clemson");
            System.out.println("3 to exit");

            choice = input.nextInt();

            if (choice == 1)
            {
                scWin();
            }
            if (choice == 2)
            {
                clemWin();
            }
            if (choice == 3)
            {
                exit();
            }
        }
            while (choice != 3);
        }
        public static void scWin()
        {
            int sc = 0;
            int clem = 0;
            Scanner input = new Scanner(System.in);
            
            System.out.println("Enter SC score:");
            sc = input.nextInt();
            System.out.println("Enter Clemson score:");
            clem = input.nextInt();
            System.out.println("SC " + sc + " " + "Clemson " + clem);
        }
        public static void clemWin()
        {
            int clem = 0;
            int sc = 0;
            Scanner input = new Scanner(System.in);
            
            System.out.println("Enter Clemson score:");
            clem = input.nextInt();
            System.out.println("Enter SC score:");
            sc = input.nextInt();
            System.out.println("Clemson " + clem + " " + "SC " + sc);
        }
        public static void exit()
        {
            System.out.println("See you next time!");
        }
    }
