import java.util.Scanner;

class Details {
    String name;
    String phone;
    String votersid;

    public Details(String n,String p, String v){
        name = n;
        phone = p;
        votersid = v;
    }
}

public class exam {

    Details[] dets;
    int count; //Stored number of elements in array

    public exam(){
        dets = new Details[100];
        count = 0;
    }

    public static void main(String args[]) throws Exception{
        //System.setIn(new FileInputStream("input.txt"));
        exam e = new exam();
        e.start();
    }

    public void start(){
       
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements to be inserted : ");
        int no_elements = Integer.parseInt(sc.nextLine());
        for(int i = 0; i < no_elements; i++){
            System.out.println("Enter Name : ");
            String n = sc.nextLine();
            System.out.println("Enter Phone Number : ");
            String p = sc.nextLine();
            System.out.println("Enter Voters Id Number : ");
            String v = sc.nextLine();
            Details de = new Details(n, p, v);
            insert(de);
        }

        System.out.println("Enter name to be searched for : ");
        String name = sc.nextLine();
        System.out.println("Enter phone number to be searched for : ");
        String ph = sc.nextLine();

        String result = binary_search(name, ph);
        if(result == null) {
            System.out.println("Not Found");
        }
        else {
            System.out.println(result);
        }
    }   

    public void insert(Details d) {

        if(count == 0){
            dets[0] = d;
            ++count;
            return;
        }

        for(int i = 0; i < count; i++) {
            if(d.name.compareTo(dets[i].name) > 0){
                continue;
            }
            else {
                for(int j = count-1; j >=i ; j--){
                    dets[j+1] = dets[j];
                }
                dets[i] = d;
                ++count;
                return;
            }
        }
        dets[count] = d;
        ++count;
    }

    public String binary_search(String name, String ph){
        if(count == 0) {
            return null;
        }

        int low = 0;
        int high = count;

        while(low <= high) {
            int m = low + (high - low) / 2;
            if(dets[m].name.compareTo(name) == 0) {
                if(dets[m].phone.compareTo(ph) == 0) {
                    return dets[m].votersid;
                }
            }

            if(dets[m].name.compareTo(name) < 0) {
                low = m+1;
            }
            else {
                high = m-1;
            }

        }

        return null;
    }
}



