object Main {
  def main(args: Array[String]) {
    for (i <- 1 to 9) {
        for (j <- 1 to 9) {
            printf("%dx%d=%d\n",i,j,i*j)
        }
    }
  }
}