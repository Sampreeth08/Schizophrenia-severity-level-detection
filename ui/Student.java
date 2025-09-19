package javatraining;

public class Student {

    private String name;
    private int roll;
    private double cgpa;

    public Student(String name, int roll, double cgpa) {
        this.name = name;
        this.roll = roll;
        this.cgpa = cgpa;
    }

    public void displayProfile() {
        System.out.println(roll + "" + name + "" + cgpa);
    }

    public void findPercentage() {
        System.out.println("percentage of s1 is " + (cgpa * 10));

    }

    public static void main(String args[]) {
        Student s1 = new Student("karan", 1056, 8.8);
        s1.displayProfile();
        s1.findPercentage();
    }
}