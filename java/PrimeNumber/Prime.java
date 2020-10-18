public class Prime {
  public static boolean isPrime(int num) {
  
    if (num <= 1 ) {
      return false;
    } 
     if (num > 2 && num %2 == 0) {
      return false;
    }
    
    //if (num==0) return true;
    
   for(int i = 3; i < ((int)Math.sqrt(num) + 1); i+=2){
      if (num % i== 0 ) {
        return false;
      } 
    }
    return true; //TODO
  }
}
