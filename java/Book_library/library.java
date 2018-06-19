class Library {
    // Add the missing implementation to this class 
	String address;
	Book[] books = new Book[5];
	int i = 0;
	int found = 0;
	Library(String addr){
		address = addr;	
	}
	
	public void addBook(Book name){
		if (i == 0) {
			books[i] = name;
			// System.out.println(books[i].title+"i" + i);
			i = i + 1;
		} else {
			books[i] = name;
			// System.out.println(books[i].title+"i" + i);
			i = i + 1;
		}	
	}
	
	public static void printOpeningHours(){
		System.out.println("Libraries are open daily from 9am to 5pm.");
	}
	
	public void printAddress(){
		System.out.println(address);
	}
	
	public void borrowBook(String booktitle){
		for (int j = 0; j < i; j++) {

			if (books[j].title.equals(booktitle) && books[j].borrowed == false) {
				System.out.println("You successfully borrowed "
						+ books[j].title);
				books[j].borrowed();
				found = 1;
				break;
			} else if (books[j].title.equals(booktitle)
					&& books[j].borrowed == true) {
				System.out.println("Sorry, this book is already borrowed");
				found = 1;
			}

		}
		if (found == 0) {
			System.out.println("Sorry, this book is not in our catalog");
		}
		
	}
	
	public void printAvailableBooks(){
		for(int k=0;k<i;k++){
			if (books[k].borrowed==false){
				System.out.println(books[k].title);
			}
		}
		if (found==0){
			System.out.println("Sorry, this book is not in our catalog");
		}
		
	}
	
	public void returnBook(String bookname){
		for(int j=0;j<i;j++){
			if (books[j].title.equals(bookname)&& books[j].borrowed==true){
				books[j].borrowed=false;
				System.out.println("You have susccessfully returned "+ books[j].title);
				break;
			}
		}
	}
	
    public static void main(String[] args) { 
        // Create two libraries
    	Library firstLibrary = new Library("10 Main St.");
    	Library secondLibrary = new Library("228 Liberty St."); 
        
    	// Add four books to the first library 
    	firstLibrary.addBook(new Book("The Da Vinci Code"));
        firstLibrary.addBook(new Book("Le Petit Prince"));
        firstLibrary.addBook(new Book("A Tale of Two Cities"));
        firstLibrary.addBook(new Book("The Lord of the Rings"));
        
        
        // Print opening hours and the addresses 
        System.out.println("Library hours:");
        printOpeningHours();
        System.out.println();
        System.out.println("Library addresses:");
        firstLibrary.printAddress();
        secondLibrary.printAddress();
        System.out.println();
        
        // Try to borrow The Lords of the Rings from both libraries 
        System.out.println("Borrowing The Lord of the Rings:");
        
        firstLibrary.borrowBook("The Lord of the Rings");

        firstLibrary.borrowBook("The Lord of the Rings");
               
        secondLibrary.borrowBook("The Lord of the Rings");
        
        System.out.println();
        // Print the titles of all available books from both libraries
        System.out.println("Books available in the first library:");
        firstLibrary.printAvailableBooks();
        System.out.println();
        System.out.println("Books available in the second library:");
        secondLibrary.printAvailableBooks();
        System.out.println();
        // Return The Lords of the Rings to the first library 
        System.out.println("Returning The Lord of the Rings:"); 
        firstLibrary.returnBook("The Lord of the Rings"); 
        System.out.println(); 
        // Print the titles of available from the first library 
        System.out.println("Books available in the first library:"); 
        firstLibrary.printAvailableBooks(); 
    } 

}
