
def count_batteries_by_health(present_capacities):
    h,e,f=0,0,0       # h,e,f variables for storing count of healthy, exchange, failed cells respectively 
    soh = 0.0         # sof - varaible to store health percentage of the cell
    for i in present_capacities:  
        soh = 100 * i/120         # calculation of health
        if(soh>80 and soh<=100):  # updation of count variables based on the range 
            h=h+1
        elif(soh>=63 and soh<=80):
            e = e+1
        else:
            f = f+1
    return {                      # return the dictonary which contains all the category and it's counts as key value pairs 
    "healthy": h,
    "exchange": e,
    "failed": f}


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 72]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
